from django.db import models
from django.db.models.base import Model

# Create your models here.

class YoutubeVideos(models.Model):
    video_id = models.CharField(max_length=100,db_index=True,null=False)
    video_title = models.CharField(max_length=100)
    video_desc = models.CharField(max_length=500)
    publish_datetime = models.DateTimeField(db_index=True,null=False)
    thumbnail_url = models.CharField(max_length=100)
    created_timestamp = models.DateTimeField(null=False,blank=False)
