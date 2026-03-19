from src.chess_engine import ChessEngine
from src.ai_opponent import AIOpponent

def main():
    engine = ChessEngine()
    ai = AIOpponent(depth=3)  # you can adjust depth for difficulty

    print("Welcome to AI Opponent Chess!")
    print(engine.board)

    while not engine.is_game_over():
        # Player move
        move = input("Enter your move in UCI format (e.g., e2e4): ")
        if not engine.make_move(move):
            print("Illegal move, try again.")
            continue

        print(engine.board)

        if engine.is_game_over():
            break

        # AI move
        ai_move = ai.choose_move(engine.board)
        if ai_move:
            engine.board.push(ai_move)
            print(f"AI plays: {ai_move}")
            print(engine.board)

    print("Game over!")
    print("Result:", engine.get_result())

if __name__ == "__main__":
    main()
