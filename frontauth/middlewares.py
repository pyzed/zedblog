# -*- coding: utf-8 -*-
# @Author: xiaotuo
# @Date:   2016-11-18 20:40:01
# @Last Modified by:   Administrator
# @Last Modified time: 2016-11-18 21:05:02
from django.utils.deprecation import MiddlewareMixin
from models import FrontUserModel
import configs

class AuthMiddleware(MiddlewareMixin):

	def process_request(self,request):
		# front_user
		# 1.先要判断当前用户是否已经登录，如果已经登录，则添加front_user属性
		if request.session.get(configs.LOGINED_KEY):
			# 2. 再判断当前request是否已经添加了front_user这个属性，
			# 因为如果front_user这个属性已经添加到request上了，
			# 就不需要重复添加
			if not hasattr(request,'front_user'):
				uid = request.session.get(configs.LOGINED_KEY)
				user = FrontUserModel.objects.filter(pk=uid).first()
				setattr(request,'front_user',user)