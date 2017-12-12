/*
* @Author: xiaotuo
* @Date:   2016-11-04 21:14:43
* @Last Modified by:   xiaotuo
* @Last Modified time: 2016-11-04 21:40:42
*/

'use strict';
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// 自己封装的ajax请求
// 'beforeSend':function(xhr,settings) {
// 				var csrftoken = getCookie('csrftoken');
// 				//2.在header当中设置csrf_token的值
// 				xhr.setRequestHeader('X-CSRFToken',csrftoken);
// 			}

// function A(args){
// 	console.log(args);
// }

// function B(args){
// 	args['username'] = 'xt';
// 	A(args);
// }

// A({'username':'xt'});
// A({'username':'xt'});
// A({'username':'xt'});
// A({'username':'xt'});
// B();


var xtajax = {
	'get':function(args) {
		args['method'] = 'get';
		this.ajax(args);
	},
	'post':function(args) {
		args['method'] = 'post';
		this.ajax(args);
	},
	'ajax':function(args) {
		// 设置csrftoken
		this._ajaxSetup();
		$.ajax(args);
	},
	'_ajaxSetup': function() {
		$.ajaxSetup({
			'beforeSend':function(xhr,settings) {
				var csrftoken = getCookie('csrftoken');
				//2.在header当中设置csrf_token的值
				xhr.setRequestHeader('X-CSRFToken',csrftoken);
			}
		});
	}
}