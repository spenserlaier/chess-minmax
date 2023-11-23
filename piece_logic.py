class Piece:

    def __init__(self, x, y, board, color):
        self.x = x
        self.y = y
        # self.symbol = "placeholder"
        self.board = board
        self.color = color

    def check_valid_move(next_x, next_y):
        return True


class Pawn(Piece):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board, color)
        if self.color == "black":
            self.symbol = u"♟︎"
        else:
            self.symbol = u"♙"

    def check_valid_move(self, next_x, next_y):
        return True


class Rook(Piece):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board, color)
        if self.color == "black":
            self.symbol = u"♜"
        else:
            self.symbol = u"♖"

    def check_valid_move(self, next_x, next_y):
        return True


class Knight(Piece):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board, color)
        if self.color == "black":
            self.symbol = u"♞"
        else:
            self.symbol = u"♘"

    def check_valid_move(self, next_x, next_y):
        return True


class Bishop(Piece):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board, color)
        if self.color == "black":
            self.symbol = u"♝"
        else:
            self.symbol = u"♗"

    def check_valid_move(self, next_x, next_y):
        return True


class Queen(Piece):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board, color)
        if self.color == "black":
            self.symbol = u"♛"
        else:
            self.symbol = u"♕"

    def check_valid_move(self, next_x, next_y):
        return True


class King(Piece):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board, color)
        if self.color == "black":
            self.symbol = u"♚"
        else:
            self.symbol = u"♔"

    def check_valid_move(self, next_x, next_y):
        return True

