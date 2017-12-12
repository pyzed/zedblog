/*
* @Author: xiaotuo
* @Date:   2016-10-31 21:54:48
* @Last Modified by:   xiaotuo
* @Last Modified time: 2016-10-31 22:10:10
*/

'use strict';

$(function() {
	$('.captcha-img').click(function() {
		//ajax擅长处理纯文本和json对象
		//对于流媒体不擅长,比较消耗资源
		//只要img的src改变了,就会重新加载图片
		var old_src = $(this).attr('src');
		var src = old_src + '?xx=' + Math.random();
		$(this).attr('src',src);
	});
});