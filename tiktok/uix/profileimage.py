from kivy.lang.builder import Builder
from kivymd.uix.floatlayout import MDFloatLayout

Builder.load_string(
"""
#: import get_color_from_hex kivy.properties.get_color_from_hex
<ProfileImg>:
    size_hint: None, None
    size: '50dp', '50dp'
    radius: '25dp'
    md_bg_color: [1, 1, 1, 1]
    img: ''
    FitImage:
        source: root.img
        radius: root.radius
        size: '45dp', '45dp'
        size_hint: None, None
        center: root.center
    MDLabel: #Didnt use icon because it wasnt bold enough
        text: '+'
        font_size: '15sp'
        pos_hint: {'center_x':.5, 'y':-.15}
        size: dp(20), dp(20)
        size_hint: None, None
        md_bg_color: get_color_from_hex('#FC2D55')
        radius: '20dp'
        halign: 'center'
        bold: True
"""
)

class ProfileImg(MDFloatLayout):
    pass