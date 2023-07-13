
import kivymd
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from plyer import tts, vibrator
from PIL import Image

class app(MDApp):
    def say(self):
        img = Image.new('RGB', (100, 100), color = 'red')
        img.save('red.jpg')


    def vib(self):
        img = Image.new('RGB', (100, 100), color = 'blue')
        img.save('blue.jpg')


while True:
    app().run()