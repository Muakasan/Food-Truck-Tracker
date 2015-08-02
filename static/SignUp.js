$("#submit-button").click(function(){
	if ($("#password-input").val()===$("#confirm-password-input").val()){

	/*
	$SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
	$.getJSON('_create_user', {
	    username: $("#username-input").val(),
	}
	*/
    
	$.ajax({
		url: 'http://10.180.0.60:5000/_create_user',
		type: 'POST',
        data:JSON.stringify({
        	username: $("#username-input").val(),
        	password: $("#password-input").val(),
        	food_truck_name: $("#food-truck-name-input").val(),
        	description: $("#description-input").val()
        }),        
        contentType: 'application/json;charset=UTF-8',
        success: function(data){
        	alert(data);
        	$.initNameSpaceStorage("food-truck-finder"):
        	storage - $.localStorage;
        	storage.set("username", username)
        	storage.remove("username")
        	storage.get("get")

        },
        failure: function(errMsg) {
            alert(errMsg);
        }});
	window.location.replace("/");
	

}
else
{alert("Passwords do not match")}
});
