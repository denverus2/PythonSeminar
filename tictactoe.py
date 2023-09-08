import random

def print_board(board):
  print("\033[H\033[J") 
  for row in board:
    print('|' + '|'.join(row) + '|')

def make_move(board, x, y, player):
    if board[x][y] != ' ':
        return False
    board[x][y] = player
    return True

def has_winner(board):
    # Проверяем строки
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # Проверяем столбцы
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Проверяем диагонали
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    # Ничья
    if all(all(row[i] != ' ' for i in range(3)) for row in board):
        return 'Ничья'

    # Игра продолжается
    return None

def tictactoe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)
        winner = has_winner(board)
        if winner is not None:
            if winner == 'Ничья':
                print('Игра окончена! Ничья!')
            else:
                print(f'Игра окончена! Победитель: {winner}')
            return

        if player == 'X':
            x = int(input('Введите номер строки (0, 1 или 2): '))
            y = int(input('Введите номер столбца (0, 1 или 2): '))
            if not make_move(board, x, y, player):
                print('Эта клетка уже занята! Попробуйте еще раз.')
                continue
        else:
            x, y = random.choice([(x,y) for x in range(3) for y in range(3) if board[x][y] == ' '])
            make_move(board, x, y, player)

        player = 'X' if player == 'O' else 'O'

tictactoe()
