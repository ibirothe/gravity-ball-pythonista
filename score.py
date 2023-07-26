from scene import *
from settings import *

def setup_score_board_bg(parent):
    """This is a purely cosmetic method, that is not relevant for the game mechanics."""
    def create_shape(width, height, fill_color, position_y):
        shape = ShapeNode(ui.Path.rect(0, 0, width, height), fill_color=fill_color)
        shape.anchor_point = (0.5, 1)
        x = min(get_screen_size()) // 2
        y = position_y
        shape.position = x, y
        parent.add_child(shape)

    outline_height = TILE_SIZE
    outline_width = TILE_SIZE * 7
    filling_height = TILE_SIZE - 10
    filling_width = TILE_SIZE * 7 - 10

    create_shape(outline_width, outline_height, BACKGROUND_COLOR, TILE_SIZE)
    create_shape(filling_width, filling_height, COIN_COLOR, TILE_SIZE - 5)

class ScoreBoard(LabelNode):
    def __init__(self):
        super().__init__("text", font=('Helvetica', 20))
        self.anchor_point = (0, 1)
        self.position = TILE_SIZE - 10, TILE_SIZE - 12

    def update_text(self, time, score, level, balls):
        self.text = f"⏳ {time:3} ✨ {score} 🕹 {level} 🏐 {balls}"

    def game_over(self):
        self.text = "☠️ GAME OVER ☠️"
