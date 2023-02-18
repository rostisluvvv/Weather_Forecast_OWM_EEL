from pyowm import OWM
import eel


@eel.expose
def get_weather(city):
    owm = OWM('8afcf8ea6330577aaf06e872f0f01fba')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    temp = w.temperature('celsius')
    t1 = temp['temp']
    t2 = temp['feels_like']

    status = w.status
    wi = w.wind()['speed']

    weather_info = {
        'city': city,
        'temp': t1,
        'temp_feels': t2,
        'wind': wi,
        'status': status
    }
    return weather_info
