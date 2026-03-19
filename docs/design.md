# AI Opponent Chess - Design Document
 
## Overview
This project implements a chess game with an AI opponent.  
The system is divided into four main parts:
- **Chess Engine** (`src/chess_engine.py`): Handles board state and move validation.
- **AI Opponent** (`src/ai_opponent.py`): Uses minimax with alpha-beta pruning to choose moves.
- **Game UI** (`src/game_ui.py`): Provides a graphical interface for players.
- **Utils** (`src/utils.py`): Helper functions for conversions and utilities.

## Architecture
- **Models**: Trained AI models are stored in `models/trained_model.pkl`.
- **Tests**: Unit tests are located in `tests/test_engine.py`.
- **Docs**: Documentation lives here in `docs/design.md`.

## Future Enhancements
- Add reinforcement learning for stronger AI.
- Improve UI with drag-and-drop piece movement.
- Integrate online multiplayer.
