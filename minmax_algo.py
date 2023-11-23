import chessboard


def compute_value(board):
    # let's try defining the value of a current board state by the sum of the values of the black pieces
    # subtracted by the sum of the values of the white pieces
    total_white_value = 0
    total_black_value = 0
    for row in board:
        for piece in board:
            if piece is not None:
                if piece.color == "black":
                    total_black_value += piece.value
                else:
                    total_white_value += piece.value
    return total_black_value - total_white_value


def minimax(board, curr_depth, max_depth, own_turn):
    if curr_depth == max_depth:
        return 0
    best_move_value = 0
    best_move = float('-inf') if own_turn is True else float('inf')
    curr_team = "black" if own_turn is True else "white"

    for r_idx, row in enumerate(board):
        for c_idx, piece in enumerate(row):
            if piece is not None and piece.color == curr_team:
                for row, col in piece.available_moves:
                    piece.move_self(row, col)
                    move_value = minimax(piece.board, curr_depth+1, max_depth, own_turn=False)
                    if own_turn is True:
                        if move_value > best_move_val:
                            best_move_value = move_value
                            best_move = ((r_idx, c_idx), (row, col))
                    else:
                        if move_value < best_move_val:
                            best_move_value = move_value
                            best_move = ((r_idx, c_idx), (row, col))
                    piece.move_self(r_idx, c_idx) # undo the move
    if curr_depth == 0:
        return best_move
    else:
        return best_move_value


            

