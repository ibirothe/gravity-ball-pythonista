import random

def generate_random_board() -> list:
    # Placeholder for future board maze generation.
    board = [
    "XXXXXXXXX",
    "XXXXXXXXX",
    "X x  B  X",
    "XX   X XX",
    "X  XH   X",
    "XX  XXXXX",
    "X  XX  HX",
    "X x   x X",
    "X  X C  X",
    "XX XX x X",
    "X   X  CX",
    "XX XXXXXX",
    "X   XX  X",
    "XX  X   X",
    "XXX   X X",
    "X   XXX X",
    "X   X   X",
    "XXXXXXXXX",
    ]
    return board

def sort_entity_positions(board) -> dict:
    """Sort objects and positions by iterating over a board."""
    entity_positions = {}
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell not in entity_positions.keys():
                entity_positions[cell] = []
                entity_positions[cell].append((x,y))
            else:
                entity_positions[cell].append((x,y))
    return entity_positions
