import random
import curses

def initialize_board(size):
    board = [[0] * size for _ in range(size)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_cells = [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 2 if random.random() < 0.9 else 4

def print_board(win, board):
    win.clear()
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            win.addstr(i * 2, j * 5, f'{val:^5}')
    win.refresh()

def move(board, direction):
    size = len(board)
    new_board = [row[:] for row in board]

    for i in range(size):
        row = board[i]
        row = [value for value in row if value != 0]
        for j in range(len(row) - 1):
            if row[j] == row[j + 1]:
                row[j] *= 2
                row[j + 1] = 0

        row = [value for value in row if value != 0]
        row = [0] * (size - len(row)) + row
        new_board[i] = row

    if direction == 'left':
        return new_board
    elif direction == 'right':
        return [row[::-1] for row in new_board]
    elif direction == 'up':
        transposed_board = [list(x) for x in zip(*new_board)]
        return [list(x) for x in zip(*transposed_board)]
    elif direction == 'down':
        transposed_board = [list(x) for x in zip(*new_board)]
        return [row[::-1] for row in transposed_board]

def is_game_over(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return False
            if i < len(board) - 1 and board[i][j] == board[i + 1][j]:
                return False
            if j < len(board[0]) - 1 and board[i][j] == board[i][j + 1]:
                return False
    return True

def play_game(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    size = 4
    board = initialize_board(size)
    add_new_tile(board)
    add_new_tile(board)

    while not is_game_over(board):
        print_board(stdscr, board)
        key = stdscr.getch()

        if key in [curses.KEY_LEFT, ord('a')]:
            board = move(board, 'left')
        elif key in [curses.KEY_RIGHT, ord('d')]:
            board = move(board, 'right')
        elif key in [curses.KEY_UP, ord('w')]:
            board = move(board, 'up')
        elif key in [curses.KEY_DOWN, ord('s')]:
            board = move(board, 'down')

        add_new_tile(board)

    print_board(stdscr, board)
    stdscr.addstr(size * 2, 0, "Game over! Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(play_game)