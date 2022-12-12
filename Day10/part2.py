board = [['.']*40 for _ in range(6)]

def update_board(x, c):
    c -= 1
    row = c//40
    col = c%40
    if abs(col-x) <= 1:
        board[row][col] = '#'

def process_signals(signals):
    x = 1
    c = 0
    for s in signals:
        c += 1
        update_board(x, c)
        if len(s) == 2:
            amt = int(s[1])
            c += 1
            update_board(x,c)
            x += amt

with open('input.txt', 'r') as f:
    lines = f.readlines()
    signals = []
    for line in lines:
        line = line.strip('\n')
        signals.append(line.split(' '))
    process_signals(signals)
    for r in board:
        for c in r:
            print(c, end='')
        print()