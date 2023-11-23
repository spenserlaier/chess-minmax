def test_generic_directions(piece, directions):
    def generic_test(piece, row_diff, col_diff, moves):
        test_row = piece.row
        test_col = piece.col
        while (0 <= test_row < len(piece.board) 
               and 0 <= test_col < len(piece.board)):
            if piece.board[test_row][test_col] is None:
                moves.add((test_row, test_col))
            elif piece.board[test_row][test_col].color != piece.color:
                moves.add((test_row, test_col))
                break
            else:
                break
            test_row += row_diff
            test_col += col_diff
        return moves
    final_moves = set()
    if "up" in directions:
        final_moves = generic_test(piece, 
                                   row_diff=-1, 
                                   col_diff=0, 
                                   moves=final_moves)
    if "down" in directions:
        final_moves = generic_test(piece, 
                                   row_diff=+1, 
                                   col_diff=0, 
                                   moves=final_moves)
    if "left" in directions:
        final_moves = generic_test(piece, 
                                   row_diff=0, 
                                   col_diff=-1,
                                   moves=final_moves)
    if "right" in directions:
        final_moves = generic_test(piece, 
                                   row_diff=0, 
                                   col_diff=1, 
                                   moves=final_moves)
    if "up-right" in directions:
        final_moves = generic_test(piece, 
                                   row_diff=-1, 
                                   col_diff=1, 
                                   moves=final_moves)
    if "down-right" in directions:
        final_moves = generic_test(piece, 
                                   row_diff=+1, 
                                   col_diff=1, 
                                   moves=final_moves)
    if "up-left" in directions:
        final_moves = generic_test(piece, 
                                   row_diff=-1, 
                                   col_diff=-1, 
                                   moves=final_moves)
    if "down-left" in directions:
        final_moves = generic_test(piece, 
                                   row_diff=+1, 
                                   col_diff=-1, 
                                   moves=final_moves)
    return final_moves

        






class Piece:

    def __init__(self, row, col, board, color):
        self.row = row
        self.col = col
        # self.symbol = "placeholder"
        self.board = board
        self.color = color
        self.available_moves = set()

    def compute_valid_moves(self):
        return True

    def move_self(self, row, col):
        self.board[self.row][self.col] = None
        self.row = row
        self.col = col
        self.board[row][col] = self


class Pawn(Piece):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board, color)
        self.symbol = u"♟︎"

    def compute_valid_moves(self ):
        return True


class Rook(Piece):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board, color)
        self.symbol = u"♜"

    def compute_valid_moves(self):
        return test_generic_directions(self, ["left", "right", "up", "down"])

class Knight(Piece):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board, color)
        self.symbol = u"♞"

    def compute_valid_moves(self ):
        moves = set()
        test_left = self.col
        while test_left >= 0:
            if self.board[self.row][test_left] is None:
                moves.add((self.row, test_left))
            elif self.board[self.row][test_left].color != self.color:
                moves.add((self.row, test_left))
                break
            else:
                break
            test_left -=1
        return True


class Bishop(Piece):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board, color)
        self.symbol = u"♝"

    def compute_valid_moves(self ):
        return test_generic_directions(self, ["up-left","up-right", "down-left", "down-right"])

class Queen(Piece):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board, color)
        self.symbol = u"♛"

    def compute_valid_moves(self ):
        return test_generic_directions(self, ["up", "down", "left", "right",  "up-left","up-right", "down-left", "down-right"])


class King(Piece):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board, color)
        #if self.color == "black":
        self.symbol = u"♚"
        #else:
            #self.symbol = u"♔"

    def compute_valid_moves(self ):
        return True

