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


def minimax_test(pieces, curr_depth, max_depth, own_turn):
    if curr_depth == max_depth:
        return 0
    best_move_value = float('-inf') if own_turn is True else float('inf')
    best_move = None
    curr_team = "black" if own_turn is True else "white"
    pieces = list()
    # whereas before almost all the pieces disappeared, now it's just white that disappears. why?
    # every call to move is matched by an un-move call, so this isn't the issue
    # and there's no piece deletion taking place
    # experiment: try passing only pieces, and not board to minimax
    for piece in pieces:
        r_idx, c_idx = piece.row, piece.col
        #if piece is not None and piece.color == curr_team:
        if piece.color == curr_team:
            piece.compute_valid_moves()
            #TODO: make sure this works
            #update: it doesn't
            #TODO: alpha beta pruning
            #TODO: remember to detect check and checkmate when computing moves
            #may want to integrate this into the piece classes themselves
            for r, c in piece.available_moves.copy():
                piece.move_self(r, c)
                board_state_value = compute_value(piece.board)
                move_value = minimax(pieces, curr_depth+1, max_depth, own_turn=not own_turn)
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
        print(best_move)
        return best_move
    else:
        return best_move_value


            

def minimax(board, curr_depth, max_depth, own_turn):
    if curr_depth == max_depth:
        return 0
    best_move_value = float('-inf') if own_turn is True else float('inf')
    best_move = None
    curr_team = "black" if own_turn is True else "white"
    pieces = list()
    for row in board:
        for piece in row:
            if piece is not None:
                pieces.append(piece)
    # whereas before almost all the pieces disappeared, now it's just white that disappears. why?
    # every call to move is matched by an un-move call, so this isn't the issue
    # and there's no piece deletion taking place
    # experiment: try passing only pieces, and not board to minimax
    for piece in pieces:
        r_idx, c_idx = piece.row, piece.col
        #if piece is not None and piece.color == curr_team:
        if piece.color == curr_team:
            piece.compute_valid_moves()
            #TODO: make sure this works
            #update: it doesn't
            #TODO: alpha beta pruning
            #TODO: remember to detect check and checkmate when computing moves
            for r, c in piece.available_moves.copy():
                piece.move_self(r, c)
                board_state_value = compute_value(piece.board)
                move_value = minimax(board, curr_depth+1, max_depth, own_turn=not own_turn)
                # when we pass in piece.board instead of simply board,
                # more pieces disappear. why?
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
        for row in board:
            for piece in row:
                if piece is not None:
                    print(piece.row, piece.col)

        return best_move
    else:
        return best_move_value


            

