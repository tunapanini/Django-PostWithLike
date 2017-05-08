# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 08:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reddit', '0007_post_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('commented_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default='default value'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='on_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reddit.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='reply_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='reddit.Comment'),
        ),
    ]