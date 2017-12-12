# -*- coding: utf-8 -*-
# @Author: xiaotuo
# @Date:   2016-11-03 20:54:16
# @Last Modified by:   xiaotuo
# @Last Modified time: 2016-11-03 20:58:22
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CmsUser(models.Model):
	avatar = models.URLField(max_length=100,blank=True)
	# 使用一對一,django中的User模型必須和CmsUser中一對一的對應,
	# 不能出現一個User对应多个CmsUser的情况
	user = models.OneToOneField(User)