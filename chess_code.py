import sys

def parse_fen(fen_string):
    """
    Parse FEN string into a dictionary representation.
    
    Args:
        fen_string (str): FEN string representing the chess board.
    
    Returns:
        dict: Dictionary containing the chess board state.
    """
    # Split FEN string into components
    rows, turn, castling, en_passant, halfmove, fullmove = fen_string.split()
    
    # Initialize board dictionary
    board = {}
    
    # Parse rows
    for i, row in enumerate(rows.split('/')):
        board[i] = {}
        for j, piece in enumerate(row):
            if piece.isdigit():
                # Empty squares
                for k in range(int(piece)):
                    board[i][j + k] = '.'
                j += int(piece) - 1
            else:
                # Pieces
                board[i][j] = piece
    
    # Parse turn
    board['turn'] = turn
    
    # Parse castling
    board['castling'] = castling
    
    # Parse en passant
    board['en_passant'] = en_passant
    
    # Parse halfmove and fullmove
    board['halfmove'] = int(halfmove)
    board['fullmove'] = int(fullmove)
    
    return board

def render_board(board):
    """
    Render the chess board in a text-based representation.
    
    Args:
        board (dict): Dictionary containing the chess board state.
    
    Returns:
        str: Text-based representation of the chess board.
    """
    output = ''
    
    # Print board rows
    for i in range(8):
        output += ' '.join(str(board[i][j]) for j in range(8)) + '\n'
    
    # Print additional information
    output += f'Turn: {board["turn"]}\n'
    output += f'Castling: {board["castling"]}\n'
    output += f'En passant: {board["en_passant"]}\n'
    output += f'Halfmove clock: {board["halfmove"]}\n'
    output += f'Fullmove number: {board["fullmove"]}\n'
    
    return output

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python (link unavailable) <FEN_string>")
        sys.exit(1)
    
    fen_string = sys.argv[1]
    board = parse_fen(fen_string)
    print(render_board(board))