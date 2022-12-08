def check(grid, i, j):
    total = 1
    if i == 0 or i == len(grid)-1 or j == 0 or j == len(grid[0])-1:
        return 0
    
    row = grid[i]
    tree = grid[i][j]

    left = 0
    for t in row[:j][::-1]:
        left += 1
        if t >= tree:
            break
    total *= left

    right = 0
    for t in row[j+1:]:
        right += 1
        if t >= tree:
            break
    total *= right

    down = 0
    up = 0
    col = [grid[k][j] for k in range(len(grid))]
    for t in col[:i][::-1]:
        up += 1
        if t >= tree:
            break
    total *= up

    for t in col[i+1:]:
        down += 1
        if t >= tree:
            break
    total *= down

    # print(left, right, up, down, end='->')
    return total

with open('input.txt', 'r') as f:
    lines = f.readlines()
    grid = []
    for line in lines:
        line = line.strip('\n')
        trees = []
        for c in line:
            trees.append(int(c))
        grid.append(trees)
    score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            curr = check(grid, i, j)
            # if curr != 0: print(i, j, curr)
            score = max(score, curr)
    print(score)

