def detect_square_clicked(pixel_coords, square_size, mouse_x, mouse_y):
    for r_idx, row in enumerate(pixel_coords):
        for c_idx, (x, y) in enumerate(row):
            min_x = x
            max_x = x + square_size
            min_y = y
            max_y = y + square_size
            if min_x <= mouse_x <= max_x and min_y <= mouse_y <= max_y:
                return (r_idx, c_idx)
    return None
