from scene import *
from settings import *
from user_input import GravityControl
from timer import TickTimer
from level_entities import *
from generate_board import *
from score import *


class Game(Scene):
    def setup(self):
        """Setup the game."""
        self.background_color = BACKGROUND_COLOR

        # Create gravity-like controller using the gyroscope
        self.controller = GravityControl()

        # Create timer objects
        self.animation_timer = TickTimer()
        self.game_timer = TickTimer(3600)

        # Game progress attributes
        self.level = 0
        self.score = 0
        self.balls_left = 5

        # Creating parent nodes for different Entity Types
        self.tiles = Node(parent=self)
        self.holes = Node(parent=self)
        self.coins = Node(parent=self)
        self.balls = Node(parent=self)
        self.score_board = Node(parent=self)

        # Create score board background (cosmetic)
        setup_score_board_bg(self.score_board)

        # Initialize the score board LabelNode
        self.score_board_text = ScoreBoard()
        self.score_board.add_child(self.score_board_text)

        # Initialize the game board
        self.new_board()

    def new_board(self):
        # Increase level
        self.level += 1

        # Generate a random Board and extract the entity positions from it
        self.board = generate_random_board()
        self.entity_positions = sort_entity_positions(self.board)

        # Creating the Board Entities and adding them to a parent
        self.create_entities(Tile)
        self.create_entities(Hole)
        self.create_entities(Coin)

        # Creating the ball object, the player is going to control
        self.create_entities(Ball)
        self.ball = self.balls.children[0]

        # Saving the initial position to reset the ball when needed
        self.reset_position = (self.ball.position[0], self.ball.position[1])

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

    def collect_coin(self):
        """Collect coins if the ball collides with them."""
        for coin in self.coins.children:
            if coin.frame.intersects((self.ball.position[0], self.ball.position[1], 8, 8)):
                coin.remove_from_parent()
                self.score += 5

    def fall_check(self):
        """Check if the ball falls into a hole."""
        for hole in self.holes.children:
            if hole.bbox.intersects((self.ball.position[0], self.ball.position[1], 0, 0)):
                self.fall(hole.position)

    def fall(self, hole_pos):
        """Define the animation and play the animation of the ball falling into a hole."""
        # Create animation objects
        roll_in_anm = Action.move_to(hole_pos[0], hole_pos[1], 0.07)
        fade_out = Action.fade_to(0, 0.18)
        wait_anm = Action.wait(0.2)
        # Create sequence of animations
        hole_anm = Action.sequence(roll_in_anm, wait_anm, fade_out)
        # Disable controller while animation is playing
        self.controller.disable()
        # Run the animation sequence
        self.ball.run_action(hole_anm)
        # Run a countdown timer before resetting the ball
        self.animation_timer.set_ticks(RESET_TIME)
        if self.animation_timer.ticks_left == 1:
            # Apply penalty to the game timer
            self.game_timer.modify(HOLE_PENALTY)
            self.reset_ball()

    def reset_ball(self):
        """Remove all balls from the game and add a new ball at the reset position."""
        # Removing all ball objects
        for ball in self.balls.children:
            ball.remove_from_parent()

        # Creating, positioning and assigning the new ball object
        self.create_entities(Ball)
        self.ball = self.balls.children[0]
        self.ball.position = self.reset_position
        self.controller.enable()
        self.balls_left = max(0, self.balls_left - 1)

    def clear_board(self):
        # Delete the current board
        for tile in self.tiles.children:
            tile.remove_from_parent()
        for hole in self.holes.children:
            hole.remove_from_parent()
        for ball in self.balls.children:
            ball.remove_from_parent()

    def update(self):
        """Update the game state."""
        # Get current velocity via gravity controller
        velocity = self.controller.get_gravity_input()

        # Apply movement per axis and check for collisions with tiles
        self.horizontal_movement(velocity[0])
        self.vertical_movement(velocity[1])

        # Check for collisions with coins
        self.collect_coin()

        # Check for collisions with holes
        self.fall_check()

        # Update the set timers
        self.animation_timer.tick()
        self.game_timer.tick()
        self.score_board_text.update_text(self.game_timer.get_seconds(), self.score, self.level, self.balls_left)

        # Check for all coins being collected
        if len(self.coins.children) == 0:
            self.clear_board()
            self.new_board()
            self.game_timer.ticks_left += min(3600, self.game_timer.ticks_left * LEVEL_TIME_MULTIPLYER)
            self.score += self.game_timer.get_seconds()

        if self.game_timer == 0 or self.balls_left == 0:
            self.animation_timer.set_ticks(1)
            self.score_board_text.game_over()
            if self.animation_timer.ticks_left == 0:
                self.paused = True


if __name__ == "__main__":
    run(Game(), PORTRAIT, show_fps=True)
