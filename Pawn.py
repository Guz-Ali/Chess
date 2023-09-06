from helper import *

class Pawn:
    def __init__(self, color, coordinate):
        self.name = PAWN_NAME
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
        at_start_position = self.position == self.start_position
        max_move_dist = 2 if at_start_position else 1
        team_switch = 1 if self.color == COLOR_WHITE else -1

        if start_col == goal_col:
            end_row = start_row + max_move_dist*team_switch
            if not at_start_position and end_row==goal_row:
                return True
            
            if team_switch > 0 and (end_row == goal_row or end_row == goal_row+1):
                return True
            elif team_switch < 0 and (end_row == goal_row or end_row == goal_row-1):
                return True
            else:
                return False
        else:
            return False
