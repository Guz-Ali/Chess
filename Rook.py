from helper import *

class Rook:
    def __init__(self, color, coordinate):
        self.name = ROOK_NAME
        self.is_alive = True
        self.set_color(color)
        self.set_position(coordinate)
        self.start_position = self.position

    def set_color(self, color):
        if is_valid_color(color):
            self.color = color
        else:
            print("INVALID COLOR")
            self.color = COLOR_BLACK

    def set_position(self, coordinate):
        if is_valid_position(coordinate):
            self.position = coordinate
        else:
            print("INVALID POSITION")
            self.position = ('A',1)

    def move(self, goal):
        if self.is_valid_move(goal):
            self.position = goal
        else:
            print("INVALID MOVE")
            return

    def is_valid_move_piece(self, goal):
        """
        Basic move boolean, does not consider occuppied grid, elimination, or out of board
        """
        if convert_coordinate_to_idx(self.position) == goal:
            return False
        start_row, start_col = convert_coordinate_to_idx(self.position)
        goal_row, goal_col = goal
        
        if start_row == goal_row or start_col == goal_col:
            return True
        else:
            return False

