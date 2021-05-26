# Generated by Django 2.2.23 on 2021-05-26 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeVideos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(db_index=True, max_length=100)),
                ('video_title', models.CharField(max_length=100)),
                ('video_desc', models.CharField(max_length=500)),
                ('publish_datetime', models.DateTimeField(db_index=True)),
                ('thumbnail_url', models.CharField(max_length=100)),
                ('created_timestamp', models.DateTimeField()),
            ],
        ),
    ]