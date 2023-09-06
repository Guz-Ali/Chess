
BISHOP_NAME = "BISHOP"
KING_NAME = "KING"
KNIGHT_NAME = "KNIGHT"
QUEEN_NAME = "QUEEN"
PAWN_NAME = "PAWN"
ROOK_NAME = "ROOK"

COLOR_BLACK = "BLACK"
COLOR_WHITE = "WHITE"
COLOR_INVALID = "INVALID_COLOR"

BOARD_COLORS = [COLOR_BLACK, COLOR_WHITE]
BOARD_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
BOARD_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8]

START_POSITIONS = {
    COLOR_WHITE: {
        BISHOP_NAME: [['C',1], ['F',1]],
        KING_NAME: ['E', 1],
        KNIGHT_NAME: [['B',1], ['G',1]],
        QUEEN_NAME: ['D',1],
        PAWN_NAME: [['A',2], ['B',2], ['C',2], ['D',2], ['E',2], ['F',2], ['G',2], ['H',2]],
        ROOK_NAME: [['A',1], ['H',1]],
    },
    COLOR_BLACK: {
        BISHOP_NAME: [['C',8], ['F',8]],
        KING_NAME: ['E', 8],
        KNIGHT_NAME: [['B',8], ['G',8]],
        QUEEN_NAME: ['D',8],
        PAWN_NAME: [['A',7], ['B',7], ['C',7], ['D',7], ['E',7], ['F',7], ['G',7], ['H',7]],
        ROOK_NAME: [['A',8], ['H',8]],
    }
}

def is_valid_color(color):
    if color in BOARD_COLORS:
        return True
    else:
        return False 
    

def is_valid_position(position):
    letter, number = position
    if letter not in BOARD_LETTERS:
        return False
    if number not in BOARD_NUMBERS:
        return False
    return True

def get_start_positions(color, name):
    return START_POSITIONS[color][name]

def convert_coordinate_to_idx(coordinate):
    letter, number = coordinate
    letter = letter.upper()
    number_idx_row = number - 1
    letter_idx_col = BOARD_LETTERS.index(letter)
    return number_idx_row, letter_idx_col 

def convert_idx_to_coordinate(idx):
    row_idx, col_idx = idx
    number = row_idx + 1
    letter = BOARD_LETTERS[col_idx]
    return letter, number

def print_red(string_to_print, end="\n"):
        print(f"\033[91m{string_to_print:<16}\033[00m".format(string_to_print), end=end)

        # print (f"{piece.name:<16}", end="")