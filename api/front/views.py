# -*- coding: utf-8 -*-
# @Author: xiaotuo
# @Date:   2016-10-28 21:19:27
# @Last Modified by:   Administrator
# @Last Modified time: 2016-11-21 21:01:15
from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from article.models import ArticleModel,CategoryModel,CommentModel
from django.conf import settings
from utils import xtjson
from django.forms import model_to_dict
from django.views.decorators.http import require_http_methods
from forms import SignupForm,SigninForm,ForgetpwdForm,ResetpwdForm,CommentForm
from utils.xtemail import send_email
from django.core.cache import cache
from frontauth.models import FrontUserModel
from frontauth.utils import login,logout
from frontauth.decorators import front_login_required

def article_list(request,category_id=0,page=1):
	categoryId = int(category_id)
	currentPage = int(page)

	start = (currentPage-1)*settings.NUM_PAGE
	end = start + settings.NUM_PAGE

	articles = ArticleModel.objects.all()
	
	topArticle = None
	# 如果是处在所有文章界面，那么首先需要获取三篇置顶文章
	# 再获取其他的文章，应该排除置顶的文章
	if categoryId > 0:
		articles = articles.filter(category__pk=categoryId).order_by('-release_time')
	else:
		topArticle = articles.filter(top__isnull=False).order_by('-top__create_time')
		articles = articles.filter(top__isnull=True).order_by('-release_time')

	articles = list(articles.values()[start:end])

	# model_to_dict(articleModel)  ---> 将模型转换成字典
	context = {
		'articles': articles,
		'c_page': currentPage
	}

	if request.is_ajax():
		return xtjson.json_result(data=context)
	else:
		context['categorys'] = CategoryModel.objects.all()
		context['top_articles'] = topArticle
		context['c_category'] = CategoryModel.objects.filter(pk=category_id).first()
		return render(request,'front_article_list.html',context)

def article_detail(request,article_id=''):
	articleId = article_id
	if articleId:
		articleModel = ArticleModel.objects.filter(pk=articleId).first()
		if articleModel:
			comments = articleModel.commentmodel_set.all()
			context = {
				'article':articleModel,
				'categorys': CategoryModel.objects.all(),
				'c_category': articleModel.category,
				'tags': articleModel.tags.all(),
				'comments':comments
			}
			return render(request,'front_article_detail.html',context)
		else:
			xtjson.json_params_error(message=u"该文章不存在")
	else:
		xtjson.json_params_error(message=u'文章id不能为空')


@require_http_methods(['GET','POST'])
def signin(request):
	if request.method == 'GET':
		return render(request,'front_signin.html')
	else:
		form = SigninForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			user = login(request,email,password)
			if user:
				remember = form.cleaned_data.get('remember')
				if remember:
					request.session.set_expiry(None)
				else:
					request.session.set_expiry(0)
				# 跳转到
				nexturl = request.GET.get('next')
				if nexturl:
					return redirect(nexturl)
				else:
					return redirect(reverse('front_index'))
			else:
				return render(request,'front_signin.html',{"error":u'用户名和密码错误'})
		else:
			return render(request,'front_signin.html',{'error':form.get_error()})


@require_http_methods(['GET','POST'])
def signup(request):
	if request.method == 'GET':
		return render(request,'front_signup.html')
	else:
		form = SignupForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')

			# 给用户发送一封确认邮件
			# request,email,check_url,cache_data=None,subject=None,message=None
			cache_data = {
				'email': email,
				'username': username,
				'password': password
			}
			if send_email(request,email,'front_check_email',cache_data):
				return HttpResponse(u'邮件发送成功')
			else:
				return HttpResponse(u'邮件发送失败')
		else:
			return xtjson.json_params_error(message=form.get_error())

def signout(request):
	logout(request)
	return redirect(reverse('front_index'))


def check_email(request,code=''):
	cache_data = cache.get(code)
	email = cache_data.get('email')
	username = cache_data.get('username')
	password = cache_data.get('password')

	user = FrontUserModel(email=email,username=username,password=password)
	user.save()

	return redirect(reverse('front_signin'))


@require_http_methods(['GET','POST'])
def forget_password(request):
	if request.method == 'GET':
		return render(request,'front_forgetpwd.html')
	else:
		form = ForgetpwdForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			# request,email,check_url,cache_data=None,subject=None,message
			user = FrontUserModel.objects.filter(email=email).first()
			if user:
				if send_email(request,email,'front_reset_password'):
					return HttpResponse(u'邮件发送成功')
				else:
					return HttpResponse(u'邮件发送失败')
			else:
				return HttpResponse(u'该邮件不存在')
		else:
			return render(request,'front_forgetpwd.html',{'error':form.get_error()})


def reset_password(request,code=''):
	if request.method == 'GET':
		return render(request,'front_resetpwd.html')
	else:
		form = ResetpwdForm(request.POST)
		if form.is_valid():
			# 需要从缓存中通过code来获取email
			email = cache.get(code)
			password = form.cleaned_data.get('password')
			user = FrontUserModel.objects.filter(email=email).first()
			if user:
				user.set_password(password)
				return HttpResponse(u'密码修改成功')
			else:
				return HttpResponse(u'没有该用户')
		else:
			return xtjson.json_params_error(message=form.get_error())


# 评论相关
@require_http_methods(['POST'])
@front_login_required
def comment(request):
	form = CommentForm(request.POST)
	if form.is_valid():
		content = form.cleaned_data.get('content')
		articleId = form.cleaned_data.get('article_id')
		articleModel = ArticleModel.objects.filter(pk=articleId).first()
		if articleModel:
			commentModel = CommentModel(content=content,article=articleModel,author=request.front_user)
			commentModel.save()
			return redirect(reverse('front_article_detail',kwargs={'article_id':articleId}))
		else:
			return xtjson.json_params_error(message=u'没有这篇文章')
	else:
		return xtjson.json_params_error(message=form.get_error())


def test(request):
	articleModel = ArticleModel.objects.all().first()
	articleDict = model_to_dict(articleModel)
	print articleDict
	return HttpResponse(articleDict)