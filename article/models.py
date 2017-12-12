# -*- coding: utf-8 -*-
# @Author: xiaotuo
# @Date:   2016-10-28 21:20:20
# @Last Modified by:   Administrator
# @Last Modified time: 2016-11-21 20:44:21
from __future__ import unicode_literals

from django.db import models
import uuid
from django.contrib.auth.models import User
from frontauth.models import FrontUserModel

# Create your models here.
class ArticleModel(models.Model):
	# 如果一个field传了editable=False，那么调用diaogo的model_to_dict的时候会丢失这个字段
	uid = models.UUIDField(primary_key=True,default=uuid.uuid4)
	author = models.ForeignKey(User,null=True)
	title = models.CharField(max_length=100)
	category = models.ForeignKey('CategoryModel')
	desc = models.CharField(max_length=200)
	thumbnail = models.URLField(blank=True)
	tags = models.ManyToManyField('TagModel',blank=True)
	content_html = models.TextField()
	release_time = models.DateTimeField(auto_now_add=True,null=True)
	update_time = models.DateTimeField(auto_now=True,null=True)
	read_count = models.IntegerField(default=0)
	top = models.ForeignKey('TopModel',null=True,on_delete=models.SET_NULL)


class TopModel(models.Model):
	# auto_now: save时就会更新
	# auto_now_add: 只有在第一次添加的时候才会修改这个字段
	create_time = models.DateTimeField(auto_now=True)

class CategoryModel(models.Model):
	name = models.CharField(max_length=20,unique=True)

class TagModel(models.Model):
	name = models.CharField(max_length=20,unique=True)

class CommentModel(models.Model):
	author = models.ForeignKey(FrontUserModel)
	content = models.TextField()
	create_time = models.DateTimeField(auto_now_add=True)
	article = models.ForeignKey(ArticleModel)