# -*- coding: utf-8 -*-
# @Author: xiaotuo
# @Date:   2016-11-17 20:08:36
# @Last Modified by:   Administrator
# @Last Modified time: 2016-11-21 21:09:07
from django.shortcuts import render,reverse
from django.http import HttpResponse
from models import FrontUserModel
from utils import login,logout
import configs
from decorators import front_login_required


def add_user(request):
	user = FrontUserModel(email='ccc@qq.com',username='ccc',password='123')
	user.save()
	return HttpResponse('success')

def test1(request):
	# 从数据库中查找用户，然后密码也要相匹配
	email = 'bbb@qq.com'
	password = '234'
	user = FrontUserModel.objects.filter(email=email).first()
	user.set_password('123')
	# if user.check_password(password):
	# 	return HttpResponse(u'验证成功')
	# else:
	# 	return HttpResponse(u'验证失败')

	return HttpResponse(u'success')




def front_login(request):
	email = 'bbb@qq.com'
	password = '123'
	user = login(request,email,password)
	if user:
		return HttpResponse(u'登录成功')
	else:
		return HttpResponse(u'登录失败')


def check_login(request):
	uid = request.session.get(configs.LOGINED_KEY)
	user = FrontUserModel.objects.filter(pk=uid).first()
	if user:
		return HttpResponse(u'验证成功')
	else:
		return HttpResponse(u'验证失败')


def front_logout(request):
	logout(request)
	return HttpResponse(u'退出成功')


@front_login_required
def decorator_check(request):
	print '-'*30
	print reverse('front_signin') + '?next=' + request.path
	print '-'*30
	return HttpResponse(u'您在已经登录的情况下访问了本页面')

def middleware_test(request):
	if not hasattr(request,'front_user'):
		return HttpResponse(u'失败')
	else:
		return HttpResponse('成功')


