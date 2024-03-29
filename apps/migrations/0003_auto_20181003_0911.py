# Generated by Django 2.1.1 on 2018-10-03 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20180930_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookRequest',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Request Id')),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MovieRequest',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Request Id')),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MusicRequest',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Request Id')),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TvRequest',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Request Id')),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tvconfig',
            name='sonarr_search_missing',
            field=models.BooleanField(default=False, verbose_name='Sonarr Search on Add'),
        ),
    ]
