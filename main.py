from scene import *
from settings import *
from level_entities import Tile, Coin, Hole, Ball
from generate_board import generate_random_board, sort_entity_positions 

class Game(Scene):
    def setup(self):
        """Setup the game."""
        self.background_color = BACKGROUND_COLOR

        board = generate_random_board()
        self.entity_positions = sort_entity_positions(board)

        self.tiles = Node(parent=self)
        self.holes = Node(parent=self)
        self.coins = Node(parent=self)
        self.ball = Node(parent=self)

        self.create_entities(Tile)
        self.create_entities(Hole)
        self.create_entities(Coin)
        self.create_entities(Ball)

    def create_entities(self, entity_type):
        """Create objects of the given entity type."""
        entity_list = self.entity_positions[entity_type().board_code]
        entity_container = None

        if entity_type == Tile:
            entity_parent = self.tiles
        elif entity_type == Hole:
            entity_parent = self.holes
        elif entity_type == Coin:
            entity_parent = self.coins
        elif entity_type == Ball:
            entity_parent = self.ball

        for index, _ in enumerate(entity_list):
            entity = entity_type()
            entity.position = (entity_list[index][0] * TILE_SIZE + BOARD_OFFSET[0], entity_list[index][1] * TILE_SIZE + BOARD_OFFSET[1])
            entity_parent.add_child(entity)

    def update(self):
        """Update the game state."""
        pass


if __name__ == '__main__':
    run(Game(), PORTRAIT, show_fps=True)
