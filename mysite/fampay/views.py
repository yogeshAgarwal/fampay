import requests
import asyncio
from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone
from rest_framework import response
from rest_framework.views import APIView
from .models import YoutubeVideos
from .utils import MyPaginationMixin
from .serializers import YoutubeVideosSerializer
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework import serializers, status

# Create your views here.
class GetYoutubeData(APIView, MyPaginationMixin):
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    def get(self, request):
        # Youtube.store_data()
        asyncio.run(store_data_of_video())
        data = YoutubeVideos.objects.all().order_by('-publish_datetime')
        if len(data) == 0:
            return Response({'error': 'No data available!'},
                            status=status.HTTP_204_NO_CONTENT)
        page = self.paginate_queryset(data)
        print(page)
        if page is not None:
            serializer = YoutubeVideosSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = YoutubeVideosSerializer(data, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class SearchYoutubeData(APIView, MyPaginationMixin):
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    def get(self, request):
        keyword = request.GET.get('keyword',None)
        if not keyword:
            return Response({'msg':"please provide search keyword"}, status=status.HTTP_400_BAD_REQUEST)

        data = YoutubeVideos.objects.filter(Q(video_title__icontains=keyword),
                                    Q(video_desc__icontains=keyword)).order_by('-publish_datetime')
        if len(data) == 0:
            return Response({'error': 'No data available!'},
                            status=status.HTTP_204_NO_CONTENT)
        page = self.paginate_queryset(data)
        if page is not None:
            serializer = YoutubeVideosSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)






class Youtube:
    api_key_list = [
        'AIzaSyAllJZPVvwlY0eSiOgsz6rLr_AAbdfUX0o'
        ]
    base_url = "https://youtube.googleapis.com/youtube/v3/search"
    
    def hit_api(self, api_key):
        payload={}
        headers = {
            'Accept': 'application/json'
        }
        params = {
            'key': self.api_key_list[api_key],
            'part':'snippet',
            'type':'video',
            'order':'date',
            'publishedAfter':"2020-01-12T14:47:50.000Z"
            }
        response = requests.request("GET", self.base_url, headers=headers, data=payload, params=params)
        if response.status_code not in [200,201]:
            print(response.json())
            if response.status_code == 403 and api_key < len(self.api_key_list)-1:
                new_api_key = (api_key+1)
                self.hit_api(new_api_key)
            return False
        else:
            return response.json()

    def format_data(self, data):
        videos_data = []
        required_data = data['items']
        # print(len(required_data))
        current_time = timezone.now()
        for item in required_data:
            # print(item)
            temp_dict = {}
            temp_dict.update({'video_id':item['id']['videoId']})
            temp_dict.update({'publish_datetime':item['snippet']['publishedAt']})
            temp_dict.update({'video_title':item['snippet']['title']})
            temp_dict.update({'video_desc':item['snippet']['description']})
            temp_dict.update({'thumbnail_url':item['snippet']['thumbnails']['default']['url']})
            temp_dict.update({'created_timestamp':current_time})
            video_ob = YoutubeVideos(**temp_dict)
            videos_data.append(video_ob)
        return videos_data

    @classmethod
    def store_data(cls):
        ob = cls()
        data = ob.hit_api(0)
        if not data:
            return False
        data_to_be_created = ob.format_data(data)
        YoutubeVideos.objects.bulk_create(data_to_be_created)
        return True


async def store_data_of_video():
    if not Youtube.store_data():
        return
    await asyncio.sleep(1)
    await store_data_of_video()



# Youtube.store_data()