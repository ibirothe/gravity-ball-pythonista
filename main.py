from scene import *
from settings import *
from level_entities import *

class Game(Scene):
    def setup(self):
        """Setup the game."""
        self.background_color = BACKGROUND_COLOR

        self.tiles = Node(parent=self)
        self.holes = Node(parent=self)
        self.coins = Node(parent=self)
        self.ball = Node(parent=self)

    def update(self):
        """Update the game state."""
        pass


if __name__ == '__main__':
    run(Game(), PORTRAIT, show_fps=True)
