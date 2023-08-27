import pygame as pg
import pygame.display
import numpy as np

class Pawn():
    def __init__(self, x, y):
        self.image = pygame.image.load("BlackPawn.png")
        self.cord_x = x
        self.cord_y = y
        self.rect = pg.Rect(x,y,80,80)

def draw_pieces(piece):

    screen.blit(piece.image, (piece.cord_x +7, piece.cord_y+7))
    pg.draw.rect(screen, (255, 0, 0), piece.rect, 2)






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

    #innitalize pawn objects
BlackPawn1 = Pawn(40,40)
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





print(cord_system)

    #game Loop
while Run_window == True:
    clock.tick(FPS)
    for event in pg.event.get(): #loop for quitting consol
        if event.type == pg.QUIT:
            Run_window = False

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

    draw_pieces(BlackPawn1)


    pg.display.flip()


