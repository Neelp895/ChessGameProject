import math

import numpy
import numpy as np
import pygame as pg
import pygame.display
import random
import time

rookMoves = 0
bishopMoves = 0
leftLane = 0
rightLane = 0
topLane = 0
bottomLane = 0
pawnMoves = 0

class Node:

    def __init__(self, obj_board, In_row, In_col, Fn_row, Fn_col):
        self.obj_board = obj_board
        self.In_row = In_row
        self.In_col = In_col
        self.Fn_row = Fn_row
        self.Fn_col = Fn_col

class new_space:
    identity = 0
    stEval = 0


    def __init__(self, x, y):
        self.cord_x = x
        self.cord_y = y
        self.rect = pg.Rect(x, y, 80, 80)



    def valid_move(piece, obj_board, In_row, In_col, Fn_row, Fn_col):
        piece.valid_move = False

        return piece.valid_move


class King:
    identity = 6
    alive = True
    stEval = 900

    def __init__(self, white, x, y):
        self.white = white
        if white == False:
            self.image = pygame.image.load("BlackKing.png")
        else:
            self.image = pygame.image.load("WhiteKing.png")
        self.cord_x = x
        self.cord_y = y
        self.rect = pg.Rect(x, y, 80, 80)

    def valid_move_white(piece, obj_board, In_row, In_col, Fn_row, Fn_col):
        piece.valid_move = False

        if (Fn_row < 0 or Fn_row > 7 ) or (Fn_row < 0 or Fn_row > 7 ):
            return False

        def is_blocked():
            blocked = False

            if (obj_board[Fn_row, Fn_col].identity > 0) and (obj_board[Fn_row, Fn_col].white == True):
                blocked = True

            return blocked

        if is_blocked() == True:  # checks for block
            piece.valid_move = False
            return piece.valid_move

        # if there is a piece diagnol to the paw, the pawn can take the piece
        if (abs(Fn_row - In_row) <= 1) and (abs(Fn_col - In_col) <= 1):

            piece.valid_move = True

            return piece.valid_move
        else:
            return piece.valid_move

    def valid_move_black(piece, obj_board, In_row, In_col, Fn_row, Fn_col):
        piece.valid_move = False

        if (Fn_row < 0 or Fn_row > 7 ) or (Fn_row < 0 or Fn_row > 7 ):
            return False

        def is_blocked():
            blocked = False

            if (obj_board[Fn_row, Fn_col].identity > 0) and (obj_board[Fn_row, Fn_col].white == False):
                blocked = True

            return blocked

        if is_blocked() == True:  # checks for block
            piece.valid_move = False
            return piece.valid_move

        # if there is a piece diagnol to the paw, the pawn can take the piece
        if (abs(Fn_row - In_row) <= 1) and (abs(Fn_col - In_col) <= 1):

            piece.valid_move = True

            return piece.valid_move
        else:

            return piece.valid_move


class Pawn:
    identity = 1
    firstmove = True
    stEval = 10


    def __init__(self, white, x, y):
        self.white = white
        if white == False:
            self.image = pygame.image.load("BlackPawn.png")
        else:
            self.image = pygame.image.load("WhitePawn.png")
        self.cord_x = x
        self.cord_y = y
        self.rect = pg.Rect(x, y, 80, 80)

    def valid_move_white(piece, obj_board, In_row, In_col, Fn_row, Fn_col):
        piece.valid_move = False

        if (Fn_row < 0 or Fn_row >= 8):
            piece.valid_move = False
            return piece.valid_move

        if (Fn_col < 0 or Fn_col >= 8):
            piece.valid_move = False
            return piece.valid_move

        def is_blocked():
            blocked = False

            if obj_board[Fn_row, Fn_col].identity > 0:
                blocked = True

            return blocked

        # if there is a piece diagnol to the paw, the pawn can take the piece
        if obj_board[Fn_row, Fn_col].identity > 0:
            if (Fn_row == In_row + 1) and ((Fn_col == In_col + 1) or (Fn_col == In_col - 1)) and (
                    obj_board[Fn_row, Fn_col].white == False):
                piece.valid_move = True
                return piece.valid_move


        # if piece is blocked automatically return false

        if is_blocked() == True:
            piece.valid_move = False
            return piece.valid_move

        if In_row > Fn_row:  # check if paw in moving backward
            return piece.valid_move

        elif Fn_col != In_col:
            return piece.valid_move

        else:
            if (piece.firstmove == True) and (Fn_row <= In_row + 2):
                piece.valid_move = True
                piece.firstmove = False

            elif (piece.firstmove == False) and (Fn_row == In_row + 1):
                piece.valid_move = True

            else:
                return piece.valid_move


        return piece.valid_move

    def valid_move_black(piece, obj_board, In_row, In_col, Fn_row, Fn_col):

        if (Fn_row < 0 or Fn_row >= 8):
            piece.valid_move = False
            return piece.valid_move

        if (Fn_col < 0 or Fn_col >= 8):
            piece.valid_move = False
            return piece.valid_move


        def is_blocked():
            blocked = False

            if obj_board[Fn_row, Fn_col].identity > 0:
                blocked = True
            return blocked





        if obj_board[Fn_row, Fn_col].identity > 0 and obj_board[Fn_row, Fn_col].white == True:

            if (Fn_row == In_row - 1) and ((Fn_col == In_col + 1) or (Fn_col == In_col - 1)) :
                piece.valid_move = True
                return piece.valid_move

        if is_blocked() == True:
            piece.valid_move = False
            return piece.valid_move



        # if piece is blocked automatically return false

        if In_row < Fn_row:  # check if paw in moving backward
            piece.valid_move = False
        elif Fn_col != In_col:
            piece.valid_move = False
        else:
            if (piece.firstmove == True) and (Fn_row <= In_row - 2):
                piece.valid_move = True
                piece.firstmove = False

            elif (Fn_row == In_row - 1):
                piece.valid_move = True

            else:
                return piece.valid_move

        return piece.valid_move


class space:

    identity = 0
    stEval = 0


    def __init__(self, x, y):
        self.cord_x = x
        self.cord_y = y
        self.rect = pg.Rect(x, y, 80, 80)

    def valid_move(piece, obj_board, In_row, In_col, Fn_row, Fn_col):
        piece.valid_move = False

        return piece.valid_move


class Rook:
    identity = 2
    leftRook = False
    stEval = 50


    def __init__(self, white, x, y):
        self.white = white
        if white == False:
            self.image = pygame.image.load("BlackRook.png")
        else:
            self.image = pygame.image.load("WhiteRook.png")
        self.cord_x = x
        self.cord_y = y
        self.rect = pg.Rect(x, y, 80, 80)

    def setLeftRook(self):
        self.leftRook = True

    def valid_move_white(piece, obj_board, In_row, In_col, Fn_row, Fn_col):

        if (Fn_row < 0 or Fn_row >= 8):
            print("Index out of bounds")
            piece.valid_move = False
            return piece.valid_move

        if (Fn_col < 0 or Fn_col >= 8):
            print("Index out of bounds")
            piece.valid_move = False
            return piece.valid_move

        vert_move = False
        horz_move = False
        piece.valid_move = False

        if ((Fn_row == In_row) and (Fn_col != In_col)):  # checks which way piece is moving
            horz_move = True


        elif ((Fn_row != In_row) and (Fn_col == In_col)):
            vert_move = True

        def is_blocked():
            blocked = False

            if obj_board[Fn_row][Fn_col].identity > 0:
                if obj_board[Fn_row][Fn_col].white == obj_board[In_row][In_col].white:
                    blocked = True
                    return blocked

            # horizontal movement algorithm
            if horz_move == True:
                if Fn_col > In_col:
                    ally = range(In_col + 1, Fn_col, 1)  # possible movement for piece
                elif Fn_col < In_col:
                    ally = range(In_col - 1, Fn_col, -1)  # possible movement for piece

                for index in ally:

                    if obj_board[In_row][index].identity > 0:
                        blocked = True

                # verticle move alg
            elif vert_move == True:

                if Fn_row > In_row:
                    ally = range(In_row + 1, Fn_row, 1)  # possible movement for piece
                elif Fn_row < In_row:
                    ally = range(In_row - 1, Fn_row, -1)  # possible movement for piece

                for index in ally:

                    if obj_board[index][In_col].identity > 0:
                        blocked = True

            return blocked

        if is_blocked() == True:  # checks for block
            piece.valid_move = False
            return piece.valid_move

        if (vert_move == True or horz_move == True) and (is_blocked() == False):
            piece.valid_move = True
        else:
            piece.valid_move = False

        return piece.valid_move

    def valid_move_black(piece, obj_board, In_row, In_col, Fn_row, Fn_col):

        if (Fn_row < 0 or Fn_row >= 8):
            print("Index out of bounds")
            piece.valid_move = False
            return piece.valid_move

        if (Fn_col < 0 or Fn_col >= 8):
            print("Index out of bounds")
            piece.valid_move = False
            return piece.valid_move

        vert_move = False
        horz_move = False
        piece.valid_move = False

        if ((Fn_row == In_row) and (Fn_col != In_col)):  # checks which way piece is moving
            horz_move = True


        elif ((Fn_row != In_row) and (Fn_col == In_col)):
            vert_move = True

        def is_blocked():
            blocked = False


            if obj_board[Fn_row][Fn_col].identity > 0:
                if obj_board[Fn_row][Fn_col].white == obj_board[In_row][In_col].white:
                    blocked = True
                    return blocked

            # horizontal movement algorithm
            if horz_move == True:
                if Fn_col > In_col:
                    ally = range(In_col + 1, Fn_col, 1)  # possible movement for piece
                elif Fn_col < In_col:
                    ally = range(In_col - 1, Fn_col, -1)  # possible movement for piece

                for index in ally:

                    if obj_board[In_row][index].identity > 0:
                        blocked = True

                # verticle move alg
            elif vert_move == True:

                if Fn_row > In_row:
                    ally = range(In_row + 1, Fn_row, 1)  # possible movement for piece
                elif Fn_row < In_row:
                    ally = range(In_row - 1, Fn_row, -1)  # possible movement for piece

                for index in ally:

                    if obj_board[index][In_col].identity > 0:
                        blocked = True

            return blocked

        if is_blocked() == True:  # checks for block
            piece.valid_move = False
            return piece.valid_move

        if (vert_move == True or horz_move == True) and (is_blocked() == False):
            piece.valid_move = True
        else:
            piece.valid_move = False
        return piece.valid_move


class Bishop:
    identity = 3
    stEval = 30


    def __init__(self, white, x, y):
        self.white = white
        if white == False:
            self.image = pygame.image.load("BlackBishop.png")
        else:
            self.image = pygame.image.load("WhiteBishop.png")
        self.cord_x = x
        self.cord_y = y
        self.rect = pg.Rect(x, y, 80, 80)

    def valid_move_white(piece, obj_board, In_row, In_col, Fn_row, Fn_col):

        if (Fn_row < 0 or Fn_row >= 8):
            print("reached")
            piece.valid_move = False
            return piece.valid_move

        if (Fn_col < 0 or Fn_col >= 8):
            print("reached")
            piece.valid_move = False
            return piece.valid_move

        diagnol = False
        left = False
        right = False
        up = False
        down = False

        piece.valid_move = False

        if (abs(Fn_col - In_col) == abs(Fn_row - In_row)):  # checks if piece is moving diagnol
            diagnol = True
        else:
            return piece.valid_move

        if (Fn_col > In_col):
            right = True
        else:
            left = True

        if (Fn_row > In_row):
            down = True
        else:
            up = True

        def is_blocked():
            blocked = False

            if obj_board[Fn_row][Fn_col].identity > 0:
                if obj_board[Fn_row][Fn_col].white == obj_board[In_row][In_col].white:
                    blocked = True
                    return blocked

            if (down == True) and (right == True):
                col_range = range(In_col + 1, Fn_col, 1)
                row_range = range(In_row + 1, Fn_row, 1)

            elif (down == True) and (left == True):
                col_range = range(In_col - 1, Fn_col, -1)
                row_range = range(In_row + 1, Fn_row, 1)

            elif (up == True) and (right == True):
                col_range = range(In_col + 1, Fn_col, 1)
                row_range = range(In_row - 1, Fn_row, -1)

            elif (up == True) and (left == True):
                col_range = range(In_col - 1, Fn_col, -1)
                row_range = range(In_row - 1, Fn_row, -1)

            x = 0
            for col_pos in col_range:
                row_pos = row_range[x]
                path = obj_board[row_pos][col_pos]

                if path.identity > 0:
                    blocked = True
                    return blocked
                x = x + 1

            return blocked

        if is_blocked() == True:  # checks for block
            piece.valid_move = False
            return piece.valid_move

        if (diagnol == True) and (is_blocked() == False):
            piece.valid_move = True

        return piece.valid_move

    def valid_move_black(piece, obj_board, In_row, In_col, Fn_row, Fn_col):

        if (Fn_row < 0 or Fn_row >= 8):
            print("index out of bounds")
            piece.valid_move = False
            return piece.valid_move

        if (Fn_col < 0 or Fn_col >= 8):
            print("index out of bounds")
            piece.valid_move = False
            return piece.valid_move

        diagnol = False
        left = False
        right = False
        up = False
        down = False

        piece.valid_move = False

        if (abs(Fn_col - In_col) == abs(Fn_row - In_row)):  # checks if piece is moving diagnol
            diagnol = True
        else:
            return piece.valid_move

        if (Fn_col > In_col):
            right = True
        else:
            left = True

        if (Fn_row > In_row):
            down = True
        else:
            up = True

        def is_blocked():
            blocked = False

            if obj_board[Fn_row][Fn_col].identity > 0:
                if obj_board[Fn_row][Fn_col].white == obj_board[In_row][In_col].white:
                    blocked = True
                    return blocked

            if (down == True) and (right == True):
                col_range = range(In_col + 1, Fn_col, 1)
                row_range = range(In_row + 1, Fn_row, 1)

            elif (down == True) and (left == True):
                col_range = range(In_col - 1, Fn_col, -1)
                row_range = range(In_row + 1, Fn_row, 1)

            elif (up == True) and (right == True):
                col_range = range(In_col + 1, Fn_col, 1)
                row_range = range(In_row - 1, Fn_row, -1)

            elif (up == True) and (left == True):
                col_range = range(In_col - 1, Fn_col, -1)
                row_range = range(In_row - 1, Fn_row, -1)

            x = 0
            for col_pos in col_range:
                row_pos = row_range[x]
                path = obj_board[row_pos][col_pos]

                if path.identity > 0:
                    blocked = True
                    return blocked
                x = x + 1

            return blocked

        if is_blocked() == True:  # checks for block
            piece.valid_move = False
            return piece.valid_move

        if (diagnol == True) and (is_blocked() == False):
            piece.valid_move = True

        return piece.valid_move


class Queen:

    identity = 5
    stEval = 90


    def __init__(self, white, x, y):
        self.white = white
        if white == False:
            self.image = pygame.image.load("BlackQueen.png")
        else:
            self.image = pygame.image.load("WhiteQueen.png")
        self.cord_x = x
        self.cord_y = y
        self.rect = pg.Rect(x, y, 80, 80)

    def valid_move_white(piece, obj_board, In_row, In_col, Fn_row, Fn_col):

        if (Fn_row < 0 or Fn_row >= 8):
            print("reached")
            piece.valid_move = False
            return piece.valid_move

        if (Fn_col < 0 or Fn_col >= 8):
            print("reached")
            piece.valid_move = False
            return piece.valid_move

        vert_move = False
        horz_move = False
        piece.valid_move = False
        rook_movement = False

        if ((Fn_row == In_row) and (Fn_col != In_col)):  # checks which way piece is moving
            horz_move = True
            rook_movement = True

        elif ((Fn_row != In_row) and (Fn_col == In_col)):
            vert_move = True
            rook_movement = True

        diagnol = False
        left = False
        right = False
        up = False
        down = False

        if ((Fn_row == In_row) and (Fn_col == In_col)):
            piece.valid_move = False
            return piece.valid_move



        if (abs(Fn_col - In_col) == abs(Fn_row - In_row)):  # checks if piece is moving diagnol
            diagnol = True

        if (Fn_col > In_col):
            right = True
        else:
            left = True

        if (Fn_row > In_row):
            down = True
        else:
            up = True



        def is_blocked():
            blocked = False

            if rook_movement == True:  # if queen acts as a rook

                if obj_board[Fn_row][Fn_col].identity > 0:
                    if obj_board[Fn_row][Fn_col].white == obj_board[In_row][In_col].white:
                        blocked = True
                        return blocked

                # horizontal movement algorithm
                if horz_move == True:
                    if Fn_col > In_col:
                        ally = range(In_col + 1, Fn_col, 1)  # possible movement for piece
                    elif Fn_col < In_col:
                        ally = range(In_col - 1, Fn_col, -1)  # possible movement for piece

                    for index in ally:

                        if obj_board[In_row][index].identity > 0:
                            blocked = True

                    # verticle move alg
                elif vert_move == True:

                    if Fn_row > In_row:
                        ally = range(In_row + 1, Fn_row, 1)  # possible movement for piece
                    elif Fn_row < In_row:
                        ally = range(In_row - 1, Fn_row, -1)  # possible movement for piece

                    for index in ally:

                        if obj_board[index][In_col].identity > 0:
                            blocked = True
            elif diagnol == True:  # if queen acts as a bishop

                if obj_board[Fn_row][Fn_col].identity > 0:
                    if obj_board[Fn_row][Fn_col].white == obj_board[In_row][In_col].white:
                        blocked = True
                        piece.valid_move = False
                        return piece.valid_move

                if (down == True) and (right == True):
                    col_range = range(In_col + 1, Fn_col, 1)
                    row_range = range(In_row + 1, Fn_row, 1)

                elif (down == True) and (left == True):
                    col_range = range(In_col - 1, Fn_col, -1)
                    row_range = range(In_row + 1, Fn_row, 1)

                elif (up == True) and (right == True):
                    col_range = range(In_col + 1, Fn_col, 1)
                    row_range = range(In_row - 1, Fn_row, -1)

                elif (up == True) and (left == True):
                    col_range = range(In_col - 1, Fn_col, -1)
                    row_range = range(In_row - 1, Fn_row, -1)

                x = 0
                for col_pos in col_range:
                    row_pos = row_range[x]
                    path = obj_board[row_pos][col_pos]

                    if path.identity > 0:
                        blocked = True
                        return blocked
                    x = x + 1

            return blocked

        if is_blocked() == True:  # checks for block
            piece.valid_move = False
            # rerun function
            return piece.valid_move




        if (rook_movement == True or diagnol == True) and (is_blocked() == False):
            piece.valid_move = True
        else:
            piece.valid_move = False

        return piece.valid_move

    def valid_move_black(piece, obj_board, In_row, In_col, Fn_row, Fn_col):

        if(obj_board[Fn_row][Fn_col].identity > 0):
            return False

        if (Fn_row < 0 or Fn_row >= 8):
            piece.valid_move = False
            return piece.valid_move

        if (Fn_col < 0 or Fn_col >= 8):
            piece.valid_move = False
            return piece.valid_move

        vert_move = False
        horz_move = False
        piece.valid_move = False
        rook_movement = False

        if ((Fn_row == In_row) and (Fn_col != In_col)):  # checks which way piece is moving
            horz_move = True
            rook_movement = True

        elif ((Fn_row != In_row) and (Fn_col == In_col)):
            vert_move = True
            rook_movement = True

        diagnol = False
        left = False
        right = False
        up = False
        down = False

        if ((Fn_row == In_row) and (Fn_col == In_col)):
            piece.valid_move = False
            return piece.valid_move

        if (abs(Fn_col - In_col) == abs(Fn_row - In_row)):  # checks if piece is moving diagnol
            diagnol = True

        if (Fn_col > In_col):
            right = True
        else:
            left = True

        if (Fn_row > In_row):
            down = True
        else:
            up = True

        def is_blocked():
            blocked = False

            if rook_movement == True:  # if queen acts as a rook

                if obj_board[Fn_row][Fn_col].identity > 0:
                    if obj_board[Fn_row][Fn_col].white == obj_board[In_row][In_col].white:
                        blocked = True
                        return blocked

                # horizontal movement algorithm
                if horz_move == True:
                    if Fn_col > In_col:
                        ally = range(In_col + 1, Fn_col, 1)  # possible movement for piece
                    elif Fn_col < In_col:
                        ally = range(In_col - 1, Fn_col, -1)  # possible movement for piece

                    for index in ally:

                        if obj_board[In_row][index].identity > 0:
                            blocked = True

                    # verticle move alg
                elif vert_move == True:

                    if Fn_row > In_row:
                        ally = range(In_row + 1, Fn_row, 1)  # possible movement for piece
                    elif Fn_row < In_row:
                        ally = range(In_row - 1, Fn_row, -1)  # possible movement for piece

                    for index in ally:

                        if obj_board[index][In_col].identity > 0:
                            blocked = True
            elif diagnol == True:  # if queen acts as a bishop

                if obj_board[Fn_row][Fn_col].identity > 0:
                    if obj_board[Fn_row][Fn_col].white == obj_board[In_row][In_col].white:
                        blocked = True
                        piece.valid_move = False
                        return piece.valid_move

                if (down == True) and (right == True):
                    col_range = range(In_col + 1, Fn_col, 1)
                    row_range = range(In_row + 1, Fn_row, 1)

                elif (down == True) and (left == True):
                    col_range = range(In_col - 1, Fn_col, -1)
                    row_range = range(In_row + 1, Fn_row, 1)

                elif (up == True) and (right == True):
                    col_range = range(In_col + 1, Fn_col, 1)
                    row_range = range(In_row - 1, Fn_row, -1)

                elif (up == True) and (left == True):
                    col_range = range(In_col - 1, Fn_col, -1)
                    row_range = range(In_row - 1, Fn_row, -1)

                x = 0
                for col_pos in col_range:
                    row_pos = row_range[x]
                    path = obj_board[row_pos][col_pos]

                    if path.identity > 0:
                        blocked = True
                        return blocked
                    x = x + 1

            return blocked

        if is_blocked() == True:  # checks for block
            piece.valid_move = False
            return piece.valid_move

        if (rook_movement == True or diagnol == True) and (is_blocked() == False):
            piece.valid_move = True
        else:

            piece.valid_move = False
        return piece.valid_move


class Knight:
    identity = 4
    stEval = 30


    def __init__(self, white, x, y):
        self.white = white
        if white == False:
            self.image = pygame.image.load("BlackKnight.png")
        else:
            self.image = pygame.image.load("WhiteKnight.png")
        self.cord_x = x
        self.cord_y = y
        self.rect = pg.Rect(x, y, 80, 80)

    def valid_move_white(piece, obj_board, In_row, In_col, Fn_row, Fn_col):

        if (Fn_row < 0 or Fn_row >= 8):
            piece.valid_move = False
            return piece.valid_move

        if (Fn_col < 0 or Fn_col >= 8):
            piece.valid_move = False
            return piece.valid_move

        piece.valid_move = False

        if (Fn_col == In_col + 1) and (Fn_row == In_row + 2):  # right up quad
            piece.valid_move = True
        elif (Fn_col == In_col + 2) and (Fn_row == In_row + 1):  # right up quad
            piece.valid_move = True
        elif (Fn_col == In_col - 1) and (Fn_row == In_row + 2):  # left up quad
            piece.valid_move = True
        elif (Fn_col == In_col - 2) and (Fn_row == In_row + 1):  # left up quad
            piece.valid_move = True
        elif (Fn_col == In_col - 1) and (Fn_row == In_row - 2):  # left down quad
            piece.valid_move = True
        elif (Fn_col == In_col - 2) and (Fn_row == In_row - 1):  # left down quad
            piece.valid_move = True
        elif (Fn_col == In_col + 2) and (Fn_row == In_row - 1):  # right down quad
            piece.valid_move = True
        elif (Fn_col == In_col + 1) and (Fn_row == In_row - 2):  # right down quad
            piece.valid_move = True
        else:
            piece.valid_move = False

        def is_blocked():
            blocked = False

            if (obj_board[Fn_row, Fn_col].identity > 0):
                if (obj_board[Fn_row, Fn_col].white == obj_board[In_row, In_col].white):
                    blocked = True

            return blocked

        if (is_blocked() == False) and piece.valid_move == True:
            pass
        else:
            piece.valid_move = False

        return piece.valid_move

    def valid_move_black(piece, obj_board, In_row, In_col, Fn_row, Fn_col):

        if (Fn_row < 0 or Fn_row >= 8):
            piece.valid_move = False
            return piece.valid_move

        if (Fn_col < 0 or Fn_col >= 8):
            piece.valid_move = False
            return piece.valid_move

        piece.valid_move = False

        if (Fn_col == In_col + 1) and (Fn_row == In_row + 2):  # right up quad
            piece.valid_move = True
        elif (Fn_col == In_col + 2) and (Fn_row == In_row + 1):  # right up quad
            piece.valid_move = True
        elif (Fn_col == In_col - 1) and (Fn_row == In_row + 2):  # left up quad
            piece.valid_move = True
        elif (Fn_col == In_col - 2) and (Fn_row == In_row + 1):  # left up quad
            piece.valid_move = True
        elif (Fn_col == In_col - 1) and (Fn_row == In_row - 2):  # left down quad
            piece.valid_move = True
        elif (Fn_col == In_col - 2) and (Fn_row == In_row - 1):  # left down quad
            piece.valid_move = True
        elif (Fn_col == In_col + 2) and (Fn_row == In_row - 1):  # right down quad
            piece.valid_move = True
        elif (Fn_col == In_col + 1) and (Fn_row == In_row - 2):  # right down quad
            piece.valid_move = True

        def is_blocked():
            blocked = False

            if (obj_board[Fn_row, Fn_col].identity > 0):
                if (obj_board[Fn_row, Fn_col].white == obj_board[In_row, In_col].white):
                    blocked = True

            return blocked

        if (is_blocked() == False) and piece.valid_move == True:
            pass
        else:
            piece.valid_move = False

        return piece.valid_move

def staticEval(obj_board):
    totalEval = 0
    In_row = 0
    In_col = 0
    for rows in obj_board:
        for tile in row:
            piece = object_board[In_row][In_col]
            totalEval += piece.stEval

        In_col = In_col + 1
    In_row = In_row + 1
    In_col = 0

    return totalEval

def min(a, b):
    if (a > b):
        return b
    else:
        return a

def max(a,b):
    if (a > b):
        return a
    else:
        return b

def playerWhiteMove(obj_board, cords, movement_array):
    valid_move = False

    In_row = movement_array[0]
    In_col = movement_array[1]

    Fn_row = movement_array[2]
    Fn_col = movement_array[3]

    piece = obj_board[In_row, In_col]



    if piece.identity > 0:
        if piece.white == True:  # check if correct player color has been chosen
            valid_move = piece.valid_move_white(obj_board, In_row, In_col, Fn_row, Fn_col)
    else:
        pass
    if valid_move == True:  # piece movement code
        empty = new_space(cords[In_row][In_col][0], cords[In_row][In_col][1])
        obj_board[Fn_row][Fn_col] = obj_board[In_row, In_col]

        # set new cords for moved piece
        piece = obj_board[Fn_row][Fn_col]
        piece.cord_x = cords[Fn_row][Fn_col][0]
        piece.cord_y = cords[Fn_row][Fn_col][1]
        piece.rect = pg.Rect(piece.cord_x, piece.cord_y, 80, 80)

        # fills old spot with space
        obj_board[In_row][In_col] = empty


    return obj_board


def playerBlackMove(obj_board, cords, movement_array):

    allMovesBlack = allValidMovesBlack(obj_board)

    print(f"Number of valid moves: {len(allMovesBlack)}")

    #time.sleep(2)

    rnd = random.randint(0, len(allMovesBlack) - 1)

    choiceMove = allMovesBlack[rnd]

    In_row = choiceMove.In_row
    In_col = choiceMove.In_col
    Fn_row = choiceMove.Fn_row
    Fn_col = choiceMove.Fn_col


    piece = obj_board[In_row, In_col]


    if len(allMovesBlack) > 0:  # piece movement code
        empty = new_space(cords[In_row][In_col][0], cords[In_row][In_col][1])
        obj_board[Fn_row][Fn_col] = obj_board[In_row, In_col]

        # set new cords for moved piece

        piece = obj_board[Fn_row][Fn_col]
        piece.cord_x = cords[Fn_row][Fn_col][0]
        piece.cord_y = cords[Fn_row][Fn_col][1]
        piece.rect = pg.Rect(piece.cord_x, piece.cord_y, 80, 80)

        # fills old spot with space
        obj_board = choiceMove.obj_board
        obj_board[In_row][In_col] = empty

    return obj_board


def innit_pieces(obj_board):
    for row in obj_board:
        for piece in row:
            if piece.identity > 0:
                screen.blit(piece.image, (piece.cord_x + 7, piece.cord_y + 7))

def alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col):
    # creates a deep copy for new object board

    newObj_board = np.empty((8,8), dtype= object)

    i = 0
    j = 0

    for row in obj_board:
        for tile in row:
            newObj_board[i][j] = obj_board[i][j]
            j = j + 1
        i = i + 1
        j = 0

    #moving the piece
    newObj_board[Fn_row][Fn_col] = newObj_board[In_row][In_col]
    newObj_board[In_row][In_col] = new_space(0, 0)
    return newObj_board


def game_loop(x, gameboard, cords, movement_array):
    global rookMoves
    global bishopMoves

    global leftLane
    global rightLane
    global topLane
    global bottomLane
    global pawnMoves

    if x % 2 == 1:
        print("White move")
        gameboard = playerWhiteMove(gameboard, cords, movement_array)
    else:
        print("Black move")

        gameboard = playerBlackMove(gameboard, cords, movement_array)
        print(f"Number of Pawn moves: {pawnMoves}")
        print(f"Number of Rook moves: {rookMoves}")
        print(f"Number of Bishop moves: {bishopMoves}")

        rookMoves = 0
        pawnMoves = 0

        leftLane = 0
        rightLane = 0
        topLane = 0
        bottomLane = 0

        bishopMoves = 0

    return gameboard


def allValidMovesBlack(obj_board):
    #function creates an array of object boards of all valid moves from this current board state

    global bishopMoves
    global rookMoves
    global leftLane
    global topLane
    global rightLane
    global bottomLane
    global pawnMoves

    allValidMoves = []


    In_row = 0
    In_col = 0
    Fn_row = 0
    Fn_col = 0

    for rows in obj_board:
        for tile in row:

            piece = object_board[In_row][In_col]

            if (piece.identity == 0 ):
                pass
            elif (piece.identity == 1 and piece.white == False):
                #pawn
                #not including first move ability for two squares yet

                Fn_row = In_row - 1;
                Fn_col = In_col
                # forawrd move check if valid

                if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)
                    pawnMoves += 1


                Fn_col = In_col - 1
                # diag move check if valid

                if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)
                    pawnMoves += 1

                Fn_col = In_col + 1
                # diag move check if valid

                if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)
                    pawnMoves += 1



                pass;
            elif (piece.identity == 2 and piece.white == False):
                # rook logic
                Fn_col = In_col + 1
                Fn_row = In_row
                while Fn_col <= 7: #moving right

                    if (piece.valid_move_black(object_board,In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row, Fn_col)
                        #creates a new node for this move
                        allValidMoves.append(newNode)
                        rookMoves = rookMoves + 1



                    else:
                        print(f"blocked at {Fn_row + 1}, {Fn_col + 1}")
                        print(f"There is a {obj_board[Fn_row][Fn_col].identity} piece in the blocked square")
                        break;
                    Fn_col = Fn_col + 1

                Fn_col = In_col - 1
                Fn_row = In_row

                while Fn_col >= 0: #moving left


                    if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)
                        rookMoves = rookMoves + 1


                    else:
                        print(f"blocked at {Fn_row + 1}, {Fn_col + 1}")
                        print(f"There is a {obj_board[Fn_row][Fn_col].identity} piece in the blocked square")
                        break;

                    Fn_col  = Fn_col - 1

                Fn_col = In_col
                Fn_row = In_row + 1
                while Fn_row <= 7: # moving down

                    if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)
                        rookMoves = rookMoves + 1


                    else:

                        print(f"blocked at {Fn_row + 1}, {Fn_col + 1}")
                        print(f"There is a {obj_board[Fn_row][Fn_col].identity} piece in the blocked square")
                        break;

                    Fn_row = Fn_row + 1

                Fn_col = In_col
                Fn_row = In_row - 1
                while Fn_row >= 0: #moving up


                    if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)
                        rookMoves = rookMoves + 1

                    else:
                        print(f"blocked at {Fn_row + 1}, {Fn_col + 1}")
                        print(f"There is a {obj_board[Fn_row][Fn_col].identity} piece in the blocked square")
                        break;

                    Fn_row = Fn_row - 1

            elif (piece.identity == 3 and piece.white == False):
                #logic for bishop

                Fn_col = In_col + 1
                Fn_row = In_row + 1

                while Fn_col <= 7 and Fn_row <= 7:
                #down right
                    if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)
                        bishopMoves = bishopMoves + 1
                    elif (In_col != Fn_col & In_row != Fn_row):
                        break;

                    Fn_col = Fn_col + 1
                    Fn_row = Fn_row + 1

                Fn_col = In_col + 1
                Fn_row = In_row - 1
                while Fn_col <= 7 and Fn_row >= 0:
                #up right
                    if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)
                        bishopMoves = bishopMoves + 1

                    elif (In_col != Fn_col & In_row != Fn_row):
                        break;

                    Fn_col = Fn_col + 1
                    Fn_row = Fn_row - 1

                Fn_col = In_col - 1
                Fn_row = In_row - 1
                while Fn_col >= 0 and Fn_row >= 0:
                    # up left
                    if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)
                        bishopMoves = bishopMoves + 1

                    elif (In_col != Fn_col & In_row != Fn_row):
                        break;

                    Fn_col = Fn_col - 1
                    Fn_row = Fn_row - 1

                Fn_col = In_col - 1
                Fn_row = In_row + 1
                while Fn_col >= 0 and Fn_row <= 7:
                    # down left
                    if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)
                        bishopMoves = bishopMoves + 1

                    elif (In_col != Fn_col & In_row != Fn_row):
                        break;

                    Fn_col = Fn_col - 1
                    Fn_row = Fn_row + 1

            elif (piece.identity == 4 and piece.white == False ):
                #knight logic

                #right up quad
                Fn_col = In_col + 1
                Fn_row = In_row + 2

                if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)

                # right up quad
                Fn_col = In_col + 2
                Fn_row = In_row + 1

                if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)


                # left up quad
                Fn_col = In_col - 1
                Fn_row = In_row + 2

                if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)


                # left up quad
                Fn_col = In_col - 2
                Fn_row = In_row + 1

                if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)


                # left down quad
                Fn_col = In_col - 2
                Fn_row = In_row - 1

                if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)


                # left down quad
                Fn_col = In_col - 2
                Fn_row = In_row - 1

                if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)


                # right down quad
                Fn_col = In_col + 1
                Fn_row = In_row - 2

                if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)


                # right down quad
                Fn_col = In_col + 2
                Fn_row = In_row - 1

                if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)





                pass
            elif (piece.identity == 5 and piece.white == False):
                #queen logic
                # logic for bishop

                Fn_col = In_col + 1
                Fn_row = In_row + 1

                while Fn_col <= 7 and Fn_row <= 7:
                    # down right
                    if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)
                    elif (In_col != Fn_col & In_row != Fn_row):
                        break;

                    Fn_col = Fn_col + 1
                    Fn_row = Fn_row + 1

                Fn_col = In_col + 1
                Fn_row = In_row - 1
                while Fn_col <= 7 and Fn_row >= 0:
                    # up right
                    if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)

                    elif (In_col != Fn_col & In_row != Fn_row):
                        break;

                    Fn_col = Fn_col + 1
                    Fn_row = Fn_row - 1

                Fn_col = In_col - 1
                Fn_row = In_row - 1
                while Fn_col >= 0 and Fn_row >= 0:
                    # up left
                    if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)

                    elif (In_col != Fn_col & In_row != Fn_row):
                        break;

                    Fn_col = Fn_col - 1
                    Fn_row = Fn_row - 1

                Fn_col = In_col - 1
                Fn_row = In_row + 1
                while Fn_col >= 0 and Fn_row <= 7:
                    # down left
                    if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)

                    elif (In_col != Fn_col & In_row != Fn_row):
                        break;

                    Fn_col = Fn_col - 1
                    Fn_row = Fn_row + 1

                # rook logic for queen
                Fn_col = In_col + 1
                Fn_row = In_row
                while Fn_col <= 7:  # moving right

                    if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)



                    else:
                        print(f"blocked at {Fn_row + 1}, {Fn_col + 1}")
                        print(f"There is a {obj_board[Fn_row][Fn_col].identity} piece in the blocked square")
                        break;
                    Fn_col = Fn_col + 1

                Fn_col = In_col - 1
                Fn_row = In_row

                while Fn_col >= 0:  # moving left

                    if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)


                    else:
                        print(f"blocked at {Fn_row + 1}, {Fn_col + 1}")
                        print(f"There is a {obj_board[Fn_row][Fn_col].identity} piece in the blocked square")
                        break;

                    Fn_col = Fn_col - 1

                Fn_col = In_col
                Fn_row = In_row + 1
                while Fn_row <= 7:  # moving down

                    if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)


                    else:

                        print(f"blocked at {Fn_row + 1}, {Fn_col + 1}")
                        print(f"There is a {obj_board[Fn_row][Fn_col].identity} piece in the blocked square")
                        break;

                    Fn_row = Fn_row + 1

                Fn_col = In_col
                Fn_row = In_row - 1
                while Fn_row >= 0:  # moving up

                    if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)

                    else:
                        print(f"blocked at {Fn_row + 1}, {Fn_col + 1}")
                        print(f"There is a {obj_board[Fn_row][Fn_col].identity} piece in the blocked square")
                        break;

                    Fn_row = Fn_row - 1



            elif (piece.identity == 6 and piece.white == False):
                #king logic

                #upper row
                Fn_col = In_col
                Fn_row = In_row + 1

                if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)

                Fn_col = In_col + 1
                Fn_row = In_row + 1

                if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)

                Fn_col = In_col - 1
                Fn_row = In_row + 1

                if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)

                #mid row
                Fn_col = In_col + 1
                Fn_row = In_row

                if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)

                Fn_col = In_col - 1
                Fn_row = In_row

                if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)

                #bottom row

                Fn_col = In_col
                Fn_row = In_row - 1

                if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)

                Fn_col = In_col + 1
                Fn_row = In_row - 1

                if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)

                Fn_col = In_col - 1
                Fn_row = In_row - 1

                if (piece.valid_move_black(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)






            In_col = In_col + 1
        In_row = In_row + 1
        In_col = 0

    return allValidMoves



def allValidMovesWhite(obj_board):
    #function creates an array of object boards of all valid moves from this current board state


    allValidMoves = []


    In_row = 0
    In_col = 0
    Fn_row = 0
    Fn_col = 0

    for rows in obj_board:
        for tile in row:

            piece = object_board[In_row][In_col]

            if (piece.identity == 0 ):
                pass
            elif (piece.identity == 1 and piece.white == True):
                #pawn
                #not including first move ability for two squares yet

                Fn_row = In_row - 1;
                Fn_col = In_col
                # forawrd move check if valid

                if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)
                    pawnMoves += 1


                Fn_col = In_col - 1
                # diag move check if valid

                if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)
                    pawnMoves += 1

                Fn_col = In_col + 1
                # diag move check if valid

                if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)
                    pawnMoves += 1



                pass;
            elif (piece.identity == 2 and piece.white == True):
                # rook logic
                Fn_col = In_col + 1
                Fn_row = In_row
                while Fn_col <= 7: #moving right

                    if (piece.valid_move_white(object_board,In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row, Fn_col)
                        #creates a new node for this move
                        allValidMoves.append(newNode)
                        rookMoves = rookMoves + 1



                    else:
                        break;
                    Fn_col = Fn_col + 1

                Fn_col = In_col - 1
                Fn_row = In_row

                while Fn_col >= 0: #moving left


                    if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)
                        rookMoves = rookMoves + 1


                    else:
                        break;

                    Fn_col  = Fn_col - 1

                Fn_col = In_col
                Fn_row = In_row + 1
                while Fn_row <= 7: # moving down

                    if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)
                        rookMoves = rookMoves + 1


                    else:

                        print(f"blocked at {Fn_row + 1}, {Fn_col + 1}")
                        print(f"There is a {obj_board[Fn_row][Fn_col].identity} piece in the blocked square")
                        break;

                    Fn_row = Fn_row + 1

                Fn_col = In_col
                Fn_row = In_row - 1
                while Fn_row >= 0: #moving up


                    if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)
                        rookMoves = rookMoves + 1

                    else:
                        print(f"blocked at {Fn_row + 1}, {Fn_col + 1}")
                        print(f"There is a {obj_board[Fn_row][Fn_col].identity} piece in the blocked square")
                        break;

                    Fn_row = Fn_row - 1

            elif (piece.identity == 3 and piece.white == True):
                #logic for bishop

                Fn_col = In_col + 1
                Fn_row = In_row + 1

                while Fn_col <= 7 and Fn_row <= 7:
                #down right
                    if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)
                        bishopMoves = bishopMoves + 1
                    elif (In_col != Fn_col & In_row != Fn_row):
                        break;

                    Fn_col = Fn_col + 1
                    Fn_row = Fn_row + 1

                Fn_col = In_col + 1
                Fn_row = In_row - 1
                while Fn_col <= 7 and Fn_row >= 0:
                #up right
                    if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)
                        bishopMoves = bishopMoves + 1

                    elif (In_col != Fn_col & In_row != Fn_row):
                        break;

                    Fn_col = Fn_col + 1
                    Fn_row = Fn_row - 1

                Fn_col = In_col - 1
                Fn_row = In_row - 1
                while Fn_col >= 0 and Fn_row >= 0:
                    # up left
                    if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)
                        bishopMoves = bishopMoves + 1

                    elif (In_col != Fn_col & In_row != Fn_row):
                        break;

                    Fn_col = Fn_col - 1
                    Fn_row = Fn_row - 1

                Fn_col = In_col - 1
                Fn_row = In_row + 1
                while Fn_col >= 0 and Fn_row <= 7:
                    # down left
                    if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)
                        bishopMoves = bishopMoves + 1

                    elif (In_col != Fn_col & In_row != Fn_row):
                        break;

                    Fn_col = Fn_col - 1
                    Fn_row = Fn_row + 1

            elif (piece.identity == 4 and piece.white == True ):
                #knight logic

                #right up quad
                Fn_col = In_col + 1
                Fn_row = In_row + 2

                if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)

                # right up quad
                Fn_col = In_col + 2
                Fn_row = In_row + 1

                if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)


                # left up quad
                Fn_col = In_col - 1
                Fn_row = In_row + 2

                if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)


                # left up quad
                Fn_col = In_col - 2
                Fn_row = In_row + 1

                if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)


                # left down quad
                Fn_col = In_col - 2
                Fn_row = In_row - 1

                if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)


                # left down quad
                Fn_col = In_col - 2
                Fn_row = In_row - 1

                if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)


                # right down quad
                Fn_col = In_col + 1
                Fn_row = In_row - 2

                if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)


                # right down quad
                Fn_col = In_col + 2
                Fn_row = In_row - 1

                if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)





                pass
            elif (piece.identity == 5 and piece.white == True):
                #queen logic
                # logic for bishop

                Fn_col = In_col + 1
                Fn_row = In_row + 1

                while Fn_col <= 7 and Fn_row <= 7:
                    # down right
                    if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)
                    elif (In_col != Fn_col & In_row != Fn_row):
                        break;

                    Fn_col = Fn_col + 1
                    Fn_row = Fn_row + 1

                Fn_col = In_col + 1
                Fn_row = In_row - 1
                while Fn_col <= 7 and Fn_row >= 0:
                    # up right
                    if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)

                    elif (In_col != Fn_col & In_row != Fn_row):
                        break;

                    Fn_col = Fn_col + 1
                    Fn_row = Fn_row - 1

                Fn_col = In_col - 1
                Fn_row = In_row - 1
                while Fn_col >= 0 and Fn_row >= 0:
                    # up left
                    if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)

                    elif (In_col != Fn_col & In_row != Fn_row):
                        break;

                    Fn_col = Fn_col - 1
                    Fn_row = Fn_row - 1

                Fn_col = In_col - 1
                Fn_row = In_row + 1
                while Fn_col >= 0 and Fn_row <= 7:
                    # down left
                    if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)

                    elif (In_col != Fn_col & In_row != Fn_row):
                        break;

                    Fn_col = Fn_col - 1
                    Fn_row = Fn_row + 1

                # rook logic for queen
                Fn_col = In_col + 1
                Fn_row = In_row
                while Fn_col <= 7:  # moving right

                    if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)



                    else:
                        print(f"blocked at {Fn_row + 1}, {Fn_col + 1}")
                        print(f"There is a {obj_board[Fn_row][Fn_col].identity} piece in the blocked square")
                        break;
                    Fn_col = Fn_col + 1

                Fn_col = In_col - 1
                Fn_row = In_row

                while Fn_col >= 0:  # moving left

                    if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)


                    else:
                        print(f"blocked at {Fn_row + 1}, {Fn_col + 1}")
                        print(f"There is a {obj_board[Fn_row][Fn_col].identity} piece in the blocked square")
                        break;

                    Fn_col = Fn_col - 1

                Fn_col = In_col
                Fn_row = In_row + 1
                while Fn_row <= 7:  # moving down

                    if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)


                    else:

                        print(f"blocked at {Fn_row + 1}, {Fn_col + 1}")
                        print(f"There is a {obj_board[Fn_row][Fn_col].identity} piece in the blocked square")
                        break;

                    Fn_row = Fn_row + 1

                Fn_col = In_col
                Fn_row = In_row - 1
                while Fn_row >= 0:  # moving up

                    if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):

                        newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                       Fn_col)
                        # creates a new node for this move
                        allValidMoves.append(newNode)

                    else:
                        print(f"blocked at {Fn_row + 1}, {Fn_col + 1}")
                        print(f"There is a {obj_board[Fn_row][Fn_col].identity} piece in the blocked square")
                        break;

                    Fn_row = Fn_row - 1



            elif (piece.identity == 6 and piece.white == False):
                #king logic

                #upper row
                Fn_col = In_col
                Fn_row = In_row + 1

                if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)

                Fn_col = In_col + 1
                Fn_row = In_row + 1

                if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)

                Fn_col = In_col - 1
                Fn_row = In_row + 1

                if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)

                #mid row
                Fn_col = In_col + 1
                Fn_row = In_row

                if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)

                Fn_col = In_col - 1
                Fn_row = In_row

                if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)

                #bottom row

                Fn_col = In_col
                Fn_row = In_row - 1

                if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)

                Fn_col = In_col + 1
                Fn_row = In_row - 1

                if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)

                Fn_col = In_col - 1
                Fn_row = In_row - 1

                if (piece.valid_move_white(object_board, In_row, In_col, Fn_row, Fn_col) == True):
                    newNode = Node(alterObjBoard(obj_board, In_row, In_col, Fn_row, Fn_col), In_row, In_col, Fn_row,
                                   Fn_col)
                    # creates a new node for this move
                    allValidMoves.append(newNode)






            In_col = In_col + 1
        In_row = In_row + 1
        In_col = 0

    return allValidMoves

def minimax(obj_board, depth, player):
    #player should start as black
    #blacks true or false value is false


    if(player == True):
        maxEval = (math.inf * -1)
        allValidMovesWhite(obj_board)









Run_window = True
pg.init()

# Screen Innitalization
size = width, height = 700, 700
screen = pg.display.set_mode(size)
pygame.display.set_caption("CHESS")
icon = pg.image.load("chess-pawn.png")
pg.display.set_icon(icon)
BG_Color = (255, 255, 255)
FPS = 60
clock = pg.time.Clock()

board_length = range(1, 9)

# gameboard graphics
tile1 = (64, 43, 24)
tile2 = (219, 189, 162)
# pg.draw_rect(screen, tile1, pg.Rect(30,30,50,50))


cord_system = np.zeros((8, 8, 2))

i = 0
j = 0

# important game board dims
x = 40
y = 40
space_dim = 80

for row in cord_system:
    for col in row:
        cord_system[i][j][0] = x
        cord_system[i][j][1] = y
        j = j + 1
        x = x + space_dim

    i = i + 1
    j = 0
    y = y + space_dim
    x = 40

    # innitalize objects

WhitePawn1 = Pawn(True, cord_system[1][0][0], cord_system[1][0][1])
WhitePawn2 = Pawn(True, cord_system[1][1][0], cord_system[1][1][1])
WhitePawn3 = Pawn(True, cord_system[1][2][0], cord_system[1][2][1])
WhitePawn4 = Pawn(True, cord_system[1][3][0], cord_system[1][3][1])
WhitePawn5 = Pawn(True, cord_system[1][4][0], cord_system[1][4][1])
WhitePawn6 = Pawn(True, cord_system[1][5][0], cord_system[1][5][1])
WhitePawn7 = Pawn(True, cord_system[1][6][0], cord_system[1][6][1])
WhitePawn8 = Pawn(True, cord_system[1][7][0], cord_system[1][7][1])

WhiteRook1 = Rook(True, cord_system[0][0][0], cord_system[0][0][1])
WhiteKnight1 = Knight(True, cord_system[0][1][0], cord_system[0][1][1])
WhiteBishop1 = Bishop(True, cord_system[0][2][0], cord_system[0][2][1])
WhiteKing = King(True, cord_system[0][3][0], cord_system[0][3][1])
WhiteQueen = Queen(True, cord_system[0][4][0], cord_system[0][4][1])
WhiteBishop2 = Bishop(True, cord_system[0][5][0], cord_system[0][5][1])
WhiteKnight2 = Knight(True, cord_system[0][6][0], cord_system[0][6][1])
WhiteRook2 = Rook(True, cord_system[0][7][0], cord_system[0][7][1])

BlackPawn1 = Pawn(False, cord_system[6][0][0], cord_system[6][0][1])
BlackPawn2 = Pawn(False, cord_system[6][1][0], cord_system[6][1][1])
BlackPawn3 = Pawn(False, cord_system[6][2][0], cord_system[6][2][1])
BlackPawn4 = Pawn(False, cord_system[6][3][0], cord_system[6][3][1])
BlackPawn5 = Pawn(False, cord_system[6][4][0], cord_system[6][4][1])
BlackPawn6 = Pawn(False, cord_system[6][5][0], cord_system[6][5][1])
BlackPawn7 = Pawn(False, cord_system[6][6][0], cord_system[6][6][1])
BlackPawn8 = Pawn(False, cord_system[6][7][0], cord_system[6][7][1])

BlackRook1 = Rook(False, cord_system[7][0][0], cord_system[7][0][1])
BlackKnight1 = Knight(False, cord_system[7][1][0], cord_system[7][1][1])
BlackBishop1 = Bishop(False, cord_system[7][2][0], cord_system[7][2][1])
BlackQueen = Queen(False, cord_system[7][4][0], cord_system[7][4][1])
BlackKing = King(False, cord_system[7][3][0], cord_system[7][3][1])
BlackBishop2 = Bishop(False, cord_system[7][5][0], cord_system[7][5][1])
BlackKnight2 = Knight(False, cord_system[7][6][0], cord_system[7][6][1])
BlackRook2 = Rook(False, cord_system[7][7][0], cord_system[7][7][1])

BlackRook1.setLeftRook()

space_counter_row = 0
space_counter_col = 0

space_board = np.zeros((4, 8), dtype=object)

while space_counter_row < 4:
    while space_counter_col < 8:
        x = cord_system[space_counter_row + 2][space_counter_col][0]
        y = cord_system[space_counter_row + 2][space_counter_col][1]
        space_board[space_counter_row][space_counter_col] = space(x, y)

        space_counter_col = space_counter_col + 1
    space_counter_row = space_counter_row + 1
    space_counter_col = 0

object_board = np.array(
    [[WhiteRook1, WhiteKnight1, WhiteBishop1, WhiteKing, WhiteQueen, WhiteBishop2, WhiteKnight2, WhiteRook2],
     [WhitePawn1, WhitePawn2, WhitePawn3, WhitePawn4, WhitePawn5, WhitePawn6, WhitePawn7, WhitePawn8],
     space_board[0],
     space_board[1],
     space_board[2],
     space_board[3],
     [BlackPawn1, BlackPawn2, BlackPawn3, BlackPawn4, BlackPawn5, BlackPawn6, BlackPawn7, BlackPawn8],
     [BlackRook1, BlackKnight1, BlackBishop1, BlackKing, BlackQueen, BlackBishop2, BlackKnight2, BlackRook2]])

# game Loop starts as whites turn
counter = 1

# must innitalize outside the game loop to track the times the movement has been clicked
movement_array = []
piece_clicked = False

win = False
kings = 0


while Run_window == True:
    clock.tick(FPS)
    for event in pg.event.get():  # loop for quitting consol
        if event.type == pg.QUIT:
            Run_window = False

        inp_row = 0
        inp_col = 0  # innitalize row and col input
        if event.type == pg.MOUSEBUTTONDOWN:  # clicking pieces
            for row in object_board:
                for piece in row:
                    if piece.rect.collidepoint(pygame.mouse.get_pos()):
                        movement_array.append(inp_row)
                        movement_array.append(inp_col)
                        piece_clicked = True
                    inp_col = inp_col + 1
                inp_row = inp_row + 1
                inp_col = 0

    screen.fill(BG_Color)  # starts the window as white
    x = 40
    y = 40
    space_dim = 80
    for row in board_length:
        for space in board_length:
            if row % 2 == 0:
                space = space + 1
            if space % 2 == 0:
                pg.draw.rect(screen, tile1, pg.Rect((x, y, space_dim, space_dim)))
            else:
                pg.draw.rect(screen, tile2, pg.Rect(x, y, space_dim, space_dim))

            x = x + space_dim
        y = y + space_dim
        x = 40

    if piece_clicked == True: #shows user what they click
            pg.draw.rect(screen, (246,255,120), pg.Rect(cord_system[movement_array[-2]][movement_array[-1]][0],cord_system[movement_array[-2]][movement_array[-1]][1] , space_dim, space_dim))

    innit_pieces(object_board)
    pg.display.update()




    if len(movement_array) == 4 or (counter%2 == 0):
        same_board = True
        piece_clicked = False


        old_num_object_board = np.zeros((8,8))

        i = 0
        j = 0
        for row in object_board: # creates a number matrix refrence for old board
            for el in row:
                old_num_object_board[i, j] = el.identity

                j = j + 1
            i = i + 1
            j = 0



        new_num_object_board = np.zeros((8, 8))

        object_board = game_loop(counter, object_board, cord_system, movement_array)
        movement_array = []

        i = 0
        j = 0
        for row in object_board: # creates a number matrix refrence for new board
            for el in row:
                new_num_object_board[i, j] = el.identity
                #print(f"|{el.identity}|", end = "")

                j = j + 1
            i = i + 1
            j = 0


        i = 0
        j = 0
        for row in object_board: # creates a number matrix refrence for new board
            for el in row:
                if new_num_object_board[i, j] != old_num_object_board[i,j]:
                    same_board = False

                j = j + 1
            i = i + 1
            j = 0

        if same_board == True:
            pass
        else:
            clock.tick(10)
            innit_pieces(object_board)
            counter = counter + 1
            pg.display.update()

    if win == True:
        print("win")
        Run_window = False





