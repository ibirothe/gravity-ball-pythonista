from scene import *
from settings import *
from abc import ABC, abstractmethod


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


class Hole(ShapeNode):
    def __init__(self):
        """Initialize a Hole object."""
        super().__init__(ui.Path.oval(0, 0, HOLE_SIZE, HOLE_SIZE), fill_color=HOLE_COLOR)
        self.anchor_point = (0.5, 0.5)
        self.board_code = "H"


class Ball(ShapeNode):
    def __init__(self):
        """Initialize the Ball object."""
        super().__init__(ui.Path.oval(0, 0, BALL_SIZE, BALL_SIZE), fill_color=BALL_COLOR)
        self.anchor_point = (0.5, 0.5)
        self.board_code = "B"
