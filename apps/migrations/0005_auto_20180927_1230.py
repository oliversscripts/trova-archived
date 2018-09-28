# Generated by Django 2.1.1 on 2018-09-27 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_tvconfig'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tvconfig',
            name='trakt_api_key',
        ),
        migrations.AddField(
            model_name='tvconfig',
            name='api_key_trakt',
            field=models.CharField(blank=True, max_length=254, verbose_name='Trakt API Key'),
        ),
        migrations.AddField(
            model_name='tvconfig',
            name='api_key_tvdb',
            field=models.CharField(blank=True, max_length=254, verbose_name='TVDB API Key'),
        ),
        migrations.AddField(
            model_name='tvconfig',
            name='suggestions_anticipated_enabled',
            field=models.BooleanField(default=True, verbose_name='Anticipated Shows Enabled'),
        ),
        migrations.AddField(
            model_name='tvconfig',
            name='suggestions_enabled',
            field=models.BooleanField(default=True, verbose_name='Suggestions Enabled'),
        ),
        migrations.AddField(
            model_name='tvconfig',
            name='suggestions_popular_enabled',
            field=models.BooleanField(default=True, verbose_name='Popular Shows Enabled'),
        ),
        migrations.AddField(
            model_name='tvconfig',
            name='suggestions_trending_enabled',
            field=models.BooleanField(default=True, verbose_name='Trending Shows Enabled'),
        ),
        migrations.AlterField(
            model_name='tvconfig',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='TV Enabled'),
        ),
    ]