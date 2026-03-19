def uci_to_coords(uci_move):
    """Convert UCI move (e.g., 'e2e4') to board coordinates."""
    start = (8 - int(uci_move[1]), ord(uci_move[0]) - ord('a'))
    end = (8 - int(uci_move[3]), ord(uci_move[2]) - ord('a'))
    return start, end
