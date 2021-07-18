from kivy.lang.builder import Builder
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty

Builder.load_string(
"""
<SnapScroll>:
    scroll_distance: 500 # helps prevent kivy detecting multiple scroll in one drag.
    bar_width: 0
    scroll_wheel_distance: 0 # disable mouse scrolling
"""
)

class SnapScroll(ScrollView):
    layout = ObjectProperty() # The adaptive layout inside the scrollview; where widgets are added to

    def on_scroll_start(self, touch, check_children=True):
        touch.ud['pos'] = self.to_local(*touch.pos) # saving the touch pos clicked by the user.
        for widget in self.layout.children: # Looping through all widget to get the clicked widget
            if widget != self:
                if widget.collide_point(*touch.ud['pos']):
                    touch.ud['widget'] = widget # saving the widget that recieved the touch
                    touch.ud['index'] = self.layout.children.index(widget) # and its index

        return super().on_scroll_start(touch, check_children=check_children) # Make sure you return this

    def on_scroll_stop(self, touch, check_children=True):
        self._touch = None # cancel touch
        local_touch = self.to_local(*touch.pos)

        if local_touch[1] > touch.ud['pos'][1]: # Comparing current touch pos with the one we saved.
                                                # to know the direction the user is scrolling. 
            if touch.ud['index'] != 0: # If widget is not the first, scroll up
                self.scroll_to(self.layout.children[touch.ud['index']-1], padding=0)
                self.layout.children[touch.ud['index']-1].video_state = 'play' # play next video
                self.layout.children[touch.ud['index']].video_state = 'pause' # pause current video

        elif local_touch[1] < touch.ud['pos'][1]:
            if touch.ud['index'] < len(self.layout.children)-1: # If widget is not the last, scroll down
                self.scroll_to(self.layout.children[touch.ud['index']+1], padding=0)

                self.layout.children[touch.ud['index']+1].video_state = 'play' # play prev video
                self.layout.children[touch.ud['index']].video_state = 'pause' # pause current video

        touch.ud.pop('pos') # we are done with the pos we save so we clear it
        return True #...........
