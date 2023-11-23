white = (255, 255, 255)
black = (0, 0, 0)
brown = (128, 71, 59)


def get_color_at_coords(x, y):
    if x % 2 == 0:
        if y % 2 == 0:
            return white
        return black
    else:
        if y % 2 == 1:
            return white
        return black
