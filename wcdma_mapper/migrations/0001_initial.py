# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureID',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feature_id', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OSSitem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_code', models.CharField(max_length=20)),
                ('description', models.CharField(default=b'Description.', max_length=128)),
                ('feature_id', models.ForeignKey(to='wcdma_mapper.FeatureID')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RAitem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_code', models.CharField(unique=True, max_length=20)),
                ('description', models.CharField(default=b'Description.', max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='featureid',
            name='ra_item',
            field=models.ForeignKey(to='wcdma_mapper.RAitem'),
            preserve_default=True,
        ),
    ]
