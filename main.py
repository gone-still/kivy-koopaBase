from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window

# Set background color for the window:
Window.clearcolor = (1,1,1,1) # RGBA
# Set window size:
Window.size = (360, 600)

class MainApp(App):
    def build(self):
        # Set the layout with extra parameters: # spacing = 10 , padding = 40
        layout = GridLayout(cols=1)
        # Set the image:
        img = Image(source="koopa01.png")

        # Create the relative layout::
        r1 = RelativeLayout()

        # Set button parameters:
        btnWidth = 100
        btnHeight = 40

        # Create button1:
        btn1 = Button(text="Test 1", size_hint=(None,None), width=btnWidth, height=btnHeight,
                      pos_hint={"center_x":0.5,"center_y":0.8})
        # Add to relative layout:
        r1.add_widget(btn1)

        # Create button2:
        btn2 = Button(text="Test 2", size_hint=(None,None), width=btnWidth, height=btnHeight,
                      pos_hint={"center_x":0.5,"center_y":0.6} )
        # Add to relative layout:
        r1.add_widget(btn2)

        # Add the items to layout:
        layout.add_widget(img) # Image
        layout.add_widget(r1) # Relative layout with buttons

        return layout


MainApp().run()
