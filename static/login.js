/*
$("#submit-button").click(function(){
	window.location.replace("../templates/index.html");
    username = $("#username-input").val()
    $.ajax({
		url: 'http://10.180.0.60:5000/_update_location',
		type: 'POST',
        data:JSON.stringify({
            username: "username",
        	navigator.geolocation.getCurrentPosition(showPosition);
        }),        
        contentType: 'application/json;charset=UTF-8',
        success: function(data){alert(data);},
        failure: function(errMsg) {
            alert(errMsg);
        }});
}
*/
$("#home-button").click(function(){
    window.location.replace("/");
});