!function ($) {
	var f = new Date();
	document.getElementById('select-mes-inicial').options[f.getMonth()].selected = true;
	document.getElementById('select-mes-final').options[f.getMonth()].selected = true;

	
}(window.jQuery);