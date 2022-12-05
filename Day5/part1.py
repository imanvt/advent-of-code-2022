from collections import deque

def process(line):
    words = line.split(' ')
    return [int(words[1]), int(words[3]), int(words[5])]

def move(arr, m):
    [N, s, e] = m
    for _ in range(N):
        elem = arr[s-1].popleft()
        arr[e-1].insert(0, elem)



with open('input.txt', 'r') as f:
    N = 9
    Y = 8
    arr = []
    for i in range(N):
        arr.append(deque([]))
    lines = f.readlines()
    for line in lines[:Y]:
        line = line.strip('\n')
        i = 0
        curr = ''
        while i < N*4:
            curr = line[i:i+3]
            if curr != '   ':
                arr[i//4].append(curr[1])
            i += 4
    for line in lines[Y+2:]:
        line = line.strip('\n')
        move(arr, process(line))
    
    # print(arr)
    for q in arr:
        print(q.popleft(), end='')