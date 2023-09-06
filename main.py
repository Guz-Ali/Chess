from ChessBoard import ChessBoard
from helper import *

def main():
    """
    Chess game
    """
    chessboard = ChessBoard()
    turn = 1
    while(True):
        team_turn = "WHITE" if turn % 2 == 1 else "BLACK"
        team = chessboard.get_team_by_name(team_turn)
        team_pieces = [[piece.name, piece.position] for pieces in team.pieces for piece in pieces]
        print(f"TURN: {turn}\nTEAM: {team.color}")
        chessboard.print_board() 
        while(True):
            try:
                piece_input = input("CHOOSE PIECE:")
                letter, number = piece_input
                piece_row, piece_col = convert_coordinate_to_idx([letter, int(number)])
                piece_selected = chessboard.board[piece_row][piece_col]
                if not chessboard.piece_is_in_team(team, piece_selected):
                    continue
                goal_input = input("CHOOSE GRID:")
                goal_letter, goal_number = goal_input
                goal = convert_coordinate_to_idx([goal_letter, int(goal_number)])
                break
            except Exception as err:
                print(err)
                print("try again...")

        if chessboard.move_piece(team, piece_selected, goal):
            turn += 1

if __name__ == "__main__":
    main()
