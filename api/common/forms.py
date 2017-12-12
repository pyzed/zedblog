# -*- coding: utf-8 -*-
# @Author: xiaotuo
# @Date:   2016-11-18 21:22:55
# @Last Modified by:   Administrator
# @Last Modified time: 2016-11-18 21:23:37
from django import forms
import json
from utils import xtjson

class BaseForm(forms.Form):
	def get_error(self):
		errors = self.errors.as_json()
		error_dict = json.loads(errors)
		message = ''
		# 只取字典中的第一个值
		# {u'captcha': [{u'message': u'xxx', u'code': u''}]}
		for k,v in error_dict.items():
			message = v[0].get('message',None)
		return message

	def get_error_response(self):
		if self.errors:
			return xtjson.json_params_error(message=self.get_error())
		else:
			return xtjson.json_result()