import pygame
import sys
import chessboard
import colors
import utilities

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SQUARE_SIZE = 50

BOARD_ROWS = 8
BOARD_COLS = 8

BOARD_STARTING_X = 20
BOARD_STARTING_Y = 20

FONT = pygame.font.Font("fonts/arial_unicode.ttf", SQUARE_SIZE-8)



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chess AI")

# Set up colors

# Set up rectangle
chessboard_grid = chessboard.generate_chessboard(BOARD_ROWS, BOARD_COLS)
chessboard_pixels = chessboard.get_chessboard_pixel_coords(BOARD_STARTING_X, 
                                                           BOARD_STARTING_Y, 
                                                           SQUARE_SIZE, 
                                                           chessboard_grid)

initialized_chessboard = chessboard.initialize_starting_board(chessboard_grid)




# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position when clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Print the coordinates
            print(f"Mouse clicked at ({mouse_x}, {mouse_y})")
            grid_pos_clicked = utilities.detect_square_clicked(chessboard_pixels,
                                                               SQUARE_SIZE,
                                                               mouse_x,
                                                               mouse_y)
            print(grid_pos_clicked)
            


    # Draw background
    screen.fill(colors.brown)
    for r_idx, row in enumerate(chessboard_grid):
        #for c_idx, (coord_x, coord_y) in enumerate(row):
        for c_idx in range(len(row)):
            coord_x, coord_y = chessboard_pixels[r_idx][c_idx]
            square_color = colors.get_color_at_coords(r_idx, c_idx)
            pygame.draw.rect(screen, 
                             square_color, 
                             (coord_x, coord_y, SQUARE_SIZE, SQUARE_SIZE))
            curr_piece = initialized_chessboard[r_idx][c_idx]
            if curr_piece is not None:
                piece_color = colors.white if curr_piece.color == "black" else colors.brown
                #text_surface = FONT.render(curr_piece.symbol, True, colors.black)
                text_surface = FONT.render(curr_piece.symbol, True, piece_color)
                # Blit the text surface onto the screen at the specified rectangle
                text_rect = pygame.Rect(coord_x, coord_y, SQUARE_SIZE, SQUARE_SIZE)
                screen.blit(text_surface, text_rect)


    pygame.display.flip()

    # Control frame rate (optional)
    pygame.time.Clock().tick(60)

