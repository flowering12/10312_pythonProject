import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    clear_screen()
    for row in board:
        print(' '.join(map(str, row)))
    print()

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

def play_game():
    size = 4
    board = initialize_board(size)
    directions = ['left', 'right', 'up', 'down']

    while not is_game_over(board):
        print_board(board)
        direction = input("Enter a direction (left, right, up, down): ").lower()

        if direction in directions:
            board = move(board, direction)
            add_new_tile(board)
        else:
            print("Invalid direction. Please enter left, right, up, or down.")

    print_board(board)
    print("Game over!")

if __name__ == "__main__":
    play_game()