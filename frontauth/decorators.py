# -*- coding: utf-8 -*-
# @Author: xiaotuo
# @Date:   2016-11-17 22:37:10
# @Last Modified by:   Administrator
# @Last Modified time: 2016-11-21 21:09:13

# 实现一个login_required的装饰器
# 需求：
# 1. 如果用户没有登录，跳转到登录页面
# 2. 如果用户已经登录，不执行任何操作
# 3. 如果用户没有登录，跳转到登录页面，并且需要
# 添加一个next的url到url中

from models import FrontUserModel
import configs
from django.shortcuts import redirect,reverse

def front_login_required(func):
	def wrapper(request,*args,**kwargs):
		uid = request.session.get(configs.LOGINED_KEY)
		if uid:
			# 如果uid存在，则说明当前已经登录
			# 更为严谨的做法是，要拿到这个uid
			# 去数据库中查找这个用户，如果找到了
			# 才说明确实是登陆了，如果没有找到，
			# 说明没有登录。但是这种方法比较耗
			# 性能，因此我们采用第一种方式
			return func(request,*args,**kwargs)
		else:
			# 如果session中不存在uid，说明没有登录
			url = reverse('front_signin') + '?next=' + request.path
			# /cms/login/?next=/cms/
			# reverse('front_signin') + '?next=' + request.path
			return redirect(url)
	return wrapper


