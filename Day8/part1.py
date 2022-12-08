def check(grid, i, j):
    if i == 0 or i == len(grid)-1 or j == 0 or j == len(grid[0])-1:
        # print('edge', end=' ')
        return True
    row = grid[i]
    left = max(row[:j])
    if grid[i][j] > left:
        return True
    right = max(row[j+1:])
    if grid[i][j] > right:
        return True
    
    up = []
    down = []
    for k in range(len(grid)):
        if k < i:
            up.append(grid[k][j])
        elif k > i:
            down.append(grid[k][j])
    
    upMax = max(up)
    downMax = max(down)

    if grid[i][j] > upMax:
        return True
    if grid[i][j] > downMax:
        return True
    
    return False

with open('input.txt', 'r') as f:
    lines = f.readlines()
    grid = []
    for line in lines:
        line = line.strip('\n')
        trees = list(line)
        grid.append(trees)
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if check(grid, i, j):
                # print(i,j)
                count += 1
    print(count)

