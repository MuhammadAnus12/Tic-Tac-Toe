class Minimax:
    def __init__(self, board):
        self.board = board

    def minimax(self, player, ai_player, human_player):
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
                score = self.minimax(human_player, ai_player, human_player)
                self.board.undo_move(move)
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.board.available_moves():
                self.board.make_move(move, player)
                score = self.minimax(ai_player, ai_player, human_player)
                self.board.undo_move(move)
                best_score = min(score, best_score)
            return best_score
