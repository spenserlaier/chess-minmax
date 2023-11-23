def test_generic_directions(piece, directions, num_iterations=None):
    def generic_test(piece, row_diff, col_diff, moves, num_iterations=None):
        test_row = piece.row
        test_col = piece.col
        curr_iterations = 0
        #print(piece.board)
        while (0 <= test_row < len(piece.board) 
               and 0 <= test_col < len(piece.board)):
            #print(f"testing piece: {piece}, at row {test_row}, and col {test_col}")
            if piece.board[test_row][test_col] is None:
                moves.add((test_row, test_col))
            elif piece.board[test_row][test_col].color != piece.color:
                moves.add((test_row, test_col))
                break
            elif piece.row != test_row or piece.col != test_col:
                #print('breaking early; encontered same color')
                #TODO: this is the only branch being taken. why?
                #answer: the piece has been detecting itself and executing the break
                # on the first check
                break
            test_row += row_diff
            test_col += col_diff
            curr_iterations += 1
            if num_iterations is not None and curr_iterations == num_iterations:
                break
        return moves
    final_moves = set()
    if "up" in directions:
        final_moves = generic_test(piece, row_diff=-1, col_diff=0, moves=final_moves)
    if "down" in directions:
        final_moves = generic_test(piece, row_diff=+1, col_diff=0, moves=final_moves)
    if "left" in directions:
        final_moves = generic_test(piece, row_diff=0, col_diff=-1, moves=final_moves)
    if "right" in directions:
        final_moves = generic_test(piece, row_diff=0, col_diff=1, moves=final_moves)
    if "up-right" in directions:
        final_moves = generic_test(piece, row_diff=-1, col_diff=1, moves=final_moves)
    if "down-right" in directions:
        final_moves = generic_test(piece, row_diff=1, col_diff=1, moves=final_moves)
    if "up-left" in directions:
        final_moves = generic_test(piece, row_diff=-1, col_diff=-1, moves=final_moves)
    if "down-left" in directions:
        final_moves = generic_test(piece, row_diff=+1, col_diff=-1, moves=final_moves)
    return final_moves

        






class Piece:

    def __init__(self, row, col, board, color):
        self.row = row
        self.col = col
        # self.symbol = "placeholder"
        self.board = board
        self.color = color
        self.available_moves = set()
        self.moves_made = 0

    def compute_valid_moves(self):
        return True

    def move_self(self, row, col):
        self.board[self.row][self.col] = None
        self.row = row
        self.col = col
        self.board[row][col] = self
        self.moves_made += 1


class Pawn(Piece):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board, color)
        self.symbol = u"♟︎"

    def compute_valid_moves(self):
        row, col = self.row, self.col
        self.available_moves = set()
        if self.color == 'black':
            # check that we can move down one row
            if self.row + 1 < len(self.board):
                if self.board[row+1][col] is None:
                    self.available_moves.add((self.row+1, self.col))
                    if (
                        self.moves_made == 0 
                        and self.row+2 < len(self.board) 
                        and self.board[row+2][col] is None
                    ):
                        self.available_moves.add((self.row+2, self.col))
                if (
                    self.col - 1 >= 0 
                    and self.board[row+1][self.col-1] is not None 
                    and self.board[self.row+1][self.col-1].color != self.color
                ):
                    
                    self.available_moves.add((self.row+1, self.col-1))
                if (
                    self.col + 1 < len(self.board) 
                    and self.board[row+1][self.col+1] is not None 
                    and self.board[self.row+1][self.col+1].color != self.color
                ):

                    self.available_moves.add((self.row+1, self.col+1))
        elif self.color == 'white':
            # check that we can move up one space
            if self.row - 1 >= 0:
                if self.board[row-1][col] is None:
                    self.available_moves.add((self.row-1, self.col))
                    if (
                        self.moves_made == 0 
                        and self.row-2 >= 0 
                        and self.board[row-2][col] is None
                    ):
                        self.available_moves.add((self.row-2, self.col))
                if (
                    self.col - 1 >= 0 
                    and self.board[row-1][self.col-1] is not None 
                    and self.board[self.row-1][self.col-1].color != self.color
                ):

                    self.available_moves.add((self.row-1, self.col-1))
                if (
                    self.col + 1 < len(self.board) 
                    and self.board[row-1][self.col+1] is not None 
                    and self.board[self.row-1][self.col+1].color != self.color
                ):

                    self.available_moves.add((self.row-1, self.col+1))

class Rook(Piece):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board, color)
        self.symbol = u"♜"

    def compute_valid_moves(self):
        self.available_moves =  test_generic_directions(self, ["left", "right", "up", "down"])

class Knight(Piece):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board, color)
        self.symbol = u"♞"

    def compute_valid_moves(self ):
        steep_up_right = (self.row-2, self.col+1)
        flat_up_right= (self.row-1, self.col+2)

        steep_up_left = (self.row-2, self.col-1)
        flat_up_left= (self.row-1, self.col-2)

        steep_down_right = (self.row+2, self.col+1)
        flat_down_right = (self.row+1, self.col+2)

        steep_down_left = (self.row+2, self.col-1)
        flat_down_left = (self.row+1, self.col-2)
        for row, col in [steep_up_right, flat_up_right, 
                       steep_up_left, flat_up_left, 
                       steep_down_right, flat_down_right,
                       steep_down_left, flat_down_left]:
            if 0 <= row < len(self.board) and 0 <= col < len(self.board):
                if self.board[row][col] is None or self.board[row][col].color != self.color:
                    self.available_moves.add((row, col))

class Bishop(Piece):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board, color)
        self.symbol = u"♝"

    def compute_valid_moves(self ):
        self.available_moves =  test_generic_directions(self, ["up-left","up-right", "down-left", "down-right"])

class Queen(Piece):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board, color)
        self.symbol = u"♛"

    def compute_valid_moves(self ):
        self.available_moves = test_generic_directions(self, ["up", "down", "left", "right",  "up-left","up-right", "down-left", "down-right"])


class King(Piece):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board, color)
        #if self.color == "black":
        self.symbol = u"♚"
        #else:
            #self.symbol = u"♔"
    def compute_valid_moves(self ):
        self.available_moves = test_generic_directions(self, ["up","left","down","right","up-left","up-right","down-left","down-right" ]
                                       ,num_iterations=1)

