import chessboard


def compute_value(board):
    # let's try defining the value of a current board state by the sum of the values of the black pieces
    # subtracted by the sum of the values of the white pieces
    total_white_value = 0
    total_black_value = 0
    for row in board:
        for piece in row:
            if piece != None:
                if piece.color == "black":
                    total_black_value += piece.value
                else:
                    total_white_value += piece.value
    return total_black_value - total_white_value
'''
minimax bug summary:
    unlike in regular (non-ai) play, the ai seems to have issues properly recognizing valid moves and pieces,
    which is strange because the same move detection code is used in both gamemodes.
    For example, each piece automatically excludes its starting position from the list of moves,
    but the ai will try to execute "moves" to the starting position
    Similarly, each piece excludes moves that explicitly capture the king, but the ai will
    attempt to execute those moves. This implies that there's some kind of miscommunication
    between the application components
'''


def minimax(board, curr_depth, max_depth, own_turn):
    if curr_depth == max_depth:
        #return 0
        return compute_value(board)
    #best_move_value = float('-inf') if own_turn is True else float('inf')
    best_move_value = 0
    best_move = None
    curr_team = "black" if own_turn is True else "white"
    pieces = list()
    for row in board:
        for piece in row:
            if piece is not None:
                pieces.append(piece)
    kings = chessboard.get_kings(board)
    curr_king = None
    for king in kings:
        if king.color == curr_team:
            curr_king = king
    if curr_king == None:
        print("error: ai couldn't find its king")
        exit(1)
    for row in board:
        for piece in row:
            if piece != None and piece.color == curr_team:
                #print(f"ai is checking piece: {curr_team} {piece.symbol}")
                piece.compute_valid_moves()
                #TODO: alpha beta pruning
                currently_in_check = chessboard.detect_check(board, curr_king)
                r_idx, c_idx = piece.row, piece.col
                for r, c in piece.available_moves.copy():
                    if r == r_idx and c == c_idx:
                        print(f"excluding a move to the same position: {r} {c} from {r_idx} {c_idx}")
                        continue
                    old_piece = board[r][c]
                    if old_piece != None and old_piece.symbol == "♚":
                        print("something is wrong. ai trying to occupy a king spot")
                    piece.move_self(r, c)
                    if currently_in_check:
                        print('in check; ignoring a move')
                        still_in_check = chessboard.detect_check(board, curr_king)
                        if still_in_check: #that means that this move is invalid
                            piece.move_self(r_idx, c_idx) # undo the move
                            #board[r][c] = old_piece
                            if old_piece != None:
                                old_piece.move_self(r, c)
                                old_piece.moves_made -=1
                            piece.moves_made -=2
                            continue
                    if best_move == None:
                        best_move = ((r_idx, c_idx), (r, c))
                    board_state_value = compute_value(board)
                    own_turn = not own_turn
                    move_value = minimax(board, curr_depth+1, max_depth, own_turn)
                    # TODO: also need to exclude the reverse of moves just taken
                    # TODO: ai seems to be recognizing fewer moves than actually exist
                    piece.move_self(r_idx, c_idx) # undo the move
                    #board[r][c] = old_piece
                    if old_piece is not None:
                        old_piece.move_self(r, c)
                        old_piece.moves_made -=1
                    piece.moves_made -=2
                    if own_turn is True:
                        #if board_state_value + move_value >= best_move_value:
                        if  move_value >= best_move_value:

                            best_move_value = move_value
                            best_move = ((r_idx, c_idx), (r, c))
                    else:
                        if  move_value <= best_move_value:
                            best_move_value = move_value
                            best_move = ((r_idx, c_idx), (r, c))
    if curr_depth == 0:
        print(f"best move: {best_move}")
        return best_move
    else:
        return best_move_value


