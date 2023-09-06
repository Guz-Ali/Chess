from helper import *

class Queen:
    def __init__(self, color):
        self.name = QUEEN_NAME
        self.is_alive = True
        self.set_color(color)
        self.set_position()
        self.start_position = self.position

    def set_color(self, color):
        if is_valid_color(color):
            self.color = color
        else:
            print("INVALID COLOR")
            self.color = COLOR_BLACK

    def set_position(self):
        self.position = get_start_positions(self.color, QUEEN_NAME)
        
    def is_valid_move_piece(self, goal):
        """
        Basic move boolean, does not consider occuppied grid, elimination, or out of board
        """
        if self.position == goal:
            return False
        
        start_row, start_col = convert_coordinate_to_idx(self.position)
        goal_row, goal_col = goal
        
        move_dist_col = abs(start_col - goal_col)
        move_dist_row = abs(start_row - goal_row)

        if move_dist_row == move_dist_col:
            return True
        elif start_col == goal_col or start_row == goal_row:
            return True
        else:
            return False