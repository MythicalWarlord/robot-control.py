#!/usr/bin/env python

from pyPS4Controller.controller import Controller


# defining class for controller
class MyController(Controller):
    # initialize attributes for controller
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
        print("Hello world")

    def on_x_release(self):
        print("Goodbye world")


# pointing to where controller is connected to and listening for inputs
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()
