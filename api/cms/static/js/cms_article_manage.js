/*
* @Author: xiaotuo
* @Date:   2016-11-11 22:02:01
* @Last Modified by:   xiaotuo
* @Last Modified time: 2016-11-14 21:03:54
*/

'use strict';
// 删除文章的执行函数
$(function() {
	$('.delete-article-btn').click(function(event) {
		// 阻止a标签的默认行为
		event.preventDefault();
		var result = confirm('您确定要删除这篇文章吗?');
		if(result){
			var trTag = $(this).parent().parent();
			var uid = trTag.attr('data-article-id');
			//发送ajax请求到服务器去删除文章
			xtajax.post({
				'url': '/cms/delete_article/',
				'data': {
					'uid': uid
				},
				'success':function(result) {
					if(result['code'] == 200){
						trTag.hide(1000,function() {
							trTag.remove();
						});
					}else{
						alert(result['message']);
					}
				},
				'error':function(error) {
					alert(error);
				}
			});
		}else{
			//nothing
		}
	});
});

//置顶文章的执行函数
$(function() {
	$('.top-article-btn').click(function(event) {
		event.preventDefault();
		var self = $(this);
		var trTag = $(this).parent().parent();
		var uid = trTag.attr('data-article-id');
		var url = '/cms/top_article/';
		if(self.html().indexOf('取消置顶') >= 0){
			url = '/cms/untop_article/';
		}
		xtajax.post({
			'url': url,
			'data':{
				'uid': uid
			},
			'success':function(result) {
				if(result['code'] == 200){
					console.log('success');
					// 1. 在标题前面添加"[置顶]"的文字
					// var span = $('<span class="top-title-word">[置顶]</span>');
					// var titleTag = $(self).parent().siblings().first().children().eq(0);
					// console.log(titleTag);
					// var title = titleTag.text();
					// titleTag.html('');
					// titleTag.append(span);
					// titleTag.append(title);
					// 2. 之前的"置顶"的按钮的文字应该修改成"取消置顶"
					// self.html('取消置顶');
					window.location = '/cms/';
				}else{
					alert(result['message']);
				}
			},
			'error':function(error) {
				alert(error);
			}
		});
	});
});


//监听分类选择的事件
$(function() {
	$('#category-select').change(function() {
		var categoryId = $(this).val();
		window.location = '/cms/article_manage/1/' + categoryId + '/'
	});
});