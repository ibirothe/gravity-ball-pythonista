from scene import *
from settings import *
from abc import ABC


class LevelEntity(ABC):
    """Base class of all level objects"""
    pass


class Tile(ShapeNode,LevelEntity):
    def __init__(self,moving=False):
        """Initialize a Tile object."""
        super().__init__(ui.Path.rect(0, 0, TILE_SIZE, TILE_SIZE), fill_color=TILE_COLOR)
        self.anchor_point = (0.5, 0.5)


class Coin(ShapeNode,LevelEntity):
    def __init__(self):
        """Initialize a Coin object."""
        super().__init__(ui.Path.oval(0, 0, COIN_SIZE, COIN_SIZE), fill_color=COIN_COLOR)
        self.anchor_point = (0.5, 0.5)


class Hole(ShapeNode,LevelEntity):
    def __init__(self):
        """Initialize a Hole object."""
        super().__init__(ui.Path.oval(0, 0, HOLE_SIZE, HOLE_SIZE), fill_color=HOLE_COLOR)
        self.anchor_point = (0.5, 0.5)
