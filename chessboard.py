import piece_logic

def generate_chessboard(board_rows, board_cols):
    single_row = [None]*board_rows
    board = []
    for i in range(board_cols):
        row_copy = single_row.copy()
        board.append(row_copy)
    return board


def get_chessboard_pixel_coords(starting_x, 
                                starting_y, 
                                square_size, 
                                curr_chessboard):
    curr_x, curr_y = starting_x, starting_y
    output = []
    for r_idx, row in enumerate(curr_chessboard):
        new_row = []
        curr_x = starting_x
        for c_idx, col in enumerate(row):
            new_row.append((curr_x, curr_y))
            curr_x += square_size
        curr_y += square_size
        output.append(new_row)
    return output

def initialize_starting_board(chessboard):
    for r_idx, row in enumerate(chessboard):
        new_row = []
        for c_idx in range(len(row)):
            piece = None
            if r_idx == 1:  # black pawn
                piece = piece_logic.Pawn(r_idx, c_idx, chessboard, "black")
            elif r_idx == len(chessboard) - 2:  # white pawn
                piece = piece_logic.Pawn(r_idx, c_idx, chessboard, "white")
            elif r_idx == 0 or r_idx == len(chessboard) - 1:
                color = "black" if r_idx == 0 else "white"
                if c_idx == 0 or c_idx == len(row) - 1:  # rook
                    piece = piece_logic.Rook(r_idx, c_idx, chessboard, color)
                elif c_idx == 1 or c_idx == len(row) - 2:  # knight
                    piece = piece_logic.Knight(r_idx, c_idx, chessboard, color)
                elif c_idx == 2 or c_idx == len(row) - 3:  # bishop
                    piece = piece_logic.Bishop(r_idx, c_idx, chessboard, color)
                elif c_idx == 3:  # queen
                    piece = piece_logic.Queen(r_idx, c_idx, chessboard, color)
                elif c_idx == 4:  # king
                    piece = piece_logic.King(r_idx, c_idx, chessboard, color)
            #chessboard[r_idx][c_idx] = piece
            new_row.append(piece)
        chessboard[r_idx] = new_row
    return chessboard


def detect_check(chessboard, king):
    king_color = king.color
    for row in chessboard:
        for piece in row:
            #if piece.available_moves.contains((king.x, king.y)) and piece.color != king_color:
            if piece is not None and piece != king:
                piece.compute_valid_moves()
                if piece.checks_king:
                    print(f"check detected: {king.color} {king.symbol} threatened by {piece.color} {piece.symbol}")
                    return True

                #if (king.row, king.col) in piece.available_moves and piece.color != king_color:
                    # we may not need to check color, because the king shouldn't be in the same colored
                    # pieces available moves anyway
                    #print(f"check detected: {king.color} {king.symbol} threatened by {piece.color} {piece.symbol}")
                    #return True
    return False

def prune_moves_for_checked_team(board, piece_row, piece_col, king):
    piece = board[piece_row][piece_col]
    for row, col in piece.available_moves.copy():
        piece.move_self(row, col)
        if detect_check(piece.board, king) is True:
            piece.available_moves.remove((row, col))
        piece.move_self(piece_row, piece_col) #move the piece back to its original state


def detect_checkmate(chessboard, king):
    # traverse one layer of moves from the pieces with the same color of
    # the checked king. if we run check detection for each of these moves
    # and none of them returns a non-checked state, then we have checkmate
    valid_moves_after_check = 0
    for row in chessboard:
        for piece in row:
            if piece is not None:
                prune_moves_for_checked_team(chessboard, piece.row, piece.col, king)
                valid_moves_after_check += len(piece.available_moves)
    return True if valid_moves_after_check > 0 else False


def get_kings(chessboard):
    kings = []
    for row in chessboard:
        for piece in row:
            if piece is not None:
                if piece.symbol == '♚':
                    kings.append(piece)
    return kings






            
            











            
