# -*- coding: utf-8 -*-
# @Author: xiaotuo
# @Date:   2016-11-18 20:52:20
# @Last Modified by:   Administrator
# @Last Modified time: 2016-11-18 21:04:09
import configs
from models import FrontUserModel

def auth(request):
	# 给模板添加一个front_user变量
	# 1. 首先要判断当前用户是否已经登录，如果已经登录，才添加front_user变量
	# 2. 如果当前已经登录了，并且request已经有front_user属性了，直接拿来返回就可以了，就没有必要去从数据库中查找了
	# 3. 如果当前已经登录，但是request还没有front_user属性，那么就需要从数据库中获取user对象，然后返回回去。
	if request.session.get(configs.LOGINED_KEY):
		if hasattr(request,'front_user'):
			print request.front_user.username
			return {'front_user':request.front_user}
		else:
			uid = request.session.get(configs.LOGINED_KEY)
			user = FrontUserModel.objects.filter(pk=uid)
			return {'front_user':user}
	else:
		# 如果没有登录还是需要返回一个空字典回去
		return {}
