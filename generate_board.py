import random
from collections import defaultdict
from settings import *

def generate_random_board() -> list:
    """Generate a random board maze with entities."""
    carved_board = carve_board()
    board_with_entities = set_entities(carved_board)
    board = add_borders(board_with_entities)

    return board

def sort_entity_positions(board) -> dict:
    """Sort objects and positions by iterating over a board."""
    entity_positions = defaultdict(list)
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            entity_positions[cell].append((x, y))
    return dict(entity_positions)

def carve_board():
    """Create a maze using Recursive Backtracking algorithm."""
    board = [['X' for _ in range(BOARD_DIMENSIONS[0] - 2)] for _ in range(BOARD_DIMENSIONS[1] - 3)]

    def backtrack(x, y):
        board[y][x] = ' '  # Mark the current cell as free space
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Up, Right, Down, Left
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < BOARD_DIMENSIONS[0] - 2 and 0 <= ny < BOARD_DIMENSIONS[1] - 3 and board[ny][nx] == 'X':
                count_visited_neighbors = sum(1 for sx, sy in directions if 0 <= nx + sx < BOARD_DIMENSIONS[0] - 2 and 0 <= ny + sy < BOARD_DIMENSIONS[1] - 3 and board[ny + sy][nx + sx] == ' ')
                if count_visited_neighbors == 1:
                    board[ny][nx] = ' '
                    backtrack(nx, ny)

    start_x, start_y = random.randint(0, BOARD_DIMENSIONS[0] - 3), random.randint(0, BOARD_DIMENSIONS[1] - 4)
    backtrack(start_x, start_y)

    return board

def add_borders(board):
    """Add borders to the maze board."""
    board_with_borders = []
    # Adding horizontal border at the bottom
    board_with_borders.append("X" * BOARD_DIMENSIONS[0])
    board_with_borders.append("X" * BOARD_DIMENSIONS[0])
    # Adding vertical borders
    for row in board:
        board_with_borders.append("X" + ''.join(row) + "X")
    # Adding horizontal border at the top
    board_with_borders.append("X" * BOARD_DIMENSIONS[0])
    return board_with_borders

def set_entities(board):
    """Set entities (Ball, Holes, and Coins) randomly on the maze board, using their set probabilities."""
    # Replacement of exactly one tile with a ball
    while True:
        random_x = random.randint(0, BOARD_DIMENSIONS[0] - 3)
        random_y = random.randint(0, BOARD_DIMENSIONS[1] - 4)
        if board[random_y][random_x] == " ":
            board[random_y][random_x] = "B" 
            break

    for y in range(BOARD_DIMENSIONS[1] - 3):
        for x in range(BOARD_DIMENSIONS[0] - 2):
            entity_rng = random.randint(0, 100)
            # Replacement of tile with hole with set probabilty
            if entity_rng < 100 * HOLE_PROBABILITY:
                if board[y][x] == "X":
                    board[y][x] = "H"
            # Replacement of space with coin with set probabilty
            if entity_rng < 100 * COIN_PROBABILITY:
                if board[y][x] == " ":
                    board[y][x] = "C"
    return board
