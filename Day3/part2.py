def priority(c):
    if ord(c) < ord('a'):
        return ord(c) - ord('A') + 27
    return ord(c) - ord('a') + 1

def find_item(a,b,c):
    a = set(a)
    b = set(b)
    c = set(c)
    return list(a.intersection(b).intersection(c))[0]

with open('input.txt', 'r') as f:
    ans = 0
    lines = f.readlines()
    i = 0
    while i < len(lines):
        a = lines[i].strip('\n')
        b = lines[i+1].strip('\n')
        c = lines[i+2].strip('\n')
        i += 3
        item = find_item(a,b,c)
        ans += priority(item)
    print(ans)