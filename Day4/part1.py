def contains(l, r):
    return int(l[0]) >= int(r[0]) and int(l[1]) <= int(r[1])

with open('input.txt', 'r') as f:
    ans = 0
    for line in f.readlines():
        line = line.strip('\n').split(',')
        l, r = line[0], line[1]
        l = l.split('-')
        r = r.split('-')
        if contains(l,r) or contains(r,l):
            ans += 1
    
    print(ans)
