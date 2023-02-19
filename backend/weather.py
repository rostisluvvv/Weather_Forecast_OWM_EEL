from pyowm.commons.exceptions import NotFoundError
from pyowm import OWM
import eel

from config.config import load_config


@eel.expose
def get_weather(city):
    owm = OWM(load_config('.env').weather.token)
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

    try:
        return weather_info

    except NotFoundError:
        pass
