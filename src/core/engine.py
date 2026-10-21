
from kivy.config import Config
from kivy.utils import platform

if platform not in ('androis', 'ios'):
    scale = 0.9
    width = 360
    height = 800
    Config.set('graphics', 'width', int(width*scale))
    Config.set('graphics', 'height', int(height * scale))
    Config.set('graphics','resizable','0')
    Config.set('input', 'mouse', 'mouse,diable_multitouch')



from kivymd.app import MDApp
class MatchIt(MDApp):
    def build(self):
        return

if __name__ == '__main__':
    MatchIt().run()