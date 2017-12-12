# -*- coding: utf-8 -*-
# @Author: xiaotuo
# @Date:   2016-10-28 21:18:13
# @Last Modified by:   xiaotuo
# @Last Modified time: 2016-11-14 23:10:24
from django.conf.urls import url,include
import views

urlpatterns = [
    url(r'^$',views.article_manage,name='cms_index'),
    url(r'^login/$',views.cms_login,name='cms_login'),
    url(r'^logout/$',views.cms_logout,name='cms_logout'),
    url(r'^article_manage/(?P<page>\d+)/(?P<category_id>\d+)/$',views.article_manage,name='cms_article_manage'),
    url(r'^add_article/$',views.add_article,name='cms_add_article'),
    url(r'^edit_article/(?P<pk>[\w\-]+)$',views.edit_article,name='cms_edit_article'),
    url(r'^delete_article/$',views.delete_article,name='cms_delete_article'),
    url(r'^top_article/$',views.top_article,name='cms_top_article'),
    url(r'^untop_article/$',views.untop_article,name='cms_untop_article'),
    url(r'^settings/$',views.cms_settings,name='cms_settings'),
    url(r'^update_profile/$',views.update_profile,name='cms_update_profile'),
    url(r'^get_token/$',views.get_token,name='cms_get_token'),
    url(r'^update_email/$',views.update_email,name='cms_update_email'),
    url(r'^check_email/(?P<code>\w+)$',views.check_email,name='cms_check_email'),
    url(r'^add_category/$',views.add_category,name='cms_add_category'),
    url(r'^delete_category/$',views.delete_category,name='cms_delete_category'),
    url(r'^edit_category/$',views.edit_category,name='cms_edit_category'),
    url(r'^category_manage/$',views.category_manage,name='cms_category_manage'),
    url(r'^add_tag/$',views.add_tag,name='cms_add_tag'),
    url(r'^email_success/$',views.email_success,name='cms_email_success'),
    url(r'^email_fail/$',views.email_fail,name='cms_email_fail'),
    url(r'^test/$',views.test)
]