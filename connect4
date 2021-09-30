from pprint import pprint

import pygame

import Resources

pygame.init()
pygame.font.init()
pygame.mixer.init()


# global vars
screen_width = 560
screen_height = 640
cell_dim = 80
cell_size = (cell_dim, cell_dim)
board_cells_across = 7
board_cells_down = 6

cell_img = pygame.image.load(r"Resources/board_cell.png")
highlight_cell_img = pygame.image.load(r"Resources/board_cell_highlighted.png")
red_chip = pygame.image.load(r"Resources/red_chip.png")
yellow_chip = pygame.image.load(r"Resources/yellow_chip.png")
hover = pygame.mixer.Sound("Resources/hover.wav")
change = pygame.mixer.Sound("Resources/column_change.wav")
click = pygame.mixer.Sound("Resources/click.wav")
placed = pygame.mixer.Sound("Resources/placed.wav")
applause = pygame.mixer.Sound("Resources/applause.wav")

board = [[0 for i in range(board_cells_across)] for j in range(board_cells_down)]
row_start_posns = sorted(
    [(row, col) for col in range(len(board[0]) - 3) for row in range(len(board))]
)
col_start_posns = sorted(
    [(row, col) for col in range(len(board[0])) for row in range(len(board) - 3)]
)
diag_right_start_posns = sorted(list(set(row_start_posns) & set(col_start_posns)))
diag_left_start_posns = sorted(
    list(
        set((row, col) for col in range(3, len(board[0])) for row in range(len(board)))
        & set(col_start_posns)
    )
)


def draw_board(surface, board):
    surface.fill((0, 0, 0))
    for i in range(6):
        for j in range(7):
            surface.blit(cell_img, (j * cell_dim, 160 + i * cell_dim))
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] == 1:
                surface.blit(red_chip, (j * cell_dim, 160 + i * cell_dim))
            elif board[i][j] == 2:
                surface.blit(yellow_chip, (j * cell_dim, 160 + i * cell_dim))
    pygame.display.update()


def draw_winning_board(surface, board, winning_cells):
    draw_board(surface, board)
    for cell in winning_cells:
        i, j = cell
        surface.blit(highlight_cell_img, (j * cell_dim, 160 + i * cell_dim))
        if board[i][j] == 1:
            surface.blit(red_chip, (j * cell_dim, 160 + i * cell_dim))
        elif board[i][j] == 2:
            surface.blit(yellow_chip, (j * cell_dim, 160 + i * cell_dim))
    pygame.display.update()
    pygame.mixer.Sound.play(applause)


def get_move(surface, board, player):
    if player == 1:
        chip = red_chip
    else:
        chip = yellow_chip
    mouse_pos = pygame.mouse.get_pos()[0]
    if mouse_pos < 40:
        mouse_pos = 40
    if mouse_pos > 520:
        mouse_pos = 520
    surface.blit(chip, (mouse_pos - 40, 80))
    pygame.display.update()
    move = None
    # clock = pygame.time.Clock
    while not move:
        # move_time += clock.get_rawtime()
        # clock.tick()
        pygame.time.wait(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()[0]
                if mouse_pos < 40:
                    mouse_pos = 40
                if mouse_pos > 520:
                    mouse_pos = 520
                pygame.draw.rect(surface, (0, 0, 0), (0, 80, 560, 80))
                surface.blit(chip, (mouse_pos - 40, 80))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.draw.rect(surface, (0, 0, 0), (0, 80, 560, 80))
                pygame.display.update()
                pygame.mixer.Sound.play(click)
                return mouse_pos // 80
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


def init():
    board = [[0 for i in range(7)] for j in range(6)]
    return board


def place_piece(player, col, board):
    if board[0][col]:
        print("Column full, try another")
        return board, False
    for row in board[::-1]:
        if not row[col]:
            row[col] = player
            return board, True


def check_rows(board):
    for posn in row_start_posns:
        r, c = posn
        set_of_four = [board[r][column] for column in range(c, c + 4)]
        row_found, winner = check_four(set_of_four, "row", r, c)
        if row_found:
            winning_cells = [(r, column) for column in range(c, c + 4)]
            return True, winning_cells, winner
    return False, None, None


def check_cols(board):
    for posn in col_start_posns:
        r, c = posn
        set_of_four = [board[row][c] for row in range(r, r + 4)]
        col_found, winner = check_four(set_of_four, "column", r, c)
        if col_found:
            winning_cells = [(row, c) for row in range(r, r + 4)]
            return True, winning_cells, winner
    return False, None, None


def check_right_diag(board):
    for posn in diag_right_start_posns:
        r, c = posn
        set_of_four = [board[r + n][c + n] for n in range(4)]
        diag_found, winner = check_four(set_of_four, "diagonal down left", r, c)
        if diag_found:
            winning_cells = [(r + n, c + n) for n in range(4)]
            return True, winning_cells, winner
    return False, None, None


def check_left_diag(board):
    for posn in diag_left_start_posns:
        r, c = posn
        set_of_four = [board[r + n][c - n] for n in range(4)]
        diag_found, winner = check_four(set_of_four, "diagonal down right", r, c)
        if diag_found:
            winning_cells = [(r + n, c - n) for n in range(4)]
            return True, winning_cells, winner
    return False, None, None


def check_four(set_of_four, direction, r, c):
    for cell in set_of_four:
        if not cell:
            break
        if set_of_four[0] == set_of_four[1] == set_of_four[2] == set_of_four[3]:
            print(
                f"Winning {direction} starting at row {r+1} column {c+1}: {set_of_four}"
            )
            return True, set_of_four[0]
    return False, None


def check_board(surface, board):
    for check in [check_rows, check_cols, check_right_diag, check_left_diag]:
        result, winning_cells, winner = check(board)
        if result:
            draw_winning_board(surface, board, winning_cells)
            font = pygame.font.SysFont("helvetica", 30)
            if winner == 1:
                label = font.render("Red Player Wins!", 1, (255, 255, 255))
            else:
                label = font.render("Yellow Player Wins!", 1, (255, 255, 255))
            label_x = (screen_width - label.get_width()) // 2
            label_y = 20
            surface.blit(label, (label_x, label_y))
            pygame.display.update()

            print("Game Over!/n/n")
            return True


def play_again(surface):
    while True:
        pygame.time.wait(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if 150 <= x <= 210 and 80 <= y <= 110:
                    return True
                if 250 <= x <= 310 and 80 <= y <= 110:
                    return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


def main():
    surface = pygame.display.set_mode((screen_width, screen_height))
    player = 1
    run = True
    board = init()
    draw_board(surface, board)
    while run:
        col = get_move(surface, board, player)

        # try:
        #     move = input(f'Move for player {player}: ')
        #     if move == 'q':
        #         exit()
        #     col = int(move)
        #     assert 0 <= col <= 6
        # except:
        #     continue
        board, valid_move = place_piece(player, col, board)
        if valid_move:
            draw_board(surface, board)
            if check_board(surface, board):
                run = False
                font = pygame.font.SysFont("helvetica", 20)
                label = font.render("Play again?", 1, (0, 255, 255))
                label_x = 30
                label_y = 80
                surface.blit(label, (label_x, label_y))
                pygame.draw.rect(
                    surface, (0, 255, 0), (150, 80, 60, 30), border_radius=4
                )
                label = font.render("Yes", 1, (0, 0, 0))
                label_x = 160
                label_y = 80
                surface.blit(label, (label_x, label_y))
                pygame.draw.rect(
                    surface, (255, 0, 0), (250, 80, 60, 30), border_radius=4
                )
                label = font.render("No", 1, (255, 255, 255))
                label_x = 260
                label_y = 80
                surface.blit(label, (label_x, label_y))
                pygame.display.update()
                replay = play_again(surface)
            if player == 1:
                player = 2
            else:
                player = 1
        pprint(board)
    return replay


replay = True
while replay:
    replay = main()
pygame.display.quit()
