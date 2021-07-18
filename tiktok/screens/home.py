from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from data import data as users
from uix.videocard import VideoCard
from kivy.core.window import Window
from kivy.metrics import dp

Builder.load_string(
"""
#: import FadeTransition kivy.uix.screenmanager.FadeTransition
<Home>:
    layout: layout
    MDBoxLayout:
        orientation: 'vertical'
        ScreenManager:
            id: screen_manager
            transition: FadeTransition()
            Screen:
                name: 'feed'
                MDBoxLayout:    
                    md_bg_color: [0, 0, 0, 1]
                    size_hint_y: None
                    height: root.height - dp(50)
                    SnapScroll:
                        layout: layout
                        MDBoxLayout:
                            id: layout
                            orientation: 'vertical'
                            adaptive_height: True
                          

            Screen:
                name: 'discover'
                MDLabel:
                    text: 'Discover'
                    halign: 'center'
            Screen:
                name: 'upload'
                MDLabel:
                    text: 'Upload'
            Screen:
                name: 'inbox'
                MDLabel:
                    text: 'Inbox'
                    halign: 'center'
            Screen:
                name: 'profile'
                MDLabel:
                    text: 'Profile'
                    halign: 'center'
        MDBoxLayout:    
            size_hint_y: None
            height: '50dp'
            NavBar:
                screen_manager: screen_manager
            
    MDBoxLayout:
        height: dp(20)
        size_hint_y: None
        pos_hint: {'top':.95, 'center_x':.5}
        adaptive_width: True
        spacing: '5dp'
        MDTextButton:
            text: 'Following'
            font_size: '16sp'
            theme_text_color: 'Custom'
            text_color: [1, 1, 1, .5]
        MDSeparator:
            orientation: 'vertical'
            width: '2dp'
            md_bg_color: [1, 1, 1, .5]
        MDTextButton:
            text: 'Following'
            font_size: '16sp'
            theme_text_color: 'Custom'
            text_color: [1, 1, 1, 1]
            bold: True
"""
)

class Home(Screen):
    data = []
    def __init__(self, **kw):
        for profile in users:
            _data = {
                'name':profile['name'],
                'source':profile['video'],
                'caption':profile['caption'],
                'song_name':profile['song_name'],
                'profile_pic':profile['profile_pic'],
                'likes':profile['likes'],
                'comments':profile['comments'],
                'shares':profile['shares'],
                'album_pic':profile['album_pic'],
            }
            self.data.append(_data)
        super().__init__(**kw)
    def on_enter(self, *args):
        for data in self.data:
            video_card = VideoCard()
            video_card.data = data
            video_card.height = Window.size[1] - dp(50)
            if self.data.index(data) == 0: # if the video is the first, play it
                video_card.video_state = 'play'

            self.layout.add_widget(video_card)
        return super().on_enter(*args)