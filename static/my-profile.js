var sendPosition = function(position){
    window.location.replace("/");
    $.ajax({
        url: 'http://10.180.0.60:5000/_update_location',
        type: 'POST',
        data:JSON.stringify({
            username: "tacotruck",
            x: position.coords.latitude,
            y: position.coords.longitude
        }),        
        contentType: 'application/json;charset=UTF-8',
        success: function(data){alert(data);},
        failure: function(errMsg) {
            alert(errMsg);
        }});
    
}
$("#location-button").click(function(){
        navigator.geolocation.getCurrentPosition(sendPosition)
});

$("#home-button").click(function(){
    window.location.replace("/");
});