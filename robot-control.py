#!/usr/bin/env python

from pyPS4Controller.controller import Controller


# defining class for controller
class MyController(Controller):
    # initialize attributes for controller
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
        print("pressed x")

    def on_x_release(self):
        print("released x")

    def on_triangle_press(self):
        print("triangle pressed")

    def on_triangle_release(self):
        print("triangle released")

    def on_circle_press(self):
        print("circle pressed")

    def on_circle_release(self):
        print("circle released")

    def on_square_press(self):
        print("square pressed")

    def on_square_release(self):
        print("square released")

    def on_L1_press(self):
        print("L1 pressed")

    def on_L1_release(self):
        print("L1 released")

    def on_L2_press(self, value):
        print("L2 pressed to " + value)

    def on_L2_release(self):
        print("L2 released")

    def on_L3_press(self):
        print("L3 pressed")

    def on_L3_release(self):
        print("L3 released")

    def on_R1_press(self):
        print("R1 pressed")

    def on_R1_release(self):
        print("R1 released")

    def on_R2_press(self, value):
        print("R2 pressed to " + value)

    def on_R2_release(self):
        print("R2 released")

    def on_R3_press(self):
        print("R3 pressed")

    def on_R3_release(self):
        print("R3 released")

    def on_share_press(self):
        print("share button pressed")

    def on_share_release(self):
        print("share button released")

    def on_options_press(self):
        print("option button pressed")

    def on_options_release(self):
        print("option button released")

    def on_down_arrow_press(self):
        print("down arrow pressed")

    def on_up_down_arrow_release(self):
        print("down arrow released")

    def on_up_arrow_press(self):
        print("up arrow pressed")

    def on_right_arrow_press(self):
        print("right arrow pressed")

    def on_left_arrow_press(self):
        print("left arrow pressed")

    def on_left_right_arrow_release(self):
        print("left/right arrow release")

    def on_playstation_button_press(self):
        print("playstation button pressed")

    def on_playstation_button_release(self):
        print("playstation button released")

    def on_L3_up(self, value):
        print("L3 up to " + value)

    def on_L3_down(self, value):
        print("L3 down to " + value)

    def on_L3_left(self, value):
        print("L3 left to " + value)

    def on_L3_right(self, value):
        print("L3 right to " + value)

    def on_R3_up(self, value):
        print("R3 up to " + value)

    def on_R3_down(self, value):
        print("R3 down to " + value)

    def on_R3_left(self, value):
        print("R3 left to " + value)

    def on_R3_right(self, value):
        print("R3 right to " + value)

    def on_L3_x_at_rest(self):
        print("L3 x at rest")

    def on_L3_y_at_rest(self):
        print("L3 y at rest")

    def on_R3_x_at_rest(self):
        print("R3 x at rest")

    def on_R3_y_at_rest(self):
        print("R3 y at rest")


# pointing to where controller is connected to and listening for inputs
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()
