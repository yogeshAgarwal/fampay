from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import YoutubeVideos



class YoutubeVideosSerializer(serializers.ModelSerializer):

    class Meta:
        model = YoutubeVideos
        fields = "__all__"