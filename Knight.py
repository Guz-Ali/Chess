from helper import *

class Knight:
    def __init__(self, color, coordinate):
        self.name = KNIGHT_NAME
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

        req_move_dist = [1,2]

        try:
            req_move_dist.remove(move_dist_col)
            if move_dist_row in req_move_dist:
                return True
            else:
                return False            
        except:
            return False
