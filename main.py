import pygame
import sys
import chessboard
import colors
import utilities
import minmax_algo

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

FONT = pygame.font.Font("fonts/arial_unicode.ttf", SQUARE_SIZE)

USE_AI = True



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chess AI")


def scale_symbol(symbol, color):
    text_surface = FONT.render(symbol, True, color)
    text_surface = pygame.transform.scale(text_surface, 
                                          (SQUARE_SIZE, SQUARE_SIZE))
    return text_surface

# Set up colors

# Set up rectangle
chessboard_grid = chessboard.generate_chessboard(BOARD_ROWS, BOARD_COLS)
chessboard_pixels = chessboard.get_chessboard_pixel_coords(BOARD_STARTING_X, 
                                                           BOARD_STARTING_Y, 
                                                           SQUARE_SIZE, 
                                                           chessboard_grid)

initialized_chessboard = chessboard.initialize_starting_board(chessboard_grid)
selected_piece = None
recompute_moves = True
game_over = False


current_team_color = "white"
# Main game loop
while game_over is False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position when clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Print the coordinates
            #print(f"Mouse clicked at ({mouse_x}, {mouse_y})")
            grid_pos_clicked = utilities.detect_square_clicked(chessboard_pixels,
                                                               SQUARE_SIZE,
                                                               mouse_x,
                                                               mouse_y)
            #print(grid_pos_clicked)
            #icon_rect.center = (cursor_x, cursor_y)
            # Blit icon onto the screen at the updated position
            #screen.blit(icon, icon_rect.topleft)
            if grid_pos_clicked is not None:
                row, col = grid_pos_clicked
                piece = initialized_chessboard[row][col]
                if selected_piece is not None:
                    if (row, col) in selected_piece.available_moves:
                        selected_piece.move_self(row, col)
                        recompute_moves = True
                        current_team_color = "white" if current_team_color == "black" else "black"
                    selected_piece = None
                elif piece is not None and piece.color == current_team_color:
                    if USE_AI is True:
                        if piece.color == "white":
                            selected_piece = piece

                    else:
                        selected_piece = piece
                    #print(selected_piece.available_moves, selected_piece.color, selected_piece.symbol)
            else:
                selected_piece = None
    # Draw background
    screen.fill(colors.brown)




    for r_idx, row in enumerate(initialized_chessboard):
        new_row = []
        for c_idx in range(len(row)):
            coord_x, coord_y = chessboard_pixels[r_idx][c_idx]
            square_color = colors.get_color_at_coords(r_idx, c_idx)
            pygame.draw.rect(screen, 
                             square_color, 
                             (coord_x, coord_y, SQUARE_SIZE, SQUARE_SIZE))
            curr_piece = initialized_chessboard[r_idx][c_idx]
            if curr_piece is not None:
                piece_color = colors.black if curr_piece.color == "black" else colors.white
                #text_surface = FONT.render(curr_piece.symbol, True, colors.black)
                text_surface = FONT.render(curr_piece.symbol, True, piece_color)
                # Blit the text surface onto the screen at the specified rectangle
                text_surface = pygame.transform.scale(text_surface, (SQUARE_SIZE, SQUARE_SIZE))
                text_rect = pygame.Rect(coord_x, coord_y, SQUARE_SIZE, SQUARE_SIZE)
                screen.blit(text_surface, text_rect)

    if selected_piece is not None:
        #print(selected_piece.available_moves)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        piece_symbol = selected_piece.symbol
        piece_color = colors.get_rgb_piece_color(selected_piece)
        scaled_symbol = scale_symbol(piece_symbol, piece_color)
        text_rect = pygame.Rect(mouse_x, mouse_y, SQUARE_SIZE, SQUARE_SIZE)
        screen.blit(scaled_symbol, text_rect)
        pygame.display.flip()

    if USE_AI is True and  current_team_color == "black":
        #((piece_row, piece_col), (move_row, move_col)) = minmax_algo.minimax(initialized_chessboard, 0, 3, True)

        #initialized_chessboard[piece_row][piece_col].move_self(move_row, move_col)
        pieces = list()
        for row in initialized_chessboard:
            for col in row:
                if piece is not None:
                    pieces.append(piece)
        #result = minmax_algo.minimax(initialized_chessboard, 0, 3, True)
        result = minmax_algo.minimax(initialized_chessboard, 0, 2, True)
        #print(initialized_chessboard)
        if result is not None:
            #TODO: result has a value of none at times where it shouldn't.
            #need to figure out why
            start, end = result
            if initialized_chessboard[start[0]][start[1]] is not None:
                initialized_chessboard[start[0]][start[1]].move_self(end[0], end[1])
                current_team_color = "white"
            else:
                print(f"no valid coordinates at {start[0]} {start[1]}")
                current_team_color = "white"
        else:
            print("white wins")
            exit(0)
        
        recompute_moves = True


    pygame.display.flip()

    # Control frame rate (optional)
    pygame.time.Clock().tick(60)

    # update the moves of all pieces
    # TODO: also perform check and checkmate detection here
    if recompute_moves is True:
        for row_idx, row in enumerate(initialized_chessboard):
            for col_idx in range(len(row)):
                piece = initialized_chessboard[row_idx][col_idx]
                if piece is not None:
                    #this is printing pieces as expected
                    piece.compute_valid_moves()
        kings = chessboard.get_kings(initialized_chessboard)
        #print(kings)
        for king in kings:
            #print(king)
            if chessboard.detect_check(initialized_chessboard, king):
                print(f"check detected: {king.color} king")
                if chessboard.detect_checkmate(initialized_chessboard, king):
                    game_over = True
                    winner = "black" if king.color == "white" else "white"
                    print(f"winner is {winner}")
                    print("board state: ")
                    for row in initialized_chessboard:
                        printable_row = []
                        for piece in row:
                            if piece is not None:
                                printable_row.append(piece.symbol + piece.color[0])
                            else:
                                printable_row.append(None)
                        print(printable_row)
        recompute_moves = False



    






    
    






