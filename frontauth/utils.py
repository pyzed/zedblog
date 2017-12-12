# -*- coding: utf-8 -*-
# @Author: xiaotuo
# @Date:   2016-11-17 21:58:30
# @Last Modified by:   Administrator
# @Last Modified time: 2016-11-17 22:57:18
from models import FrontUserModel
import configs

def login(request,email,password):
	# 传request是为了做一些登录的数据设置
	# 1. 首先需要拿到用户的数据做一个验证
	user = FrontUserModel.objects.filter(email=email).first()
	if user:
		result = user.check_password(password)
		# 2. 如果验证通过了，就在session当中保存
		# 当前的用户信息，这样下次用户再进来的
		# 时候就直接从session中获取用户信息就可以，
		# 如果没有获取到，说明用户没有登录。
		if result:
			request.session[configs.LOGINED_KEY] = str(user.uid)
			return user
		else:
			return None
	else:
		return None


def logout(request):
	"""
		退出登录
	"""
	try:
		del request.session[configs.LOGINED_KEY]
	except KeyError:
		pass
