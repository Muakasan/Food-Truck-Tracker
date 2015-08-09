   $("#home-button").click(function(){
                window.location.replace("/");
            });
            
            var x = document.getElementById("coords");
            var lat = 0
            var long = 0

            function getLocation() {
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(showPosition);
                } else {
                    x.innerHTML = "Geolocation is not supported by this browser.";
                }
            }

            function showPosition(position) {
               // x.innerHTML = "Latitude: " + position.coords.latitude + 
               // "<br>Longitude: " + position.coords.longitude; 
                lat= position.coords.latitude;
                long = position.coords.longitude;
            }
            getLocation()
            var myMap;
            function initialize() {
                //var position = navigator.geolocation.getCurrentPosition()
                var mapOptions = {   
                    zoom: 8,
                    mapTypeId: google.maps.MapTypeId.ROADMAP,
                    zoom:18
                }
                myMap = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
                var initialLocation = null;
                if(navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(function(position) {
                        initialLocation = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
                        myMap.setCenter(initialLocation);
                        var marker = new google.maps.Marker({
                            position: initialLocation,
                            map: myMap,
                            label: "Me"
                        });
                    });

                } 
                  
                console.log(initialLocation);
                //google.maps.event.addDomListener(window, 'load', initialize);
            }
            
             $(document).ready(function() {
                var request = $.ajax({
                    type: "POST",
                    url: "/truck_array",
                    data: {"name":""}, // if you wanted to specifiy what list then pass an actual name
                    dataType: "html"
                });

                request.done(function(JSON_array_string) {
                    //alert(JSON_array);
               
                    array_data = JSON.parse(JSON_array_string);

                 
                    //from here you have your array to play with
                    for(i=0;i<array_data.length;i++)
                    {
                        if(array_data[i].hasOwnProperty("loc")){
                        var marker = new google.maps.Marker({
                            position: new google.maps.LatLng(parseFloat(array_data[i].loc[0]), parseFloat(array_data[i].loc[1])),
                            map: myMap,
                            title: i +""
                        });
                        var html = $("<div>", {"id":"content"+i}).append(
                                                $("<h4>", {"text":array_data[i].food_truck_name}),
                                                $("<p>", {"text":array_data[i].description}))
                        var infowindow = new google.maps.InfoWindow({
                          content: html.prop("outerHTML")
                          });

                        google.maps.event.addListener(marker, 'click', function() {
                            infowindow.open(myMap,marker);
                        });
                        }
                        /*
                        google.maps.event.addListener(marker, 'click', function() {
                          infowindow.open(map,marker);
                          });
                        }

                        var contentString = "<p>Finish</p>";
                        /*
                        $("<div>", {"id":"content"+i}).append(
                                                $("<h4>", {"text":array_data[i].food_truck_name}),
                                                $("<p>", {"text":array_data[i].description})).toString();
                        */
                        /*
                        var infoWindow = new google.maps.InfoWindow({
                            content: contentString
                        });
                          
                            google.maps.event.addListener(marker, 'click', function() {
                            infoWindow.open(map,marker);
                        });
*/
                   // }
                    }
                });
            });

            google.maps.event.addDomListener(window, 'load', initialize);