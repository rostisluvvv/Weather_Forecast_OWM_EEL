from dataclasses import dataclass
from environs import Env


@dataclass
class Weather:
    token: str


@dataclass
class Config:
    weather: Weather


def load_config(path) -> Config:
    env = Env()
    env.read_env(path)
    return Config(weather=Weather(token=env('API_TOKEN')))


# print(load_config('.env').weather.token)

