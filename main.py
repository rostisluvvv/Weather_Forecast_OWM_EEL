import eel
from backend.weather import *


if __name__ == '__main__':
    eel.init('frontend')
    eel.start('index.html', mode="chrome", size=(760, 760))
