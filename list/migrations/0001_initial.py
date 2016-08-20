# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='inst',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inst', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=100)),
                ('geo', models.IntegerField(default=0)),
                ('gec', models.IntegerField(default=0)),
                ('obco', models.IntegerField(default=0)),
                ('obcc', models.IntegerField(default=0)),
                ('sco', models.IntegerField(default=0)),
                ('scc', models.IntegerField(default=0)),
                ('sto', models.IntegerField(default=0)),
                ('stc', models.IntegerField(default=0)),
                ('geopd', models.IntegerField(default=0)),
                ('gecpd', models.IntegerField(default=0)),
                ('obcopd', models.IntegerField(default=0)),
                ('obccpd', models.IntegerField(default=0)),
                ('scopd', models.IntegerField(default=0)),
                ('sccpd', models.IntegerField(default=0)),
                ('stopd', models.IntegerField(default=0)),
                ('stcpd', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
