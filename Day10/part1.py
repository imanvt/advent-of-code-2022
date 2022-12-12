ans = []
total = [0]
def record(x, c):
    if c % 40 == 20:
        ans.append(x)
        total[0] += x*c

def process_signals(signals):
    x = 1
    c = 0
    for s in signals:
        c += 1
        record(x, c)
        if len(s) == 2:
            amt = int(s[1])
            c += 1
            record(x,c)
            x += amt

with open('input.txt', 'r') as f:
    lines = f.readlines()
    signals = []
    for line in lines:
        line = line.strip('\n')
        signals.append(line.split(' '))
    process_signals(signals)
    print(ans)
    print(total)




