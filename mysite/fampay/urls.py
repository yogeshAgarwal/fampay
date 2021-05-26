from django.urls import path
from fampay.views import GetYoutubeData, SearchYoutubeData

urlpatterns = [
    path('get_list/',GetYoutubeData.as_view(),name='get_list'),
    path('serach/',SearchYoutubeData.as_view(),name='serach')
]
