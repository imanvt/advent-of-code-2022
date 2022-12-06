
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        for i in range(len(line)):
            s = set(line[i:i+14])
            if len(s) == 14:
                print(i+14)
                break

