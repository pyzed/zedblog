# -*- coding: utf-8 -*-
# @Author: xiaotuo
# @Date:   2016-10-31 21:23:39
# @Last Modified by:   xiaotuo
# @Last Modified time: 2016-10-31 21:30:56
from django.conf.urls import url,include
import views

urlpatterns = [
    url(r'^captcha/',views.captcha,name='common_captcha'),
]