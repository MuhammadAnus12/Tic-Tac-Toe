class AlphaBeta:
    def __init__(self, board):
        self.board = board

    def alphabeta(self, player, ai_player, human_player, alpha, beta):
        if self.board.check_winner(ai_player):
            return 1
        if self.board.check_winner(human_player):
            return -1
        if self.board.is_draw():
            return 0

        if player == ai_player:
            best_score = -float('inf')
            for move in self.board.available_moves():
                self.board.make_move(move, player)
                score = self.alphabeta(human_player, ai_player, human_player, alpha, beta)
                self.board.undo_move(move)
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = float('inf')
            for move in self.board.available_moves():
                self.board.make_move(move, player)
                score = self.alphabeta(ai_player, ai_player, human_player, alpha, beta)
                self.board.undo_move(move)
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return best_score
