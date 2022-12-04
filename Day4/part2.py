def overlap(l, r):
    return int(r[0]) <= int(l[0]) <= int(r[1])

with open('input.txt', 'r') as f:
    ans = 0
    for line in f.readlines():
        line = line.strip('\n').split(',')
        l, r = line[0], line[1]
        l = l.split('-')
        r = r.split('-')
        if overlap(l,r) or overlap(r,l):
            ans += 1
    
    print(ans)

