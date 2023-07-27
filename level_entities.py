from scene import *
from settings import *
import random


class Tile(ShapeNode):
    def __init__(self):
        """Initialize a Tile object."""
        super().__init__(ui.Path.rect(0, 0, TILE_SIZE, TILE_SIZE), fill_color=TILE_COLOR)
        self.anchor_point = (0.5, 0.5)
        self.board_code = "X"


class Coin(ShapeNode):
    def __init__(self):
        """Initialize a Coin object."""
        super().__init__(ui.Path.oval(0, 0, COIN_SIZE, COIN_SIZE), fill_color=COIN_COLOR)
        self.anchor_point = (0.5, 0.5)
        self.board_code = "C"


class LifeCoin(ShapeNode):
    def __init__(self):
        """Initialize a Coin object."""
        super().__init__(ui.Path.oval(0, 0, COIN_SIZE, COIN_SIZE), fill_color=LIFE_COIN_COLOR)
        self.anchor_point = (0.5, 0.5)
        self.board_code = "L"


class Hole(ShapeNode):
    def __init__(self):
        """Initialize a Hole object."""
        super().__init__(ui.Path.oval(0, 0, HOLE_SIZE, HOLE_SIZE), fill_color=HOLE_COLOR)
        self.stroke_color = HOLE_SEC_COLOR
        self.anchor_point = (0.5, 0.5)
        self.board_code = "H"


class Ball(ShapeNode):
    def __init__(self, pos = (0,0)):
        """Initialize the Ball object."""
        super().__init__(ui.Path.oval(pos[0], pos[1], BALL_SIZE, BALL_SIZE), fill_color=BALL_COLOR)
        self.anchor_point = (0.5, 0.5)
        self.board_code = "B"
        self.reset_position = None
        

class FlyingNumber(LabelNode):
    def __init__(self, score, position):
        """Initialize a informative short-lived Label."""
        super().__init__(f"{score}", font=('Helvetica', 12))
        self.anchor_point = (0.5, 0.5)
        self.position = position[0], position[1]+5
        # Perform animation action
        self.run_action(Action.move_by(0, 20, 0.5, TIMING_EASE_OUT))
        self.run_action(Action.fade_to(0,0.5))


class Bird(LabelNode):
    def __init__(self):
        """Initialize a bird enemy."""
        super().__init__("🦅", font=('Helvetica', 45))
        self.anchor_point = (0.5, 0.5)
        y = random.randint(2,16) * TILE_SIZE + BOARD_OFFSET[1]
        # Perform animation action
        self.position  = min(get_screen_size())+30, y
        self.run_action(Action.move_to(-30, self.position[1], 3.5, TIMING_LINEAR))
        
