from pyS4Controller.controller import Controller
while True:
    class MyController(Controller):
    
        def __init__(self, **kwargs):
            Controller.__init__(self, **kwargs)

        def on_x_press(self):
            print("Hello world")

        def on_x_release(self):
            print("Goodbye world")