import pygame
import sys

pygame.init()

WIDTH = 300
HEIGHT = 300
CELL_SIZE = 100
FPS = 60

win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Farben
WHITE = (255, 255, 255)
BEIGE = (200, 150, 20)

# Spielvariablen
board = [['', '', ''], ['', '', ''], ['', '', '']]
current_player = 'X'
game_over = False

# Lade eigene Bilder
cross_img = pygame.image.load('cross.png')
circle_img = pygame.image.load('circle.png')

cross_img = pygame.transform.scale(cross_img, (CELL_SIZE, CELL_SIZE))
circle_img = pygame.transform.scale(circle_img, (CELL_SIZE, CELL_SIZE))

def draw_board():
    win.fill(BEIGE)
    for i in range(1, 3):
        pygame.draw.line(win, (0, 0, 0), (CELL_SIZE * i, 0), (CELL_SIZE * i, HEIGHT), 5)
        pygame.draw.line(win, (0, 0, 0), (0, CELL_SIZE * i), (WIDTH, CELL_SIZE * i), 5)

    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                win.blit(cross_img, (col * CELL_SIZE, row * CELL_SIZE))
            elif board[row][col] == 'O':
                win.blit(circle_img, (col * CELL_SIZE, row * CELL_SIZE))

def check_winner():
    # Überprüfe Reihen
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return board[row][0]

    # Überprüfe Spalten
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]

    # Überprüfe Diagonalen
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]

    return None

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked_row = mouseY // CELL_SIZE
            clicked_col = mouseX // CELL_SIZE

            if board[clicked_row][clicked_col] == '':
                board[clicked_row][clicked_col] = current_player
                winner = check_winner()

                if winner:
                    print(f'Spieler {winner} hat gewonnen!')
                    game_over = True
                elif all(board[row][col] != '' for row in range(3) for col in range(3)):
                    print('Unentschieden!')
                    game_over = True
                else:
                    current_player = 'O' if current_player == 'X' else 'X'

    draw_board()
    pygame.display.update()
    clock.tick(FPS)
