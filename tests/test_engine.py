import unittest
from src.chess_engine import ChessEngine

class TestChessEngine(unittest.TestCase):
    def setUp(self):
        self.engine = ChessEngine()

    def test_initial_board_not_game_over(self):
        self.assertFalse(self.engine.is_game_over())

    def test_make_legal_move(self):
        result = self.engine.make_move("e2e4")
        self.assertTrue(result)

    def test_illegal_move(self):
        result = self.engine.make_move("e9e5")  # invalid square
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
