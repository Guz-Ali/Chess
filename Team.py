from Bishop import Bishop
from King import King
from Knight import Knight
from Queen import Queen
from Pawn import Pawn
from Rook import Rook
from helper import *

class Team:
    """
    A team includes pieces such as:
    Bishop - 2
    King - 1
    Knight - 2
    Queen - 1
    Pawn - 8
    Rook - 2
    A team should also have a color (white-black).
    """
    # def __init__(self):
    #     pass

    def __init__(self, color):
        self.set_color(color)
        self.init_bishops()
        self.init_king()
        self.init_knights()
        self.init_queen()
        self.init_pawns()
        self.init_rooks()
        self.set_pieces()

    def set_color(self, color):
        if is_valid_color(color):
            self.color = color
        else:
            self.color = COLOR_BLACK

    def init_bishops(self):
        # initialize two bishops with their starting coordinates.
        start_positions = get_start_positions(self.color, BISHOP_NAME)
        self.bishops = [Bishop(self.color, s_pos) for s_pos in start_positions]

    def init_king(self):
        self.king = [King(self.color)]
    
    def init_knights(self):
        start_positions = get_start_positions(self.color, KNIGHT_NAME)
        self.knights = [Knight(self.color, s_pos) for s_pos in start_positions]

    def init_queen(self):
        self.queen = [Queen(self.color)]

    def init_pawns(self):
        start_positions = get_start_positions(self.color, PAWN_NAME)
        self.pawns = [Pawn(self.color, s_pos) for s_pos in start_positions]

    def init_rooks(self):
        start_positions = get_start_positions(self.color, ROOK_NAME)
        self.rooks = [Rook(self.color, s_pos) for s_pos in start_positions]

    def set_pieces(self):
        self.pieces = [self.pawns, self.rooks, self.knights, self.bishops, self.queen, self.king]

    def get_pieces_by_type(self, piece_name):
        for pieces in self.pieces:
            if piece_name == pieces[0].name:
                return pieces