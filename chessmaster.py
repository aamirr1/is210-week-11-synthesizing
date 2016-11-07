#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 11 Synthesizing tasks all"""


class ChessPiece(object):
    """This is a new class called ChessPiece"""
    import time
    
    prefix = ''

    def __init__(self, position):
        if ChessPiece.is_legal_move(self, position):
            self.position = position
            self.moves = []
        else:
            excep = "`{}` not legal position to start at"
            raise ValueError(excep.format(position))

    def algebraic_to_numeric(self, tile):
        """This is a class function called algebraic_to_numeric()"""
        if len(tile) == 2:
            x_coord = "abcdefgh".find(tile[0])
            y_coord = "12345678".find(tile[1])
            if x_coord != -1 and y_coord != -1:
                return (x_coord, y_coord)
        return None

    def is_legal_move(self, position):
        """This is a new function called is_legal_move()"""

        if self.algebraic_to_numeric(position) is None:
            return False
        else:
            return True

    def move(self, position):
        """This is a new function called move"""

        if self.is_legal_move(position):
            oldposition = self.position
            self.position = position
            timestamp = self.time.time()
            the_tup = (oldposition, position, timestamp)
            self.moves.append(the_tup)
            return the_tup
        else:
            return False


class Rook(ChessPiece):
    """This is a new class called Rook"""

    prefix = "R"

    def is_legal_move(self, position):
        cur_pos = self.algebraic_to_numeric(self.position)
        new_pos = self.algebraic_to_numeric(position)
        if new_pos is not None:
            if cur_pos[0] == new_pos[0] or cur_pos[1] == new_pos[1]:
                return True
        return False


class Bishop(ChessPiece):
    """This is a new class called Bishop"""
    prefix = 'B'

    def is_legal_move(self, position):
        """Function is_legal_move"""
        cur_pos = self.algebraic_to_numeric(self.position)
        new_pos = self.algebraic_to_numeric(position)
        if new_pos is not None:
            if abs(cur_pos[0] - new_pos[0]) == abs(cur_pos[1] - new_pos[1]):
                return True
        return False


class King(ChessPiece):
    """This is a new class called King"""

    prefix = "K"

    def is_legal_move(self, position):
        """Function is_legal_move"""
        cur_pos = self.algebraic_to_numeric(self.position)
        new_pos = self.algebraic_to_numeric(position)
        if new_pos is not None:
            if abs(cur_pos[0] - new_pos[0]) <= 1 and \
               abs(cur_pos[1] - new_pos[1]) <= 1:
                return True
        return False


class ChessMatch(object):
    """This is a new class called ChessMatch"""

    def __init__(self, pieces=None):
        if pieces is None:
            self.reset()
        else:
            self.pieces = pieces
            self.log = []

    def reset(self):
        """Function reset"""
    
        self.pieces = {'Ra1': Rook('a1'), 'Rh1': Rook('h1'),
                       'Ra8': Rook('a8'), 'Rh8': Rook('h8'),
                       'Bc1': Bishop('c1'), 'Bf1': Bishop('f1'),
                       'Bc8': Bishop('c8'), 'Bf8': Bishop('f8'),
                       'Ke1': King('e1'), 'Ke8': King('e8')}
        self.log = []

    def move(self, piece, new_pos):
        """Function move"""
        result = self.pieces[piece].move(new_pos)
        if result is not False:
            self.log.append(result)
            new_ent = self.pieces[piece].prefix + new_pos
            self.pieces[new_ent] = self.pieces.pop(piece)
        return False

    def __len__(self):
        return len(self.log)
