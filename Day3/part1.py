def priority(c):
    if ord(c) < ord('a'):
        return ord(c) - ord('A') + 27
    return ord(c) - ord('a') + 1

def find_item(line):
    split = len(line)//2
    a = set(line[:split])
    b = set(line[split:])
    return list(a.intersection(b))[0]
    
with open('input.txt', 'r') as f:
    ans = 0
    for line in f.readlines():
        c = find_item(line.strip('\n'))
        ans += priority(c)
    print(ans)