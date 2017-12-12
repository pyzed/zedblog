# -*- coding: utf-8 -*-
# @Author: xiaotuo
# @Date:   2016-11-18 21:34:10
# @Last Modified by:   Administrator
# @Last Modified time: 2016-11-18 21:52:56
import hashlib
from django.core.cache import cache
from django.shortcuts import reverse
from django.conf import settings
import time
from django.core import mail

def send_email(request,email,check_url,cache_data=None,subject=None,message=None):
	code = hashlib.md5(str(time.time())+email).hexdigest()
	if cache_data:
		cache.set(code,cache_data,120)
	else:
		cache.set(code,email,120)

	url = request.scheme + '://' + request.get_host() + reverse(check_url,kwargs={'code':code})
	# 2. 发送邮件到email这个邮箱
	if not subject:
		subject = u'邮箱验证'
	# message中应该包含验证的链接
	if not message:
		message = u'博客验证链接,点击 ' + url + u'  ,请在10分钟内完成注册。工作人员不会向您索取验证码，请勿泄露。消息来自：小拓的博客'
	from_mail = settings.EMAIL_HOST_USER
	recipient_list = [email]
	if mail.send_mail(subject,message,from_mail,recipient_list):
		return True
	else:
		return False