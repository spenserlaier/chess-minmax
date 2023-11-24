import chessboard


def compute_value(board):
    # let's try defining the value of a current board state by the sum of the values of the black pieces
    # subtracted by the sum of the values of the white pieces
    total_white_value = 0
    total_black_value = 0
    for row in board:
        for piece in row:
            if piece is not None:
                if piece.color == "black":
                    total_black_value += piece.value
                else:
                    total_white_value += piece.value
    return total_black_value - total_white_value


def minimax(board, curr_depth, max_depth, own_turn):
    if curr_depth == max_depth:
        return 0
    best_move_value = float('-inf') if own_turn is True else float('inf')
    best_move = None
    curr_team = "black" if own_turn is True else "white"

    for r_idx, row in enumerate(board):
        for c_idx, piece in enumerate(row.copy()):
            # currently pieces are disappearing (black and white) - 
            #row.copy() seems to stop some, but not all 
            # from disappearning. why?
            # most likely because if a given move eliminates a piece somewhere,
            # the restoration operation might fail, because we iterate through
            # the board and not the pieces themselves. solution: iterate through
            # the pieces and not the board
            if piece is not None and piece.color == curr_team:
                piece.compute_valid_moves()
                #TODO: make sure this works
                #update: it doesn't
                #TODO: alpha beta pruning
                #TODO: remember to detect check and checkmate when computing moves
                for r, c in piece.available_moves.copy():
                    piece.move_self(r, c)
                    board_state_value = compute_value(piece.board)
                    move_value = minimax(piece.board, curr_depth+1, max_depth, own_turn=not own_turn)
                    if own_turn is True:
                        if board_state_value + move_value > best_move_value:
                            best_move_value = move_value
                            best_move = ((r_idx, c_idx), (r, c))
                    else:
                        if board_state_value + move_value < best_move_value:
                            best_move_value = move_value
                            best_move = ((r_idx, c_idx), (r, c))
                    #if board[piece.row][piece.col] is not None:
                        #board[r_idx][c_idx] = piece
                    #else:
                    piece.move_self(r_idx, c_idx) # undo the move
                    piece.moves_made -=1
    if curr_depth == 0:
        return best_move
    else:
        return best_move_value


            

