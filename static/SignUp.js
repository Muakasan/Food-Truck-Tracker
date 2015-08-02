$("#submit-button").click(function(){
    alert($("#username-input").val());
	alert($("#password-input").val());
	alert($("#confirm-password-input").val());
	alert($("#food-truck-name-input").val());
	$SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
	$.getJSON($SCRIPT_ROOT + '/_create_user', {
	    username: $("#username-input").val(),
	}
	window.location.replace("/");
});
