# Generated by Django 2.0.2 on 2018-02-07 21:41

from django.db import migrations


def merge_news_and_events(apps, schema_editor):
    News = apps.get_model('modeemintternet', 'News')
    Event = apps.get_model('modeemintternet', 'Event')

    for event in Event.objects.all():
        News.objects.create(
            title=event.title,
            text=event.text,
            location=event.location,
            lat=event.lat,
            lon=event.lon,
            starts=event.starts,
            ends=event.ends,
            posted=event.posted,
            modified=event.modified,
            poster=event.poster,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('modeemintternet', '0019_auto_20180207_2340'),
    ]

    operations = [
    ]
