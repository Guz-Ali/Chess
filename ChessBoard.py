from Team import Team 
from helper import *

class ChessBoard:
    """
    A chessboard includes two teams:
    White - Black
    """

    def __init__(self):
        self.team_black = Team(COLOR_BLACK)
        # self.team_black.init()
        self.team_white = Team(COLOR_WHITE)
        # self.team_white.init(COLOR_WHITE)
        self.initiate_board()
        self.populate_board()

    def move_piece(self, team, piece, goal):
        if not self.is_valid_move(team, piece, goal):
            return False
        
        goal_row, goal_col = goal
        if self.grid_has_enemy(team, goal):
            piece_on_goal_grid = self.board[goal_row][goal_col]
            piece_on_goal_grid.is_alive = False
            piece_on_goal_grid.position = ['Z',-1]
        current_row, current_col = convert_coordinate_to_idx(piece.position)
        self.board[current_row][current_col] = None
        self.board[goal_row][goal_col] = piece
        goal_letter, goal_number = convert_idx_to_coordinate(goal)
        piece.position = [goal_letter, goal_number]
        
        return True

    def is_valid_move(self, team, piece, goal):
        """
        Returns True: if goal is in borders, piece can move to goal, goal grid or path is not blocked by own team
        """
        goal_row, goal_col = goal
        if not (goal_row <= 8 and goal_row >= 0) or not (goal_col <= 8 and goal_col >= 0):
            return False
        if not piece.is_valid_move_piece(goal):
            return False
        if self.path_is_blocked(team, piece, goal):
            return False
        
        return True

    def path_is_blocked(self, team, piece, goal):
        if self.grid_has_ally(team, goal):
            return True
        if piece.name == KNIGHT_NAME:
            return False
        start_row, start_col = convert_coordinate_to_idx(piece.position)
        goal_row, goal_col = goal

        # horizontal, vertical, diagonal
        if goal_row == start_row:
            for goal_step_grid in [[goal_row, col] for col in range(start_col+1, goal_col)]:
                if self.grid_has_ally(team, goal_step_grid) or self.grid_has_enemy(team, goal_step_grid):
                    return True
        if goal_col == start_col:
            for goal_step_grid in [[row, goal_col] for row in range(start_row+1, goal_row)]:
                if self.grid_has_ally(team, goal_step_grid) or self.grid_has_enemy(team, goal_step_grid):
                    return True
        if abs(goal_row - start_row) == abs(goal_col - start_col):
            row_change = goal_row - start_row
            col_change = goal_col - start_col
            steps = abs(goal_row - start_row)
            
            row_step_multiplier = 1
            col_step_multiplier = 1
            if row_change == col_change and row_change < 0:
                row_step_multiplier *= -1
                col_step_multiplier *= -1
            elif row_change > col_change:
                col_step_multiplier *= -1
            elif row_change < col_change:
                row_step_multiplier *= -1

            steps_to_goal = [[start_row + step*row_step_multiplier, start_col + step*col_step_multiplier] for step in range(1,steps+1)]
            
            for goal_step_grid in steps_to_goal:
                if self.grid_has_ally(team, goal_step_grid):
                    return True
                if self.grid_has_enemy(team, goal_step_grid):
                    goal_step_grid_row, goal_step_grid_col = goal_step_grid
                    if not self.board[goal_row][goal_col] == self.board[goal_step_grid_row][goal_step_grid_col]:
                        return True
        
        return False

    def grid_has_ally(self, team, coordinate):
        row, col = coordinate
        if self.board[row][col] == None:
            return False
        elif self.find_piece_team(self.board[row][col]) == team:
            return True
        else:
            return False

    def grid_has_enemy(self, team, coordinate):
        row, col = coordinate
        if self.board[row][col] == None:
            return False
        elif self.find_piece_team(self.board[row][col]) == team:
            return False
        else:
            return True

    def find_piece_team(self, piece):
        if piece == None:
            return None
        piece_name = piece.name
        if piece in self.team_black.get_pieces_by_type(piece_name):
            return self.team_black
        elif piece in self.team_white.get_pieces_by_type(piece_name):
            return self.team_white
        else:
            print("Error, grid_piece_team: couldn't find piece in neither teams")
            return None
        
    def piece_is_in_team(self, team, piece):
        if piece == None:
            return False
        if team == self.find_piece_team(piece):
            return True
        else:
            return False
    
    def initiate_board(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def populate_board(self):
        self.populate_board_team(COLOR_BLACK)
        self.populate_board_team(COLOR_WHITE)

    def populate_board_team(self, color):
        if color == COLOR_BLACK:
            team = self.team_black
        else:
            team = self.team_white

        for piece_type in team.pieces:
            for piece in piece_type:
                number_pos_row, letter_pos_col  = convert_coordinate_to_idx(piece.position)
                self.board[number_pos_row][letter_pos_col] = piece        

    def print_board(self):
        print(f"    {BOARD_LETTERS[0]:<16}", end="")
        for letter in BOARD_LETTERS[1:]:
            print (f"{letter:<16}", end="")
        print("\n", end="")
        for row in range(8):
            print(row+1, end=" ")
            for col in range(8):
                piece = self.board[row][col]
                if piece == None:
                    print (f"{'  -  ':<16}", end="")
                elif self.piece_is_in_team(self.team_white, piece):
                    print (f"{piece.name:<16}", end="")
                elif self.piece_is_in_team(self.team_black, piece):
                    print_red(piece.name, end="")
            if row < 7:
                print("\n\n\n\n", end="")
            else:
                print("\n\n\n", end="")

    def get_team_by_name(self, team):
        if team == "BLACK":
            return self.team_black
        elif team == "WHITE":
            return self.team_white
        else:
            return None

