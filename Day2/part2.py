# left - ABC = RPS
# right - XYZ = LDW
# score - 123 = RPS (your pick)
# score - 036 = LDW (outcome)

outcome = {'X': 0, 'Y': 3, 'Z': 6}
win = {'A': 'C', 'B': 'A', 'C': 'B'}
choice = {'A': 1, 'B': 2, 'C': 3}
lose = {'C': 'A', 'A': 'B', 'B': 'C'}

def score(opp, res):
    s = outcome[res]
    if res == 'X':
        s += choice[win[opp]]
    elif res == 'Y':
        s += choice[opp]
    else:
        s += choice[lose[opp]]
    print(opp, res, s)
    return s

with open('test.txt', 'r') as f:
    res = 0
    for line in f.readlines():
        line = line.strip('\n').split(' ')
        opp, pick = line[0], line[1]
        res += score(opp, pick)
    print(res)