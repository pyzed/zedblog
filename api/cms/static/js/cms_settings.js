/*
* @Author: xiaotuo
* @Date:   2016-11-03 21:09:59
* @Last Modified by:   xiaotuo
* @Last Modified time: 2016-11-08 22:37:39
*/
//获取cookie的方法



'use strict';
$(function() {
	// 初始化七牛SDK代码
	// 初始化七牛的代码必须放在选择图片行为之前
	//发送文件名到服务器
	xtqiniu.setUp({
		'browse_button': 'pickfiles',
		'success':function(up,file,info) {
			var avatar = domain + file.name; //设置图片的完成URL路径
			// 把图片的URL设置进img标签
			$('#pickfiles').attr('src',avatar)
		},
		'error':function(up,err,errTip) {
			console.log(err);
		}
	});
});

	// 提交按钮执行事件
	$('.submit-btn').click(function(event) {
		event.preventDefault();
		var username = $('.username-input').val();
		var avatar = null;
		// 说明有图片上传了
		if(uploader.files.length > 0){
			// src属性代表的就是上传的头像URL
			avatar = $('#pickfiles').attr('src');
		}
		var data = {'username':username};
		if(avatar){
			data['avatar'] = avatar;
		}
		// $.ajax({
		// 	'url': '/cms/update_profile/',
		// 	'method': 'post',
		// 	'data':data,
		// 	'success': function(data) {
		// 		if(data['code'] == 200){
		// 			var alert = $('.alert-success');
		// 			alert.html('更新成功');
		// 			alert.show();
		// 		}
		// 	},
		// 	'error': function(error) {
		// 		console.log(error);
		// 	},
		// 	'beforeSend':function(xhr,settings) {
		// 		var csrftoken = getCookie('csrftoken');
		// 		//2.在header当中设置csrf_token的值
		// 		xhr.setRequestHeader('X-CSRFToken',csrftoken);
		// 	}
		// });
		xtajax.post({
			'url': '/cms/update_profile/',
			'data':data,
			'success': function(data) {
				if(data['code'] == 200){
					var alert = $('.alert-success');
					alert.html('更新成功');
					alert.show();
				}
			},
			'error': function(error) {
				console.log(error);
			},
		});
	});
});
