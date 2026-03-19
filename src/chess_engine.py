import chess

class ChessEngine:
    def __init__(self):
        self.board = chess.Board()

    def make_move(self, move_uci: str):
        move = chess.Move.from_uci(move_uci)
        if move in self.board.legal_moves:
            self.board.push(move)
            return True
        return False

    def is_game_over(self):
        return self.board.is_game_over()

    def get_result(self):
        return self.board.result()
