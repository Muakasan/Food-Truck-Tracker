$("#submit-button").click(function(){
	if ($("#password-input").val()===$("#confirm-password-input").val()){
	$.ajax({
		url: '/_create_user',
		type: 'POST',
        data:JSON.stringify({
        	username: $("#username-input").val(),
        	password: $("#password-input").val(),
        	food_truck_name: $("#food-truck-name-input").val(),
        	description: $("#description-input").val()
        }),        
        contentType: 'application/json;charset=UTF-8',
        success: function(data){
        	//alert(data);

        },
        failure: function(errMsg) {
            //alert(errMsg);
        }});
	window.location.replace("/");
	

}
else
{
    alert("Passwords do not match")}
});

$("#home-button").click(function(){
    window.location.replace("/");
});
