$("#submit-button").click(function(){
	if ($("#password-input").val()===$("#confirm-password-input").val()){
    alert($("#username-input").val());
	alert($("#password-input").val());
	alert($("#confirm-password-input").val());
	alert($("#food-truck-name-input").val());
	/*
	$SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
	$.getJSON('_create_user', {
	    username: $("#username-input").val(),
	}
	*/
    
	$.ajax({
		url: 'http://localhost:5000/_create_user',
		type: 'POST',
        data:JSON.stringify({
        	username: $("#username-input").val(),
        	password: $("#password-input").val(),
        	foodTruckName: $("#food-truck-name-input").val(),
        	description: $("#description-input").val()
        }),        
        contentType: 'application/json;charset=UTF-8',
        success: function(data){alert(data);},
        failure: function(errMsg) {
            alert(errMsg);
        }});
	window.location.replace("/");


}
else
{alert("Passwords do not match")}
});
