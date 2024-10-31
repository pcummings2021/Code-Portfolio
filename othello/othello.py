
import pygame
import numpy as np

class OthelloAI:
    def __init__(self, player_color, max_depth):
        self.player_color = player_color
        self.opponent_color = 3 - player_color
        self.max_depth = max_depth
        
    def best_move(self, board):
        _, move = self.minimax_ab(board, self.max_depth, -np.inf, np.inf, False)  # Get best move
        return move  # Return the move (row, col)


    def minimax_ab(self, node, depth, alpha, beta, max_player):
        if depth == 0 or self.is_terminal_state(node):
            return self.eval_board(node), None  # Return score and no move (None)

        best_move = None  # To track the best move (row, col)

        if max_player:
            value = -np.inf
            for child_board, move in self.gen_move_tree(node):  # Also return the move from gen_move_tree
                child_value, _ = self.minimax_ab(child_board, depth - 1, alpha, beta, False)
                if child_value > value:
                    value = child_value
                    best_move = move  # Store the best move (row, col)
                if value >= beta:
                    break  # Beta pruning
                alpha = max(alpha, value)
            return value, best_move  # Return best score and the best move
        else:
            value = np.inf
            for child_board, move in self.gen_move_tree(node):  # Also return the move from gen_move_tree
                child_value, _ = self.minimax_ab(child_board, depth - 1, alpha, beta, True)
                if child_value < value:
                    value = child_value
                    best_move = move  # Store the best move (row, col)
                if value <= alpha:
                    break  # Alpha pruning
                beta = min(beta, value)
            return value, best_move  # Return best score and the best move


    def eval_board(self, board):
        ai = 0
        opp = 0
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] == self.player_color:
                    ai += 1
                elif board[row][col] == 3 - self.player_color:
                    opp += 1
        return ai - opp


    def gen_move_tree(self, board):
        move_tree = []
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if is_valid_move(board, row, col, self.player_color):
                    new_board = simulate_place_piece(board, row, col, self.player_color)
                    if new_board is not None:
                        move_tree.append((new_board, (row, col)))
        return move_tree

    def is_terminal_state(self, board):
        return not (has_valid_move(board, 1) or has_valid_move(board, 2))

ai_color = int(input('What color should the AI play? (1 == Black or 2 == White): '))
max_depth = int(input('Max Tree Depth? Input: '))
game_AI = OthelloAI(ai_color, max_depth)

# Initialize Pygame
pygame.init()

# Constants
BOARD_SIZE = 8
SQUARE_SIZE = 80
WINDOW_SIZE = BOARD_SIZE * SQUARE_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1),(-1, 1), (1, -1), (-1, -1)]
CORNERS = [(0, 0), (0, BOARD_SIZE-1), (BOARD_SIZE-1, 0), (BOARD_SIZE-1, BOARD_SIZE-1)]

# Create window
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Othello")

# Initialize board
# 0: Empty, 1: Black, 2: White
board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)

# Starting pieces
board[3][3], board[4][4] = 2, 2  # White
board[3][4], board[4][3] = 1, 1  # Black

def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            pygame.draw.rect(window, GREEN, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.rect(window, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
            if board[row][col] == 1:
                pygame.draw.circle(window, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), SQUARE_SIZE//2 - 5)
            elif board[row][col] == 2:
                pygame.draw.circle(window, WHITE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), SQUARE_SIZE//2 - 5)

def is_valid_move(board, row, col, player):
    if board[row][col] != 0:
        return False
    
    opponent = 3 - current_player
    valid = False

    for direction in DIRECTIONS:
        r_off, c_off = direction
        r, c = row + r_off, col + c_off
        found_opponent = False

        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
            if board[r][c] == opponent:
                found_opponent = True
            elif board[r][c] == player and found_opponent:
                valid = True
                break
            else:
                break
            r += r_off
            c += c_off

    return valid


        
def place_piece(board, row, col, player):
    is_valid = is_valid_move(board, row, col, player)
    if not is_valid:
        return False   
    board[row][col] = player
    opponent = 3 - player
    for direction in DIRECTIONS:
        r_off, c_off = direction
        r, c = row + r_off, col + c_off
        flip = []
        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
            if board[r][c] == opponent:
                flip.append((r, c))
            elif board[r][c] == player:
                for r_flip, c_flip in flip:
                    if (r_flip, c_flip) not in CORNERS:
                        board[r_flip][c_flip] = player
                break
            else:
                break
            r += r_off
            c += c_off
    return True

def simulate_place_piece(board, row, col, player):
    new_board = np.copy(board)
    is_valid = is_valid_move(new_board, row, col, player)
    if not is_valid:
        return None
    
    new_board[row][col] = player
    opponent = 3 - player
    for direction in DIRECTIONS:
        r_off, c_off = direction
        r, c = row + r_off, col + c_off
        flip = []
        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
            if new_board[r][c] == opponent:
                flip.append((r, c))
            elif new_board[r][c] == player:
                for r_flip, c_flip in flip:
                    if (r_flip, c_flip) not in CORNERS:
                        new_board[r_flip][c_flip] = player
                break
            else:
                break
            r += r_off
            c += c_off
    return new_board

def count_board(board):
    black, white = 0, 0
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 1:
                black += 1
            elif board[row][col] == 2:
                white += 1
    print('GAME OVER\nBlack: %d\nWhite: %d' % (black, white))
    if black > white:
        print('WINNER: BLACK')
    else:
        print('WINNER: WHITE')
        
def has_valid_move(board, player):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if is_valid_move(board, row, col, player):
                return True
    return False

def check_game_over(board):
    if not has_valid_move(board, 1) and not has_valid_move(board, 2):
        return True
    return False

# Game loop
running = True
current_player = 1  # Black starts
while running:
    if check_game_over(board):
        count_board(board)
        break
    else: 
        for event in pygame.event.get():
            print('Current Player:', 'black' if current_player==1 else 'white', end="\r")
            if event.type == pygame.QUIT:
                running = False

            if current_player != game_AI.player_color:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
                    if place_piece(board, row, col, current_player):
                        current_player = 3 - current_player  # Switch between 1 (Black) and 2 (White)
            else: 
                try:
                    row, col = game_AI.best_move(board)
                except:
                    print(current_player)
                    print(board)

                if place_piece(board, row, col, current_player):
                    current_player = 3 - current_player
                

    # Draw board and pieces
    draw_board()
    pygame.display.update()

pygame.quit()
