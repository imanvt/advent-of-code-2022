# left - ABC = RPS
# right - XYZ = RPS
# score - 123 = RPS (your pick)
# score - 036 = LDW (outcome)

map = {'X': 'A', 'Y': 'B', 'Z': 'C'}
choice = {'A': 1, 'B': 2, 'C': 3}
win = {'A': 'C', 'B': 'A', 'C': 'B'}

def score(opp, pick):
    pick = map[pick]
    res = choice[pick]
    if pick == opp:
        res += 3
    elif win[pick] == opp:
        res += 6
    return res

with open('input.txt', 'r') as f:
    res = 0
    for line in f.readlines():
        line = line.strip('\n').split(' ')
        opp, pick = line[0], line[1]
        res += score(opp, pick)
    print(res)