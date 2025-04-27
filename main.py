# main.py

import pygame
import sys
import time
from config import *
from board import Board
from aiplayer import AIPlayer

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT + 60))
pygame.display.set_caption('Tic Tac Toe AI')

board = Board()
ai_player = 'X'
human_player = 'O'
use_alpha_beta = True
current_algorithm = 'AlphaBeta'
game_over = False
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

def draw_buttons():
    toggle_rect = pygame.Rect(10, HEIGHT + 10, 200, 40)
    pygame.draw.rect(screen, (0, 200, 200), toggle_rect)
    toggle_text = font.render('Toggle (T)', True, (0, 0, 0))
    screen.blit(toggle_text, (20, HEIGHT + 20))

    restart_rect = pygame.Rect(220, HEIGHT + 10, 150, 40)
    pygame.draw.rect(screen, (0, 200, 0), restart_rect)
    restart_text = font.render('Restart (R)', True, (0, 0, 0))
    screen.blit(restart_text, (230, HEIGHT + 20))

    return toggle_rect, restart_rect

def restart_game():
    global board, ai, game_over
    board = Board()
    ai = AIPlayer(board, ai_player, human_player, use_alpha_beta=(current_algorithm == 'AlphaBeta'))
    game_over = False
    print("Game restarted!")

def toggle_algorithm():
    global use_alpha_beta, current_algorithm, ai
    use_alpha_beta = not use_alpha_beta
    current_algorithm = 'AlphaBeta' if use_alpha_beta else 'Minimax'
    ai.use_alpha_beta = use_alpha_beta
    print(f"Switched to {current_algorithm}!")

ai = AIPlayer(board, ai_player, human_player, use_alpha_beta=(current_algorithm == 'AlphaBeta'))

while True:
    screen.fill(BG_COLOR)
    board.draw_lines(screen)
    board.draw_figures(screen)
    toggle_rect, restart_rect = draw_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                toggle_algorithm()
            if event.key == pygame.K_r:
                restart_game()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos

            if toggle_rect.collidepoint(mouseX, mouseY):
                toggle_algorithm()

            elif restart_rect.collidepoint(mouseX, mouseY):
                restart_game()

            elif not game_over and mouseY < HEIGHT:
                if board.player_move(mouseX, mouseY, human_player):
                    if board.check_winner(human_player):
                        print('You Win!')
                        game_over = True
                    elif board.is_draw():
                        print('Draw!')
                        game_over = True
                    else:
                        # Update screen to show human move immediately
                        screen.fill(BG_COLOR)
                        board.draw_lines(screen)
                        board.draw_figures(screen)
                        draw_buttons()
                        pygame.display.update()
                        

                        # Pause for half a second so player can see
                        time.sleep(0.5)

                        move = ai.get_best_move()
                        if move:
                            board.make_move(move, ai_player)
                            if board.check_winner(ai_player):
                                print('AI Wins!')
                                game_over = True
                            elif board.is_draw():
                                print('Draw!')
                                game_over = True

    pygame.display.update()
    clock.tick(60)
    