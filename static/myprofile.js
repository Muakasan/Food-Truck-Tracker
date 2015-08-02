$("location-btn").click(function(){
    	$.ajax({
		url: 'http://10.180.0.60:5000/_update_location',
		type: 'POST',
        data:JSON.stringify({
            username: "username",
        	x: position.coords.latitude,
        	y: position.coords.longitude
        }),        
        contentType: 'application/json;charset=UTF-8',
        success: function(data){alert(data);},
        failure: function(errMsg) {
            alert(errMsg);
        }});
	window.location.replace("/");
}