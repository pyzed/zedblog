/*
* @Author: xiaotuo
* @Date:   2016-11-14 22:01:46
* @Last Modified by:   xiaotuo
* @Last Modified time: 2016-11-14 22:39:01
*/

'use strict';


// 监听编辑操作的函数
$(function() {
	var dialog = $("#category-modal");
	$('.edit-category-btn').click(function(event) {
		event.preventDefault();
		dialog.modal('show');
		var categoryId = $(this).parent().parent().attr('data-category-id');
		$('#category-submit-btn').attr('data-category-id',categoryId)
	});
	$('#category-submit-btn').click(function() {
		var categoryId = $('#category-submit-btn').attr('data-category-id');
		var name = $("#category-input").val();
		console.log('categoryId:'+categoryId+',name:'+name);
		xtajax.post({
			'url': '/cms/edit_category/',
			'data':{
				'category_id': categoryId,
				'name': name
			},
			'success':function(result) {
				if(result['code'] == 200){
					// 修改当前分类的标题
					$('.category-tr').each(function() {
						if($(this).attr("data-category-id") == categoryId){
							// 修改名称
							$(this).children().eq(0).html(name);
						}
					});
				}else{
					alert(result['message']);
				}
			},
			'error':function(error) {
				alert(error);
			},
			'complete':function() {
				dialog.modal('hide');
			}
		});
	});
});

//删除分类监听函数
$(function() {
	$('.delete-category-btn').click(function(event) {
		event.preventDefault();
		var trTag = $(this).parent().parent();
		var categoryId = trTag.attr('data-category-id');
		var result = confirm('您确定要删除本分类吗?');
		if(result){
			xtajax.post({
				'url': '/cms/delete_category/',
				'data':{
					'category_id':categoryId
				},
				'success':function(ret) {
					if(ret['code'] == 200){
						// 把当前这个tr给删除掉就可以了
						trTag.remove();
					}else{
						alert(ret['message']);
					}
				},
				'error':function(error) {
					alert(error);
				}
			});
		}
	});
});