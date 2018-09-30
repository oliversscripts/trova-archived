# Generated by Django 2.2.dev20180919211339 on 2018-09-30 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tvconfig',
            name='api_key_trakt',
        ),
        migrations.AddField(
            model_name='tvconfig',
            name='api_key_trakt_client_id',
            field=models.CharField(blank=True, max_length=254, verbose_name='Trakt API Client ID'),
        ),
        migrations.AddField(
            model_name='tvconfig',
            name='api_key_trakt_client_secret',
            field=models.CharField(blank=True, max_length=254, verbose_name='Trakt API Client Secret'),
        ),
    ]