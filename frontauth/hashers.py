# -*- coding: utf-8 -*-
# @Author: xiaotuo
# @Date:   2016-11-17 21:28:44
# @Last Modified by:   Administrator
# @Last Modified time: 2016-11-17 21:55:33
import hashlib
import configs

def make_password(raw_password,salt=None):
	if not salt:
		salt = configs.PASSWORD_SALT

	hash_password = hashlib.md5(salt+raw_password).hexdigest()
	return hash_password


def check_password(raw_password,hash_password):
	# 首先需要对raw_password使用和创建用户的时候
	# 一样的加密算法来进行加密,而且使用的“盐”必 
	# 须一样，然后再和数据库中
	# 的密码进行对比，这样才行。
	if not raw_password:
		return False

	tmp_password = make_password(raw_password)
	if tmp_password == hash_password:
		return True
	else:
		return False