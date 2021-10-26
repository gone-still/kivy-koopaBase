from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window

# Set background color for the window:
Window.clearcolor = (1,1,1,1) # RGBA
# Set window size:
# Window.size = (360, 600)

class MainApp(App):

    def build(self):
    
        # Set the layout with extra parameters: # spacing = 10 , padding = 40
        global layout
        layout = GridLayout(cols=1, padding=100)  # col_force_default=False, col_default_width=900

        # Set the image:
        global image
        image = Image(source=inputImageName, allow_stretch=True)  # allow_stretch=True, keep_ratio=True
        # image.stretch = True
        image.width = 200

        # Create the relative layout::
        r1 = RelativeLayout()

        # Set button parameters:
        btnWidth = 350
        btnHeight = 140

        # Create button1:
        btn1 = Button(text="Reset", size_hint=(None, None), width=btnWidth, height=btnHeight,
                      pos_hint={"center_x": 0.5, "center_y": 0.6}) # Adjust til it properly fits into the screen
        btn1.bind(on_press=resetImage)
        # Add to relative layout:
        r1.add_widget(btn1)

        # Create button2:
        btn2 = Button(text="Process", size_hint=(None, None), width=btnWidth, height=btnHeight,
                      pos_hint={"center_x": 0.5, "center_y": 0.3}) # Adjust til it properly fits into the screen
        btn2.bind(on_press=clickProcess)
        # Add to relative layout:
        r1.add_widget(btn2)

        # Add the items to layout:
        layout.add_widget(image, 1)  # Image
        layout.add_widget(r1, 0)  # Relative layout with buttons

        return layout


MainApp().run()