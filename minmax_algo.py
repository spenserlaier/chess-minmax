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
    pieces = list()
    for row in board:
        for piece in row:
            if piece is not None:
                pieces.append(piece)
    # whereas before almost all the pieces disappeared, now it's just white that disappears. why?
    # every call to move is matched by an un-move call, so this isn't the issue
    # and there's no piece deletion taking place
    # experiment: try passing only pieces, and not board to minimax
    # experiment failed, it simply returned None, without any moves
    for piece in pieces:
        #if piece is not None and piece.color == curr_team:
        if piece.color == curr_team and piece.board[piece.row][piece.col] == piece:
            piece.compute_valid_moves()
            #TODO: make sure this works
            #update: it doesn't
            #TODO: alpha beta pruning
            #TODO: remember to detect check and checkmate when computing moves
            r_idx, c_idx = piece.row, piece.col
            for r, c in piece.available_moves.copy():
                old_piece = board[r][c]
                piece.move_self(r, c)
                board_state_value = compute_value(board)
                own_turn = not own_turn
                move_value = minimax(board, curr_depth+1, max_depth, own_turn)
                # when we pass in piece.board instead of simply board,
                # more pieces disappear. why? in theory both references should contain
                # the same contents. is some operation causing a copy and decoupling somewhere?
                # one idea: maybe the order is reversed? try executing earlier moves deeper
                # in the recursion rather than shallower?
                # update: we may simply be eating up pieces without restoring them
                # to solve, we may need to store the piece and retrieve it
                # TODO: ai is somehow making non-moves (i.e. moving to the same position) -- need 
                # to figure out how that's happening and stop it
                piece.move_self(r_idx, c_idx) # undo the move
                board[r][c] = old_piece
                piece.moves_made -=1
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
    if curr_depth == 0:
        print(f"best move: {best_move}")
        return best_move
    else:
        return best_move_value


