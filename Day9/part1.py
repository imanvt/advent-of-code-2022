h = [0, 0]
t = [0, 0]
s = set()
s.add((0,0))

def update(h, t):
    x = abs(h[0]-t[0])
    y = abs(h[1]-t[1])

    dx = -1 if h[0] < t[0] else 1
    dy = -1 if h[1] < t[1] else 1

    if x + y == 3:
        t[0]+=dx
        t[1]+=dy
    elif x == 2:
        t[0]+=dx
    elif y == 2:
        t[1]+=dy
    # print(h, t)
    s.add((t[0], t[1]))

def make_move(move):
    dir, amt = move
    if dir == 'R':
        for _ in range(amt):
            h[0] += 1
            update(h, t)
    elif dir == 'L':
        for _ in range(amt):
            h[0] -= 1
            update(h, t)
    elif dir == 'D':
        for _ in range(amt):
            h[1] -= 1
            update(h, t)
    else:
        for _ in range(amt):
            h[1] += 1
            update(h, t)

with open('input.txt', 'r') as f:
    lines = f.readlines()
    moves = []
    for line in lines:
        line = line.strip('\n').split(' ')
        move = (line[0], int(line[1]))
        moves.append(move)
    for move in moves:
        make_move(move)
        # print(h, t)
    print(len(s))
    


