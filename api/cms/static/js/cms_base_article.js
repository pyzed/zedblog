/*
* @Author: xiaotuo
* @Date:   2016-11-07 21:21:53
* @Last Modified by:   xiaotuo
* @Last Modified time: 2016-11-11 20:55:59
*/

'use strict';


// 初始化simditor的函数
$(function() {
	var editor,toolbar;
	toolbar = ['title', 'bold', 'italic', 'underline', 'strikethrough', 'fontScale', 'color', '|', 'ol', 'ul', 'blockquote', 'code', 'table', '|', 'link', 'image', 'hr', '|', 'indent', 'outdent', 'alignment'];
	Simditor.locale = 'zh-CN';
	editor = new Simditor({
		textarea: $('#simditor'),
		toolbar: toolbar,
		pasteImage: true
	});
	// 加到window上去,其他地方才能访问到editor这个变量
	window.editor = editor;
});

//添加分類的函數
$(function() {
	var dialog = $('#category-modal');
	$('#category-btn').click(function() {
		dialog.modal('show');
	});
	$('#category-submit-btn').click(function() {
		// 1. 获取到输入框中的值
		var categoryInput = $("#category-input");
		var categoryName = categoryInput.val();
		// 2. 提交到服务器
		xtajax.post({
			'url': '/cms/add_category/',
			'data':{'categoryname':categoryName},
			'success':function(result) {				
				if(result['code'] == 200){
					// 请求正常
					var data = result['data'];
					var select = $('#category-select');
					dialog.modal('hide');
					var option = $('<option></option>');
					option.attr('value',data['id']);
					option.html(data['name']);
					// 通过append添加进去的,一定是在最后面
					select.append(option);
					// 可以通过last方法获取到刚刚添加进去的option
					select.children().last().attr('selected','selected').siblings().removeAttr('selected');
				}else{
					
				}
			},
			'error':function(error) {
				console.log(error);
			}
		});
	});
});


//添加标签函数
$(function() {
	var dialog = $('#tag-modal');
	$('#tag-btn').click(function() {
		// 弹出一个模态对话框
		dialog.modal('show');
	});
	//创建label标签的函数
	function addLabelTag() {
		var label = $("<label class='checkbox-inline'></label>");
					//创建一个input
		var input = $("<input type='checkbox'/>");
		input.val(data['id']);
		input.attr('checked','checked');
		label.append(input);
		label.append(data['name']);
		$("#tag-box").append(label);
	}
	$('#tag-submit-btn').click(function() {
		var tagElement = $("#tag-input");
		var tagname = tagElement.val();
		//提交到服务器
		xtajax.post({
			'url': '/cms/add_tag/',
			'data':{'tagname':tagname},
			'success':function(result) {				
				if(result['code'] == 200){
					// 请求正常
					var data = result['data'];
					// 1. 第一种方式是通过jquery原始的dom操作来创建新的label和input标签
					// addLabelTag()
					// 2. 第二种方式是通过arttemplate模板的方式进行创建
					var tpl = template('cms_tag_template',{'id':data['id'],'name':data['name']});
					$("#tag-box").append(tpl);
					dialog.modal('hide');
				}else{
					console.log(result['message']);
				}
			},
			'error':function(error) {
				console.log(error);
			}
		});
	});
});


// 上传图片执行函数
$(function() {
	//把一些固定的参数封装进函数,把那些需要更改的参数不进行封装
	var uploader = xtqiniu.setUp({
		'browse_button':'thumbnail-btn',
		'success':function(up,file,info) {
				// 把图片的URL设置input里面
			$('#thumbnail-input').val(file.name);
		},
		'error':function(up,err,errTip) {
			console.log(err);
		}
	});
});


// 添加文章的执行函数
$(function() {
	$('#submit-article-btn').click(function() {
		// 获取元素
		var titleElement = $('#title-input');
		var categoryElement = $('#category-select');
		var descElement = $('#desc-input');
		var thumbnailElement = $('#thumbnail-input');
		var tagElements = $('.tag-checkbox');

		// 获取数据
		var title = titleElement.val();
		var category = categoryElement.val();
		var desc = descElement.val();
		var thumbnail = thumbnailElement.val();
		var tags = [];
		tagElements.each(function() {
			if($(this).is(':checked')){
				var tagId = $(this).val();
				tags.push(tagId);
			}
		});
		var content_html = editor.getValue();
		var data = {
			'title': title,
			'category': category,
			'desc': desc,
			'thumbnail': thumbnail,
			'tags[]': tags,
			'content_html': content_html,
			'uid': titleElement.attr('data-article-id')
		};
		
		// 通过ajax发布到服务器
		xtajax.post({
			'url': window.location.href,
			'data': data,
			'success':function(result) {
				if (result['code'] == 200) {
					$('#submit-success-modal').modal('show');
					titleElement.val('');
					descElement.val('');
					thumbnailElement.val('');
					tagElements.removeAttr('checked');
					editor.setValue('');
				}else{
					alert(result['message']);
				}
			},
			'error': function(err) {
				console.log(err);
			}
		});
	});
	$('#back-home-btn').click(function() {
		window.location = '/cms/';
	});
	$('#write-again-btn').click(function() {
		$('#submit-success-modal').modal('hide');
	});
});