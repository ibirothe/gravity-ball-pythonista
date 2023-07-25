from scene import gravity
from settings import *

class GravityControl:
    def __init__(self):
        self.activated = True

    def get_gravity_input(self):
        """Get gravity inputs along the x and y axes."""
        
        if self.activated == False:
            return (0, 0)
        else:
            x_input = 0
            y_input = 0
            g = gravity()
            if abs(g.x) > BOARD_STICKINESS:
                x_input = g.x
            if abs(g.y) > BOARD_STICKINESS:
                y_input = g.y

            return (x_input, y_input)

    def enable(self):
        self.activated =True

    def disable(self):
        self.activated =False
