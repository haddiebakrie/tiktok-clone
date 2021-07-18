from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder

Builder.load_string(
"""
<NavBar>:
    md_bg_color: [0, 0, 0, 1]
    orientation: 'vertical'
    height: dp(50)
    size_hint_y: None
    MDBoxLayout:
        padding: '10dp', '5dp'
        spacing: '5dp'
        NavIcon:
            icon: '\U0000E80B'
            text: 'Home'
            icon_size: '18sp'
            text_size: '10sp'
            screen: 'feed'
        NavIcon:
            icon: '\U0000E80F'
            text: 'Discover'
            icon_size: '18sp'
            text_size: '10sp'
            screen: 'discover'
        Image:
            source: 'assets/img/plus.png'
            size_hint_x: None
            width: '35dp'
        NavIcon:
            icon: '\U0000E80C'
            text: 'Inbox'
            icon_size: '18sp'
            text_size: '10sp'
            screen: 'inbox'
        NavIcon:
            icon: '\U0000E80D'
            text: 'Me'
            icon_size: '18sp'
            text_size: '10sp'
            screen: 'profile'
    MDBoxLayout:
        size_hint_y: None
        height: '5dp'
"""
)

class NavBar(MDBoxLayout):
    pass