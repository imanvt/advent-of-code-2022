from tqdm import tqdm

class Monkey:
    def __init__(self, items, op, test):
        self.items = items # list of items
        self.op = op # arr -> [op, var], e.g. [*, 19]
        self.test = test # arr -> [x, true, false], x = divisible by

def calc(item, op):
    if op[0] == '*':
        if op[1] == 'old':
            return item*item
        return item * int(op[1])
    # + case
    return item + int(op[1])

def apply(operation, old):
    return eval(operation)

wtf = 17 * 3 * 19 * 7 * 2 * 5 * 11 * 13

def play_round(monkeys, counts):
    for j, m in enumerate(monkeys):
        counts[j] += len(m.items)
        for i in m.items:
            i = apply(m.op, i) % wtf # crazy optimization trick...
            x = m.test[0]
            t, f = m.test[1], m.test[2]
            if i % x == 0:
                monkeys[t].items.append(i)
            else:
                monkeys[f].items.append(i)
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

        op = lines[i+1].split(' = ')[1]

        e = int(lines[i+2].split(' ')[-1]) # x
        f = int(lines[i+3].split(' ')[-1]) # true
        g = int(lines[i+4].split(' ')[-1]) # false
        test = [e,f,g]

        monkeys.append(Monkey(items, op, test))
        counts.append(0)
        i += 7

for _ in tqdm(range(10_000)):
    play_round(monkeys, counts)

counts.sort()
print(counts[-1] * counts[-2])