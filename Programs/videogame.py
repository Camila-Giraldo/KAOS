import pygame
import sys
import os
from config import IMAGES_PATH

images_path = IMAGES_PATH

# Inicialización de Pygame
pygame.init()

# Configuración de pantalla y constantes
WIDTH, HEIGHT = 700, 700
CELL_SIZE = 225
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe!")

# Carga de imágenes
BOARD = pygame.image.load(os.path.join(images_path, "board.png"))
X_IMG = pygame.image.load(os.path.join(images_path, "x.png"))
O_IMG = pygame.image.load(os.path.join(images_path, "o.png"))
WIN_IMG = {"X": pygame.image.load(os.path.join(images_path, "Winning X.png")),
           "O": pygame.image.load(os.path.join(images_path, "Winning O.png"))}

BG_COLOR = (214, 201, 227)

# Inicialización del tablero lógico y gráfico
board = [[None for _ in range(3)] for _ in range(3)]
to_move = 'X'

def draw_board():
    """Dibujar el tablero inicial"""
    SCREEN.fill(BG_COLOR)
    SCREEN.blit(BOARD, (64, 64))
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                SCREEN.blit(X_IMG, X_IMG.get_rect(center=(j * CELL_SIZE + 130, i * CELL_SIZE + 130)))
            elif board[i][j] == 'O':
                SCREEN.blit(O_IMG, O_IMG.get_rect(center=(j * CELL_SIZE + 130, i * CELL_SIZE + 130)))
    pygame.display.update()

def handle_move(x, y):
    """Agregar movimiento en el tablero"""
    global to_move
    col, row = x // CELL_SIZE, y // CELL_SIZE
    if board[row][col] is None:  # Celda vacía
        board[row][col] = to_move
        to_move = 'O' if to_move == 'X' else 'X'
        draw_board()

def check_winner():
    """Verifica el ganador"""
    for line in board + list(zip(*board)):
        if line[0] == line[1] == line[2] and line[0] is not None:
            return line[0]

    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]

    if all(cell is not None for row in board for cell in row):
        return "DRAW"
    return None

def display_winner(winner):
    """Mostrar el ganador"""
    if winner in WIN_IMG:
        SCREEN.blit(WIN_IMG[winner], WIN_IMG[winner].get_rect(center=(WIDTH // 2, HEIGHT // 2)))
    elif winner == "DRAW":
        font = pygame.font.Font(None, 80)
        text = font.render("¡Draw!", True, (255, 0, 0))
        SCREEN.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
    pygame.display.update()
    pygame.time.delay(2000)

# Reiniciar juego
def reset_game():
    global board, to_move
    board = [[None for _ in range(3)] for _ in range(3)]
    to_move = 'X'
    draw_board()

# Ciclo principal
draw_board()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not check_winner():
            handle_move(*event.pos)
            winner = check_winner()
            if winner:
                display_winner(winner)
                reset_game()
