# I have issues playing video with ffmpeg so i use ffpyplayer
import os
os.environ['KIVY_VIDEO'] = 'ffpyplayer'
import kivy
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import FadeTransition, ScreenManager
from kivymd.font_definitions import theme_font_styles


from screens.screens import *
from uix.uix import *
from kivy.core.text import LabelBase

class WindowManager(ScreenManager):
    pass

Window.size = (310, 600)

class TikTok(MDApp):
    def build(self):
        self.wm = WindowManager(transition=FadeTransition()) #Transition between screens
        self.theme_cls.theme_style= 'Dark'
        # Registering the TikTok font so i can use its icons
        # and it has to be before the screen is created
        LabelBase.register(name="TikTokIcons", fn_regular="TikTokIcons.ttf")
        theme_font_styles.append('TikTokIcons')
        self.theme_cls.font_styles["TikTokIcons"] = ["TikTokIcons", 16, False, 0.15]

        screens = [
            Home(name='home')
        ]


        for screen in screens:
            self.wm.add_widget(screen)
        
        return self.wm

if __name__ == '__main__':
    TikTok().run()