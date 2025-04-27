# ai/ai_player.py

from minimax import Minimax
from alphabeta import AlphaBeta

class AIPlayer:
    def __init__(self, board, ai_player, human_player, use_alpha_beta=True):
        self.board = board
        self.ai_player = ai_player
        self.human_player = human_player
        self.use_alpha_beta = use_alpha_beta

        self.minimax_ai = Minimax(board)
        self.alphabeta_ai = AlphaBeta(board)

    def get_best_move(self):
        best_score = -float('inf')
        move = None

        for m in self.board.available_moves():
            self.board.make_move(m, self.ai_player)
            if self.use_alpha_beta:
                score = self.alphabeta_ai.alphabeta(self.human_player, self.ai_player, self.human_player, -float('inf'), float('inf'))
            else:
                score = self.minimax_ai.minimax(self.human_player, self.ai_player, self.human_player)
            self.board.undo_move(m)

            if score > best_score:
                best_score = score
                move = m

        return move
