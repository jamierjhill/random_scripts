var city = "New York";


$.getJSON(
    "http://api.openweathermap.org/data/2.5/weather?q=" +
     city + 
     "&units=imperial&appid=3bf3678e2a0d7862f46cb77f9b511658", 
function(data) {
 console.log(data);
var icon = 
"http://www.openweathermap.org/img/w/" + data.weather[0].icon + ".png";
var temp = Math.floor(data.main.temp);
var weather = data.weather[0].main;

$(".icon").attr("src", icon);
$(".weather").append(weather);
$(".temp").append(temp);
});