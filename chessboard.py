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
