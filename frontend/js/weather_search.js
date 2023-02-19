async function get_weather_info (){
    let city = document.getElementById("search-city").value;
    let weather_info = await eel.get_weather(city)();
    for (let [key, value] of Object.entries(weather_info)) {
        document.getElementById(key).innerHTML=value;
    }
}

document.getElementById("btncity").onclick = get_weather_info;



