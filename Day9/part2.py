nots = [[0,0] for _ in range(10)]
s = set()
s.add((0,0))

def update(h, t, is_tail):
    x = abs(h[0]-t[0])
    y = abs(h[1]-t[1])

    dx = -1 if h[0] < t[0] else 1
    dy = -1 if h[1] < t[1] else 1
    if x + y >= 3:
        t[0]+=dx
        t[1]+=dy
    elif x == 2:
        t[0]+=dx
    elif y == 2:
        t[1]+=dy
    if is_tail:
        s.add((t[0], t[1]))

def make_move(move):
    dir, amt = move
    # print(dir, amt)
    if dir == 'R':
        for _ in range(amt):
            h = nots[0]
            h[0] += 1
            for i in range(9):
                update(nots[i], nots[i+1], i == 8)
    elif dir == 'L':
        for _ in range(amt):
            h = nots[0]
            h[0] -= 1
            for i in range(9):
                update(nots[i], nots[i+1], i == 8)
            
    elif dir == 'D':
        for _ in range(amt):
            h = nots[0]
            h[1] -= 1
            for i in range(9):
                update(nots[i], nots[i+1], i == 8)
    else:
        for _ in range(amt):
            h = nots[0]
            h[1] += 1
            for i in range(9):
                update(nots[i], nots[i+1], i == 8)

with open('input.txt', 'r') as f:
    lines = f.readlines()
    moves = []
    for line in lines:
        line = line.strip('\n').split(' ')
        move = (line[0], int(line[1]))
        moves.append(move)
    for move in moves:
        make_move(move)
    print(len(s))
    


