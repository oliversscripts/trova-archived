# Generated by Django 2.2.dev20180919211339 on 2018-09-26 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20180926_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='trova_admin',
            field=models.BooleanField(default=False),
        ),
    ]
