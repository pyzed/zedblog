# -*- coding: utf-8 -*-
# @Author: xiaotuo
# @Date:   2016-11-17 20:49:59
# @Last Modified by:   Administrator
# @Last Modified time: 2016-11-18 20:49:09
from django.conf.urls import url,include
import views

urlpatterns = [
	url(r'^add_user/$',views.add_user),
	url(r'^test1/$',views.test1),
	url(r'^front_login/$',views.front_login),
	url(r'^front_logout/$',views.front_logout),
	url(r'^check_login/$',views.check_login),
	url(r'^decorator_check/$',views.decorator_check),
	url(r'^middleware_test/$',views.middleware_test),
]