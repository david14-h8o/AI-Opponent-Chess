import chess
import math

class AIOpponent:
    def __init__(self, depth=3):
        self.depth = depth

    def evaluate_board(self, board):
        """Simple heuristic: material balance."""
        piece_values = {
            chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3,
            chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0
        }
        value = 0
        for piece_type in piece_values:
            value += len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]
            value -= len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]
        return value

    def minimax(self, board, depth, alpha, beta, maximizing):
        if depth == 0 or board.is_game_over():
            return self.evaluate_board(board), None

        best_move = None
        if maximizing:
            max_eval = -math.inf
            for move in board.legal_moves:
                board.push(move)
                eval, _ = self.minimax(board, depth-1, alpha, beta, False)
                board.pop()
                if eval > max_eval:
                    max_eval, best_move = eval, move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = math.inf
            for move in board.legal_moves:
                board.push(move)
                eval, _ = self.minimax(board, depth-1, alpha, beta, True)
                board.pop()
                if eval < min_eval:
                    min_eval, best_move = eval, move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def choose_move(self, board):
        _, move = self.minimax(board, self.depth, -math.inf, math.inf, board.turn == chess.WHITE)
        return move
