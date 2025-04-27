import pygame
from config import *

class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]

    def draw_lines(self, screen):
        pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), 15)
        pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), 15)
        pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), 15)
        pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), 15)

    def draw_figures(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == 'O':
                    pygame.draw.circle(screen, CIRCLE_COLOR,
                                       (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2),
                                       CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif self.board[row][col] == 'X':
                    start_desc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
                    end_desc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                    pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)

                    start_asc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                    end_asc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
                    pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)

    def player_move(self, x, y, player):
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False

    def make_move(self, move, player):
        row, col = move
        self.board[row][col] = player

    def undo_move(self, move):
        row, col = move
        self.board[row][col] = ' '

    def available_moves(self):
        moves = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == ' ':
                    moves.append((row, col))
        return moves

    def is_draw(self):
        return all(all(cell != ' ' for cell in row) for row in self.board)

    def check_winner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        for col in range(COLS):
            if all(self.board[row][col] == player for row in range(ROWS)):
                return True
        if all(self.board[i][i] == player for i in range(ROWS)):
            return True
        if all(self.board[i][ROWS - 1 - i] == player for i in range(ROWS)):
            return True
        return False
