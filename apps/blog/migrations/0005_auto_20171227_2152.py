# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-27 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171224_1612'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='keyword',
            options={'ordering': ['id'], 'verbose_name': '关键词', 'verbose_name_plural': '关键词'},
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(default='SEO空间是一个研究网站SEO优化和分享Python学习的个人博客。本博客的后端使用Django框架搭建，前端使用Bootstrap4样式，主要分享博主在Python实战、搜索引擎优化、电子商务运营等方面的学习心得，网站所有文章都是原创。', help_text='用来作为SEO中description,长度参考SEO标准', max_length=240, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.TextField(default='SEO空间是一个研究网站SEO优化和分享Python学习的个人博客。本博客的后端使用Django框架搭建，前端使用Bootstrap4样式，主要分享博主在Python实战、搜索引擎优化、电子商务运营等方面的学习心得，网站所有文章都是原创。', help_text='用来作为SEO中description,长度参考SEO标准', max_length=240, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='icon',
            field=models.CharField(default='fa fa-pencil', max_length=50, verbose_name='图标'),
        ),
    ]
