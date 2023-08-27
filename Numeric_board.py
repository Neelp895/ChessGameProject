import numpy as np
import pygame as pg
import pygame.display

class King:
    identity = 6

    def __init__(initials, white):
        initials.white = white

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
            playerWhiteMove(obj_board)
            return piece.valid_move

        # if there is a piece diagnol to the paw, the pawn can take the piece
        if (abs(Fn_row - In_row) <= 1) and (abs(Fn_col - In_col) <= 1):

            piece.valid_move = True

            return piece.valid_move
        else:
            print("Invalid Move")
            playerWhiteMove(obj_board)

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
            playerWhiteMove(obj_board)
            return piece.valid_move

        # if there is a piece diagnol to the paw, the pawn can take the piece
        if (abs(Fn_row - In_row) <= 1) and (abs(Fn_col - In_col) <= 1):

            piece.valid_move = True

            return piece.valid_move
        else:
            print("Invalid Move")
            playerWhiteMove(obj_board)

        return piece.valid_move


class Pawn:
    identity = 1
    firstmove = True

    def __init__(self, white, x, y):
        self.white = white
        self.image = pygame.image.load("BlackPawn.png")
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

    def valid_move(piece, obj_board, In_row, In_col, Fn_row, Fn_col):
        piece.valid_move = False

        return piece.valid_move


class Rook:
    identity = 2

    def __init__(initials, white):
        initials.white = white

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

    def __init__(initials, white):
        initials.white = white

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
                    playerWhiteMove(obj_board)

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
            playerWhiteMove(obj_board)  # rerun function
            return piece.valid_move

        if (diagnol == True) and (is_blocked() == False):
            piece.valid_move = True
        else:
            print("Invalid Move")
            playerWhiteMove(obj_board)
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
                    playerBlackMove(obj_board)

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
            playerBlackMove(obj_board)  # rerun function
            return piece.valid_move

        if (diagnol == True) and (is_blocked() == False):
            piece.valid_move = True
        else:
            print("Invalid Move")
            playerBlackMove(obj_board)
        return piece.valid_move


class Queen:
    identity = 5

    def __init__(initials, white):
        initials.white = white

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
            print(rook_movement)
            print(diagnol)
            print(is_blocked())
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

    def __init__(initials, white):
        initials.white = white

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


def playerWhiteMove(obj_board):
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
        print("Error No Piece Selected: Error 1")
        playerWhiteMove(obj_board)

    print(piece.identity)
    print(piece.white)
    if piece.identity > 0:
        if piece.white == True:  # check if correct player color has been chosen
            valid_move = piece.valid_move_white(obj_board, In_row, In_col, Fn_row, Fn_col)
    else:
        print("Wrong Piece")
        playerWhiteMove(obj_board)

    print("line 826 reached")
    print(valid_move)

    if valid_move == True:  # piece movement code
        empty = space()
        obj_board[Fn_row, Fn_col] = obj_board[In_row, In_col]
        obj_board[In_row, In_col] = empty

    else:
        print("error invalid move")
        playerWhiteMove(obj_board)

    return obj_board


def playerBlackMove(obj_board):
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
        playerWhiteMove(obj_board)

    if piece.white == False:  # check if correct player color has been chosen

        valid_move = piece.valid_move_black(obj_board, In_row, In_col, Fn_row, Fn_col)
    else:
        print("Wrong Piece")
        playerBlackMove(obj_board)
    if valid_move == True:  # piece movement code

        empty = space()
        obj_board[Fn_row, Fn_col] = obj_board[In_row, In_col]

        obj_board[In_row, In_col] = empty
    else:
        print("Invalid Move")
        playerWhiteMove(obj_board)

    return obj_board


def Game_Run():
    win = False

    row = np.array([0, 1, 2, 3, 4, 5, 6, 7])
    empty = space()
    p1 = Pawn(True)
    p2 = Pawn(True)
    p3 = Pawn(True)
    p4 = Pawn(True)
    p5 = Pawn(True)
    p6 = Pawn(True)
    p7 = Pawn(True)
    p8 = Pawn(True)

    p9 = Pawn(False)
    p10 = Pawn(False)
    p11 = Pawn(False)
    p12 = Pawn(False)
    p13 = Pawn(False)
    p14 = Pawn(False)
    p15 = Pawn(False)
    p16 = Pawn(False)

    testP1 = Pawn(True)
    testP2 = Pawn(False)

    WhiteKing = King(True)
    BlackKing = King(False)

    WhiteRook1 = Rook(True)
    BlackRook1 = Rook(False)

    WhiteBishop1 = Bishop(True)
    BlackBishop1 = Bishop(False)

    WhiteQueen = Queen(True)
    BlackQueen = Queen(False)

    WhiteKnight1 = Knight(True)

    object_board = np.array([[WhiteRook1, empty, empty, WhiteKing, empty, WhiteKnight1, empty, empty],
                             [p1, p2, p3, p4, p5, p6, p7, p8],
                             [empty, WhiteQueen, empty, empty, WhiteBishop1, empty, empty, empty],
                             [empty, empty, empty, empty, empty, empty, empty, empty],
                             [empty, empty, empty, empty, empty, empty, empty, empty],
                             [empty, empty, BlackQueen, empty, empty, empty, empty, empty],
                             [p9, p10, p11, p12, p13, p14, p15, p16],
                             [empty, empty, empty, empty, BlackKing, empty, empty, empty]])

    game_board = np.zeros((8, 8), dtype=int)
    x = 0
    j = 0
    for row in object_board:
        for el in row:
            game_board[j, x] = el.identity

            x = x + 1
        j = j + 1
        x = 0

    while win == False:

        print("  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
        print("-----------------------------------")
        c = 1
        for row in game_board:
            print(c, end=" | ")
            for el in row:
                print(el, end=' | ')

            print("-----------------------------------")
            c = c + 1

        print("Whites Move")
        object_board = playerWhiteMove(object_board)

        # update game board
        x = 0
        j = 0
        for row in object_board:
            for el in row:
                game_board[j, x] = el.identity

                x = x + 1
            j = j + 1
            x = 0

        # prints game board

        print("  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
        print("-----------------------------------")
        c = 1
        for row in game_board:
            print(c, end=" | ")
            for el in row:
                print(el, end=' | ')

            print("-----------------------------------")
            c = c + 1

        print("Black's Move")

        object_board = playerBlackMove(object_board)

        # update game board
        x = 0
        j = 0
        for row in object_board:
            for el in row:
                game_board[j, x] = el.identity

                x = x + 1
            j = j + 1
            x = 0







