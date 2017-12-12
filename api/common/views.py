# -*- coding: utf-8 -*-
# @Author: xiaotuo
# @Date:   2016-10-31 21:23:45
# @Last Modified by:   xiaotuo
# @Last Modified time: 2016-10-31 22:48:13
from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from utils.captcha.xtcaptcha import Captcha
from django.core.cache import cache
from PIL import Image
try:
	from cStringIO import StringIO
except ImportError:
	from io import BytesIO as StringIO

def captcha(request):
	text,image = Captcha.gene_code()
	# image.save('text.png','png') # I/0
	#需要通过StringIO这个类来把图片当成流的形式返回给客户端
	out = StringIO() #获取"管道"
	image.save(out,'png') #把图片保存到管道中
	out.seek(0) #移动文件指针到\第0个位置
	response = HttpResponse(content_type='image/png')
	response.write(out.read())
	# 把验证码数据写入到缓存中,过期时间是2分钟
	# key = text.lower()
	# value = key
	# cache.set(key,value,120)
	return response