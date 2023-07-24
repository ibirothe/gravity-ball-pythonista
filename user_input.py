from scene import gravity
from settings import *

def get_gravity_input():
    """Get gravity inputs along the x and y axes."""
    x_input = 0
    y_input = 0
    g = gravity()
    if abs(g.x) > BOARD_STICKINESS:
        x_input = g.x
    if abs(g.y) > BOARD_STICKINESS:
        y_input = g.y

    return (x_input, y_input)
