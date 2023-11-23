import piece_logic


white = (255, 255, 255)
black = (0, 0, 0)
brown = (128, 71, 59)
blue = (106, 189, 243)
dark_gray = (68, 71, 74)
light_gray = ( 187, 188, 189 )


def get_color_at_coords(x, y):
    if x % 2 == 0:
        if y % 2 == 0:
            return light_gray
        return dark_gray
    else:
        if y % 2 == 1:
            return light_gray
        return dark_gray


def get_rgb_piece_color(piece):
    if piece.color == "black":
        return black
    return white

