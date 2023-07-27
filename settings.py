
# Screen attributes
BACKGROUND_COLOR = "#caa36f"

# Board generation attributes
BOARD_DIMENSIONS = (9, 18)
BOARD_OFFSET = (-5, -15)
BOARD_STICKINESS = 0.05

# Tile attributes
TILE_SIZE = 48
TILE_COLOR = "#ff956b"

# Ball attributes
BALL_SIZE = 20
BALL_SPEED = 13
BALL_COLOR = "#806fac"
RESET_TIME = 60 #ticks

# Coin attributes
COIN_SIZE = 10
COIN_COLOR = "#d6c976"
COIN_LEVEL_REQ = 1
COIN_PROBABILITY = 0.65

# Life Coin atteibutes
LIFE_COIN_SIZE = 10
LIFE_COIN_COLOR = "#8a2b2b"
LIFE_COIN_LEVEL_REQ = 3
LIFE_COIN_PROBABILITY = 0.01

# Hole attributes
HOLE_SIZE = 21
HOLE_COLOR = "#070215"
HOLE_SEC_COLOR = "#4b553e"
HOLE_LEVEL_REQ = 2
HOLE_PROBABILITY = 0.25

# Bird attributes
BIRD_LEVEL_REQ = 4

# Game rules
START_TIME = 80 * 60
HOLE_PENALTY = -5 * 60
LEVEL_TIME_MULTIPLYER = 3

# Game Status
GAME_STATUS_CHANGE  = {
	"start": "new game",
	"new game": "in game",
	"in game": "paused",
	"paused": "in game",
	"game over": "new game",
}
