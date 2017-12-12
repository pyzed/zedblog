/*
* @Author: xiaotuo
* @Date:   2016-11-14 22:41:24
* @Last Modified by:   xiaotuo
* @Last Modified time: 2016-11-14 22:46:00
*/

'use strict';

$(function() {
	var url = window.location.href;
	var ulTag = $('#sub-nav');
	var index = 0;
	if(url.indexOf('category_manage') > 0){
		index = 1;
	}else{
		index = 0;
	}
	ulTag.children().eq(index).addClass('active').siblings().removeClass('active');
});