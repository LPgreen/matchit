from kivy.config import Config
from kivy.utils import platform

def set_window_size(width=360, height=800, scale=1):
    if platform not in ('android', 'ios'):
        Config.set('graphics', 'width', int(width*scale))
        Config.set('graphics', 'height', int(height * scale))
        Config.set('graphics','resizable','0')
        Config.set('input', 'mouse', 'mouse,disable_multitouch')