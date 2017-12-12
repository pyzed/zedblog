'use strict'


// 设置左边导航的状态的执行函数
$(function() {
	// 获取url中的category的id
	var url = window.location.href;
	// http://127.0.0.1:8000/article_list/2/
	// http:  127.0.0.1:8000 article_list 2
	// 有两种情况：
	// 1. 处在所有文章页面的时候，categoryId就不用获取了，只需要给第1个li添加active类就可以了
	// 2. 处在其他类的时候，就需要去解析url，然后从第4个位置获取category_id
	if(url.indexOf('article_list') > 0){
		var urlArray = url.split('/');
		var categoryId = urlArray[4];
		var liTag = $('#category-box').children('[data-category-id='+categoryId+']');
		liTag.addClass('active').siblings().removeClass('active');
	}else if(url.indexOf('article_detail') > 0){
		var categoryId = $('h2.article-title').attr('data-category-id');
		var liTag = $('#category-box').children('[data-category-id='+categoryId+']');
		liTag.addClass('active').siblings().removeClass('active');
	}else{
		$('#category-box').children().eq(0).addClass('active').siblings().removeClass('active');
	}
});