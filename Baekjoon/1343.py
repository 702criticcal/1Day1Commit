board = list(input())

for i in range(len(board)):
    if board[i:i + 4] == ['X', 'X', 'X', 'X']:
        board[i:i + 4] = ['A', 'A', 'A', 'A']
    if board[i:i + 2] == ['X', 'X']:
        board[i:i + 2] = ['B', 'B']

if 'X' in board:
    print(-1)
else:
    print(''.join(board))
