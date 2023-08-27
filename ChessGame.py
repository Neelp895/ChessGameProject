import numpy as np
import pygame as pg
import pygame.display


class new_space:
    identity = 0
    def __init__(self, x, y):
        self.cord_x = x
        self.cord_y = y
        self.rect = pg.Rect(x,y,80,80)

    def valid_move(piece, obj_board, In_row, In_col, Fn_row, Fn_col):
        piece.valid_move = False

        return piece.valid_move


class King:
    identity = 6

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

        def is_blocked():
            blocked = False

            if (obj_board[Fn_row, Fn_col].identity > 0) and (obj_board[Fn_row, Fn_col].white == True):
                blocked = True
                print("Piece is Blocked")

            return blocked

        if is_blocked() == True:  # checks for block
            piece.valid_move = False
            return piece.valid_move

        # if there is a piece diagnol to the paw, the pawn can take the piece
        if (abs(Fn_row - In_row) <= 1) and (abs(Fn_col - In_col) <= 1):

            piece.valid_move = True

            return piece.valid_move
        else:
            print("Invalid Move")

        return piece.valid_move

    def valid_move_black(piece, obj_board, In_row, In_col, Fn_row, Fn_col):
        piece.valid_move = False

        def is_blocked():
            blocked = False

            if (obj_board[Fn_row, Fn_col].identity > 0) and (obj_board[Fn_row, Fn_col].black == True):
                blocked = True
                print("Piece is Blocked")

            return blocked

        if is_blocked() == True:  # checks for block
            piece.valid_move = False
            return piece.valid_move

        # if there is a piece diagnol to the paw, the pawn can take the piece
        if (abs(Fn_row - In_row) <= 1) and (abs(Fn_col - In_col) <= 1):

            piece.valid_move = True

            return piece.valid_move
        else:
            print("Invalid Move")
        return piece.valid_move


class Pawn:
    identity = 1
    firstmove = True

    def __init__(self, white, x, y):
        self.white = white
        if white == False:
            self.image = pygame.image.load("BlackPawn.png")
        else:
            self.image = pygame.image.load("WhitePawn.png")
        self.cord_x = x
        self.cord_y = y
        self.rect = pg.Rect(x,y,80,80)

    def valid_move_white(piece, obj_board, In_row, In_col, Fn_row, Fn_col):
        piece.valid_move = False

        def is_blocked():
            blocked = False

            if obj_board[Fn_row, Fn_col].identity > 0:
                blocked = True
                print("Piece is Blocked")

            return blocked

        # if there is a piece diagnol to the paw, the pawn can take the piece
        if (Fn_row == In_row + 1) and ((Fn_col == In_col + 1) or (Fn_col == In_col - 1)) and (
                obj_board[Fn_row, Fn_col].white == False):
            piece.valid_move = True
            return piece.valid_move

        # if piece is blocked automatically return false

        if is_blocked() == True:
            piece.valid_move = False
            print("Piece blocked")
            return piece.valid_move

        print("Line 109 reeached")

        if In_row > Fn_row:  # check if paw in moving backward
            print("Invalid Move: Cannot Move Backwards")
            return piece.valid_move

        elif Fn_col != In_col:
            print("Invalid Move: Pawn Cannot Move that Way")
            return piece.valid_move

        else:
            if (piece.firstmove == True) and (Fn_row <= In_row + 2):
                piece.valid_move = True
                piece.firstmove = False

            elif (piece.firstmove == False) and (Fn_row == In_row + 1):
                piece.valid_move = True

            else:
                print("Invalid Move: Piece moved too far!")
                return piece.valid_move

        print("Line 130 reeached")
        print(piece.valid_move)

        return piece.valid_move

    def valid_move_black(piece, obj_board, In_row, In_col, Fn_row, Fn_col):
        def is_blocked():
            blocked = False

            if obj_board[Fn_row, Fn_col].identity > 0:
                blocked = True
                print("Piece is Blocked")

            return blocked

        # if there is a piece diagnol to the paw, the pawn can take the piece
        if (Fn_row == In_row - 1) and ((Fn_col == In_col + 1) or (Fn_col == In_col - 1)) and (
                obj_board[Fn_row, Fn_col].white == True):
            piece.valid_move = True

            return piece.valid_move

        # if piece is blocked automatically return false

        if is_blocked() == True:
            piece.valid_move = False
            return piece.valid_move

        if In_row < Fn_row:  # check if paw in moving backward
            print("Invalid Move: Cannot Move Backwards")
            return piece.valid_move
        elif Fn_col != In_col:
            print("Invalid Move: Pawn Cannot Move that Way")
            return piece.valid_move
        else:
            print("Condition Reached")
            print(Fn_row)
            print(In_row - 1)
            print(piece.firstmove)
            if (piece.firstmove == True) and (Fn_row <= In_row - 2):
                piece.valid_move = True
                piece.firstmove = False

            elif (Fn_row == In_row - 1):
                piece.valid_move = True

            else:
                print("Invalid Move: Piece moved too far!")
                return piece.valid_move

        return piece.valid_move


class space:
    identity = 0

    def __init__(self, x, y):
        self.cord_x = x
        self.cord_y = y
        self.rect = pg.Rect(x,y,80,80)

    def valid_move(piece, obj_board, In_row, In_col, Fn_row, Fn_col):
        piece.valid_move = False

        return piece.valid_move


class Rook:
    identity = 2

    def __init__(self, white, x, y):
        self.white = white
        if white == False:
            self.image = pygame.image.load("BlackRook.png")
        else:
            self.image = pygame.image.load("WhiteRook.png")
        self.cord_x = x
        self.cord_y = y
        self.rect = pg.Rect(x,y,80,80)


    def valid_move_white(piece, obj_board, In_row, In_col, Fn_row, Fn_col):

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
            print("Path is blocked")
            return piece.valid_move

        if (vert_move == True or horz_move == True) and (is_blocked() == False):
            piece.valid_move = True
        else:
            print("Invalid Move")
            piece.valid_move = False

        return piece.valid_move

    def valid_move_black(piece, obj_board, In_row, In_col, Fn_row, Fn_col):

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
            print("Path is blocked")
            return piece.valid_move

        if (vert_move == True or horz_move == True) and (is_blocked() == False):
            piece.valid_move = True
        else:
            print("Invalid Move")
            piece.valid_move = False
        return piece.valid_move


class Bishop:
    identity = 3

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
                    print("Invalid Move")
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
                    print("path blocked")
                    blocked = True
                    return blocked
                x = x + 1

            return blocked

        if is_blocked() == True:  # checks for block
            piece.valid_move = False
            print("Path is blocked")
            return piece.valid_move

        if (diagnol == True) and (is_blocked() == False):
            piece.valid_move = True
        else:
            print("Invalid Move")
        return piece.valid_move

    def valid_move_black(piece, obj_board, In_row, In_col, Fn_row, Fn_col):

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
                    print("Invalid Move")
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
                    print("path blocked")
                    blocked = True
                    return blocked
                x = x + 1

            return blocked

        if is_blocked() == True:  # checks for block
            piece.valid_move = False
            print("Path is blocked")
            return piece.valid_move

        if (diagnol == True) and (is_blocked() == False):
            piece.valid_move = True
        else:
            print("Invalid Move")
        return piece.valid_move


class Queen:
    identity = 5

    def __init__(self, white, x, y):
        self.white = white
        if white == False:
            self.image = pygame.image.load("BlackQueen.png")
        else:
            self.image = pygame.image.load("WhiteQueen.png")
        self.cord_x = x
        self.cord_y = y
        self.rect = pg.Rect(x,y,80,80)


    def valid_move_white(piece, obj_board, In_row, In_col, Fn_row, Fn_col):

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
                        print("Invalid Move: Error 1")
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
                        print("path blocked")
                        blocked = True
                        return blocked
                    x = x + 1

            return blocked

        if is_blocked() == True:  # checks for block
            piece.valid_move = False
            print("Path is blocked")
            # rerun function
            return piece.valid_move

        if (rook_movement == True or diagnol == True) and (is_blocked() == False):
            piece.valid_move = True
        else:
            print("Invalid Move: Error 2")
            piece.valid_move = False

        return piece.valid_move

    def valid_move_black(piece, obj_board, In_row, In_col, Fn_row, Fn_col):

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
                        print("Invalid Move: Error 1")
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
                        print("path blocked")
                        blocked = True
                        return blocked
                    x = x + 1

            return blocked

        if is_blocked() == True:  # checks for block
            piece.valid_move = False
            print("Path is blocked")
            return piece.valid_move

        if (rook_movement == True or diagnol == True) and (is_blocked() == False):
            piece.valid_move = True
        else:

            print("Invalid Move: Error 2")
            piece.valid_move = False
        return piece.valid_move


class Knight:
    identity = 4

    def __init__(self, white, x, y):
        self.white = white
        if white == False:
            self.image = pygame.image.load("BlackKnight.png")
        else:
            self.image = pygame.image.load("WhiteKnight.png")
        self.cord_x = x
        self.cord_y = y
        self.rect = pg.Rect(x,y,80,80)


    def valid_move_white(piece, obj_board, In_row, In_col, Fn_row, Fn_col):

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
                    print("Piece is Blocked")

            return blocked

        if (is_blocked() == False) and piece.valid_move == True:
            pass
        else:
            piece.valid_move = False

        return piece.valid_move

    def valid_move_black(piece, obj_board, In_row, In_col, Fn_row, Fn_col):

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
                    print("Piece is Blocked")

            return blocked

        if (is_blocked() == False) and piece.valid_move == True:
            pass
        else:
            piece.valid_move = False

        return piece.valid_move


def playerWhiteMove(obj_board, cords):
    valid_move = False
    valid_start = False
    valid_end = False

    while valid_start == False:

        In_col = int(input("Enter start col: "))
        In_row = int(input("Enter start row: "))

        if (In_col > 0 and In_col < 9) and (In_row > 0 and In_row < 9):
            valid_start = True
        else:
            print('Error not a valid Space: Error 1')

    In_row = In_row - 1
    In_col = In_col - 1

    while valid_end == False:


        Fn_col = int(input("Enter end col: "))
        Fn_row = int(input("Enter end row: "))
        if (Fn_col > 0 and Fn_col < 9) and (Fn_row > 0 and Fn_row < 9):
            valid_end = True
        else:
            print('Error not a valid Space: Error 2')



    Fn_row = Fn_row - 1
    Fn_col = Fn_col - 1
    # take the inputs of the starting pos and the final pos

    piece = obj_board[In_row, In_col]

    if piece.identity == 0:
        playerWhiteMove(obj_board)


    if piece.identity > 0:
        if piece.white == True:  # check if correct player color has been chosen
            valid_move = piece.valid_move_white(obj_board, In_row, In_col, Fn_row, Fn_col)
    else:
        print("Wrong Piece")
        playerWhiteMove(obj_board)


    if valid_move == True:  # piece movement code
        empty = new_space(cords[In_row][In_col][0],cords[In_row][In_col][1])
        obj_board[Fn_row][Fn_col] = obj_board[In_row, In_col]

        #set new cords for moved piece

        piece = obj_board[Fn_row][Fn_col]
        piece.cord_x = cords[Fn_row][Fn_col][0]
        piece.cord_y = cords[Fn_row][Fn_col][1]
        piece.rect = pg.Rect(piece.cord_x, piece.cord_y, 80, 80)


        #fills old spot with space
        obj_board[In_row][In_col] = empty

    else:
        print("error invalid move")
        playerWhiteMove(obj_board, cords)

    return obj_board


def playerBlackMove(obj_board, cords):
    valid_move = False
    valid_start = False
    valid_end = False

    while valid_start == False:

        In_col = int(input("Enter start col: "))
        In_row = int(input("Enter start row: "))

        if (In_col > 0 and In_col < 9) and (In_row > 0 and In_row < 9):
            valid_start = True
        else:
            print('Error not a valid Space')

    In_row = In_row - 1
    In_col = In_col - 1

    while valid_end == False:

        Fn_col = int(input("Enter end col: "))
        Fn_row = int(input("Enter end row: "))
        if (Fn_col > 0 and Fn_col < 9) and (Fn_row > 0 and Fn_row < 9):
            valid_end = True
        else:
            print('Error not a valid Space')

    Fn_row = Fn_row - 1
    Fn_col = Fn_col - 1
    # take the inputs of the starting pos and the final pos

    piece = obj_board[In_row, In_col]

    if piece.identity == 0:
        print("Error No Piece Selected")
        playerBlackMove(obj_board, cords)

    if piece.white == False:  # check if correct player color has been chosen

        valid_move = piece.valid_move_black(obj_board, In_row, In_col, Fn_row, Fn_col)
    else:
        print("Wrong Piece")
        playerBlackMove(obj_board, cords)
    if valid_move == True:  # piece movement code

        empty = new_space()
        obj_board[Fn_row][Fn_col] = obj_board[In_row, In_col]

        # set new cords for moved piece

        piece = obj_board[Fn_row][Fn_col]
        piece.cord_x = cords[Fn_row][Fn_col][0]
        piece.cord_y = cords[Fn_row][Fn_col][1]
        piece.rect = pg.Rect(piece.cord_x, piece.cord_y, 80, 80)

        # fills old spot with space
        obj_board[In_row][In_col] = empty

    else:
        print("Invalid Move")
        playerBlackMove(obj_board, cords)

    return obj_board



def innit_pieces(obj_board):

    for row in obj_board:
        for piece in row:
            if piece.identity > 0:
                screen.blit(piece.image, (piece.cord_x +7, piece.cord_y+7))
                pg.draw.rect(screen, (255, 0, 0), piece.rect, 2)
            else:
                pg.draw.rect(screen, (0, 255, 0), piece.rect, 2)


def game_loop(x, gameboard, cords):

    if x%2 == 1:
        gameboard = playerWhiteMove(gameboard, cords)
    else:
        gameboard = playerBlackMove(gameboard, cords)
    return gameboard

Run_window = True
pg.init()

#Screen Innitalization
size = width, height = 700, 700
screen = pg.display.set_mode(size)
pygame.display.set_caption("CHESS")
icon = pg.image.load("chess-pawn.png")
pg.display.set_icon(icon)
BG_Color = (255,255,255)
FPS = 60
clock = pg.time.Clock()

board_length = range(1,9)

    #gameboard graphics
tile1 = (64, 43, 24)
tile2 = (219, 189, 162)
    #pg.draw_rect(screen, tile1, pg.Rect(30,30,50,50))


cord_system = np.zeros((8,8,2))

i = 0
j = 0

#important game board dims
x = 40
y = 40
space_dim = 80


for row in cord_system:
    for col in row:
        cord_system[i][j][0] = x
        cord_system[i][j][1] = y
        j = j+1
        x = x + space_dim

    i = i+1
    j = 0
    y = y + space_dim
    x = 40

    #innitalize objects


WhitePawn1 = Pawn(True, cord_system[1][0][0],cord_system[1][0][1])
WhitePawn2 = Pawn(True, cord_system[1][1][0],cord_system[1][1][1])
WhitePawn3 = Pawn(True, cord_system[1][2][0],cord_system[1][2][1])
WhitePawn4 = Pawn(True, cord_system[1][3][0],cord_system[1][3][1])
WhitePawn5 = Pawn(True, cord_system[1][4][0],cord_system[1][4][1])
WhitePawn6 = Pawn(True, cord_system[1][5][0],cord_system[1][5][1])
WhitePawn7 = Pawn(True, cord_system[1][6][0],cord_system[1][6][1])
WhitePawn8 = Pawn(True, cord_system[1][7][0],cord_system[1][7][1])

WhiteRook1 = Rook(True, cord_system[0][0][0],cord_system[0][0][1])
WhiteKnight1 = Knight(True, cord_system[0][1][0],cord_system[0][1][1])
WhiteBishop1 = Bishop(True, cord_system[0][2][0],cord_system[0][2][1])
WhiteQueen = Queen(True, cord_system[0][4][0],cord_system[0][4][1])
WhiteKing = King(True, cord_system[0][3][0],cord_system[0][3][1])
WhiteBishop2 = Bishop(True, cord_system[0][5][0],cord_system[0][5][1])
WhiteKnight2 = Knight(True, cord_system[0][6][0],cord_system[0][6][1])
WhiteRook2 = Rook(True, cord_system[0][7][0],cord_system[0][7][1])


BlackPawn1 = Pawn(False, cord_system[6][0][0],cord_system[6][0][1])
BlackPawn2 = Pawn(False, cord_system[6][1][0],cord_system[6][1][1])
BlackPawn3 = Pawn(False, cord_system[6][2][0],cord_system[6][2][1])
BlackPawn4 = Pawn(False, cord_system[6][3][0],cord_system[6][3][1])
BlackPawn5 = Pawn(False, cord_system[6][4][0],cord_system[6][4][1])
BlackPawn6 = Pawn(False, cord_system[6][5][0],cord_system[6][5][1])
BlackPawn7 = Pawn(False, cord_system[6][6][0],cord_system[6][6][1])
BlackPawn8 = Pawn(False, cord_system[6][7][0],cord_system[6][7][1])

BlackRook1 = Rook(False, cord_system[7][0][0],cord_system[7][0][1])
BlackKnight1 = Knight(False, cord_system[7][1][0],cord_system[7][1][1])
BlackBishop1 = Bishop(False, cord_system[7][2][0],cord_system[7][2][1])
BlackQueen = Queen(False, cord_system[7][4][0],cord_system[7][4][1])
BlackKing = King(False, cord_system[7][3][0],cord_system[7][3][1])
BlackBishop2 = Bishop(False, cord_system[7][5][0],cord_system[7][5][1])
BlackKnight2 = Knight(False, cord_system[7][6][0],cord_system[7][6][1])
BlackRook2 = Rook(False, cord_system[7][7][0],cord_system[7][7][1])

space_counter_row = 0
space_counter_col = 0

space_board = np.zeros((4,8), dtype= object)

while space_counter_row < 4:
    while space_counter_col < 8:

        x = cord_system[space_counter_row+2][space_counter_col][0]
        y = cord_system[space_counter_row+2][space_counter_col][1]
        space_board[space_counter_row][space_counter_col] = space(x,y)

        space_counter_col = space_counter_col +1
    space_counter_row = space_counter_row +1
    space_counter_col = 0



object_board = np.array([[WhiteRook1, WhiteKnight1, WhiteBishop1, WhiteQueen, WhiteKing, WhiteBishop2, WhiteKnight2, WhiteRook2],
                             [WhitePawn1, WhitePawn2, WhitePawn3, WhitePawn4, WhitePawn5, WhitePawn6, WhitePawn7, WhitePawn8],
                             space_board[0],
                             space_board[1],
                             space_board[2],
                             space_board[3],
                             [BlackPawn1, BlackPawn2, BlackPawn3, BlackPawn4, BlackPawn5, BlackPawn6, BlackPawn7, BlackPawn8],
                             [BlackRook1, BlackKnight1, BlackBishop1, BlackKing, BlackQueen, BlackBishop2, BlackKnight2, BlackRook2]])


#game Loop
counter = 1

#must innitalize outside the game loop to track the times the movement has been clicked
movement_array = []

while Run_window == True:
    clock.tick(FPS)
    for event in pg.event.get(): #loop for quitting consol
        if event.type == pg.QUIT:
            Run_window = False

        inp_row = 0
        inp_col = 0 #innitalize row and col input
        if event.type == pg.MOUSEBUTTONDOWN: #clicking pieces
            for row in object_board:
                for piece in row:
                    if piece.rect.collidepoint(pygame.mouse.get_pos()):
                        print("initial input recorded")
                        movement_array.append(inp_row)
                        movement_array.append(inp_col)
                    inp_col = inp_col + 1
                inp_row = inp_row + 1
                inp_col = 0
    screen.fill(BG_Color)  # starts the window as white
    x = 40
    y = 40
    space_dim = 80
    for row in board_length:
        for space in board_length:
            if row%2 == 0:
                space = space + 1
            if space%2 == 0:
                pg.draw.rect(screen, tile1, pg.Rect((x, y, space_dim, space_dim)))
            else:
                pg.draw.rect(screen, tile2, pg.Rect(x, y, space_dim, space_dim))

            x = x + space_dim
        y = y + space_dim
        x = 40

    innit_pieces(object_board)
    pg.display.update()
    if len(movement_array) == 4:
        print("run function")
        movement_array = []
    #calls for the white players move
        #object_board = game_loop(counter, object_board, cord_system, movement_array)
        #innit_pieces(object_board)
        #pg.display.update()
        #counter = counter +1




