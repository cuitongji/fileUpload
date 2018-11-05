# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UpInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('uname', models.CharField(max_length=50)),
                ('uploadFile', models.FileField(upload_to='upapp/upload/')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('uname', models.CharField(max_length=50)),
                ('upwd', models.CharField(max_length=20)),
                ('uchname', models.CharField(max_length=20, null=True)),
                ('uenname', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
