# Generated by Django 2.0.5 on 2018-05-18 18:19

import api.models
import datetime
from django.conf import settings
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20180515_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('hash', models.CharField(max_length=256)),
                ('file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/Users/sweetchip/PycharmProjects/sweetmon2/file/users/'), upload_to=api.models.get_user_upload_path)),
                ('original_name', models.CharField(max_length=256)),
                ('reg_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('download_count', models.IntegerField(default=0)),
                ('comment', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]