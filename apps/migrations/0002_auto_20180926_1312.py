# Generated by Django 2.1.1 on 2018-09-26 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='plex_id',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
