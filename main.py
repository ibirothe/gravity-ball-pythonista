from scene import *
from settings import *
from user_input import get_gravity_input
from level_entities import *
from generate_board import *

class Game(Scene):
    def setup(self):
        """Setup the game."""
        self.background_color = BACKGROUND_COLOR

        # Generate a random Board and extract the entity positions from it
        self.board = generate_random_board()
        self.entity_positions = sort_entity_positions(self.board)

        # Creating parent nodes for the different Entity Types
        self.tiles = Node(parent=self)
        self.holes = Node(parent=self)
        self.coins = Node(parent=self)
        self.balls = Node(parent=self)

        # Creating the Board Entities and adding them to a parent
        self.create_entities(Tile)
        self.create_entities(Hole)
        self.create_entities(Coin)

        # Creating the ball object, the player is going to control
        self.create_entities(Ball)
        self.ball = self.balls.children[0]

    def create_entities(self, entity_type):
        """Create objects of the given entity type."""
        # Accessing the creation list of the requested entity type
        creation_list = self.entity_positions.get(entity_type().board_code, [])

        # Assigning the entity types to a parent node using a dictionary
        entity_parent_map = {
            Tile: self.tiles,
            Hole: self.holes,
            Coin: self.coins,
            Ball: self.balls
        }

        entity_parent = entity_parent_map.get(entity_type)
        if entity_parent is None:
            return

        # Creating entities and defining their positions according to the creation list
        for x, y in creation_list:
            entity = entity_type()
            entity.position = (x * TILE_SIZE + BOARD_OFFSET[0], y * TILE_SIZE + BOARD_OFFSET[1])
            entity_parent.add_child(entity)

    def horizontal_movement(self, x_velocity):
        """Move the ball horizontally."""
        x, y = self.ball.position
        new_x = x + x_velocity * BALL_SPEED
        self.ball.position = (new_x, y)
        collision_side = "right" if x_velocity > 0 else "left" if x_velocity < 0 else "none"
        success, collision_x = self.check_collision(collision_side)
        if success:
            self.ball.position = (collision_x, y)

    def vertical_movement(self, y_velocity):
        """Move the ball vertically."""
        x, y = self.ball.position
        new_y = y + y_velocity * BALL_SPEED
        self.ball.position = (x, new_y)
        collision_side = "top" if y_velocity > 0 else "bottom" if y_velocity < 0 else "none"
        success, collision_y = self.check_collision(collision_side)
        if success:
            self.ball.position = (x, collision_y)
        
    def check_collision(self, side):
        """Check collisions of the ball with the map borders."""
        ball_offset = BALL_SIZE // 2 + 2
        for tile in self.tiles.children:
            if tile.frame.intersects(self.ball.frame):
                if side == "right":
                    return True, tile.bbox.min_x - ball_offset
                elif side == "left":
                    return True, tile.bbox.max_x + ball_offset
                elif side == "top":
                    return True, tile.bbox.min_y - ball_offset
                elif side == "bottom":
                    return True, tile.bbox.max_y + ball_offset
        return False, None

    def update(self):
        """Update the game state."""
        velocity = get_gravity_input()
        self.horizontal_movement(velocity[0])
        self.vertical_movement(velocity[1])


if __name__ == '__main__':
    run(Game(), PORTRAIT, show_fps=True)
