from kivy.lang.builder import Builder
from kivymd.uix.floatlayout import MDFloatLayout

Builder.load_string(
"""
<AlbumImg>:
    size_hint: None, None
    size: '50dp', '50dp'
    radius: '25dp'
    md_bg_color: [0, 0, 0, 1]
    img: ''
    FitImage:
        source: root.img
        radius: root.radius
        size: '30dp', '30dp'
        size_hint: None, None
        center: root.center

"""
)

class AlbumImg(MDFloatLayout):
    pass