# -*- coding: utf-8 -*-
# @Author: xiaotuo
# @Date:   2016-11-17 20:08:36
# @Last Modified by:   Administrator
# @Last Modified time: 2016-11-18 21:26:20
from __future__ import unicode_literals

from django.db import models
import uuid
import hashers

class FrontUserModel(models.Model):
	# 用户相关的表，不要使用自增长的id作为主键
	uid = models.UUIDField(primary_key=True,default=uuid.uuid4)
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=128)
	avatar = models.URLField(blank=True)
	is_active = models.BooleanField(default=True)
	date_joined = models.DateTimeField(auto_now_add=True)


	def __init__(self,*args,**kwargs):
		if 'password' in kwargs:
			hash_password = hashers.make_password(kwargs['password'])
			kwargs['password'] = hash_password
		super(FrontUserModel,self).__init__(*args,**kwargs)


	def check_password(self,raw_password):
		return hashers.check_password(raw_password,self.password)


	def set_password(self,raw_password):
		if not raw_password:
			return None

		hash_password = hashers.make_password(raw_password)
		self.password = hash_password
		self.save(update_fields=['password'])


