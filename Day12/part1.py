from collections import deque

def verify(grid, i, j, letter):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return False
    diff = ord(grid[i][j]) - ord(letter)
    return diff <= 1 or letter == 'S'
    
def bfs(grid, start):
    i, j = start
    q = deque([(i, j, [])])
    vis = set()
    vis.add((i,j))
    curr = 0
    while q:
        # print(curr)
        size = len(q)
        for _ in range(size):
            i, j, path = q.popleft()
            if grid[i][j] == 'E':
                return curr
            # print(i, j, grid[i][j], path)
            if verify(grid, i+1, j, grid[i][j]) and (i+1, j) not in vis:
                vis.add((i+1,j))
                q.append((i+1, j, path+[(i,j, grid[i][j])]))

            if verify(grid, i-1, j, grid[i][j]) and (i-1, j) not in vis:
                vis.add((i-1,j))
                q.append((i-1, j, path+[(i,j, grid[i][j])]))

            if verify(grid, i, j+1, grid[i][j]) and (i, j+1) not in vis:
                vis.add((i,j+1))
                q.append((i, j+1, path+[(i,j, grid[i][j])]))

            if verify(grid, i, j-1, grid[i][j]) and (i, j-1) not in vis:
                vis.add((i,j-1))
                q.append((i, j-1, path+[(i,j, grid[i][j])]))
        curr += 1
    return None

with open('input.txt', 'r') as f:
    lines = f.readlines()
    grid = []
    start = (1,1)
    for line in lines:
        line = line.strip('\n')
        grid.append(list(line))
        i = line.find('S')
        if i != -1:
            start = (len(grid)-1, i)
    print(bfs(grid, start))