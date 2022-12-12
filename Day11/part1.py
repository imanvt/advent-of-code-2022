class Monkey:
    def __init__(self, items, op, test):
        self.items = items # list of items
        self.op = op # arr -> [op, var], e.g. [*, 19]
        self.test = test # arr -> [x, true, false], x = divisible by

def calc(item, op):
    if op[0] == '*':
        if op[1] == 'old':
            return item**2
        return item * int(op[1])
    # + case
    return item + int(op[1])

def play_round(monkeys, counts):
    for j, m in enumerate(monkeys):
        counts[j] += len(m.items)
        for i in m.items:
            new = calc(i, m.op)
            new = new//3
            x = m.test[0]
            t, f = m.test[1], m.test[2]
            if new % x == 0:
                monkeys[t].items.append(new)
            else:
                monkeys[f].items.append(new)
        m.items = []

with open('input.txt', 'r') as f:
    lines = [line.strip('\n') for line in f.readlines()]
    i = 1
    monkeys = []
    counts = []
    while i < len(lines):
        a = lines[i].split(':')
        b = a[1].split(',')
        items = [int(item[1:]) for item in b]

        c = lines[i+1].split('=')
        d = c[1].split(' ')
        op = d[-2:]
       
        e = int(lines[i+2].split(' ')[-1]) # x
        f = int(lines[i+3].split(' ')[-1]) # true
        g = int(lines[i+4].split(' ')[-1]) # false
        test = [e,f,g]

        monkeys.append(Monkey(items, op, test))
        counts.append(0)
        i += 7

    for _ in range(20):
        play_round(monkeys, counts)
    
    counts.sort()
    print(counts[-1] * counts[-2])