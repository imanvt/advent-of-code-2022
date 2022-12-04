with open('input.txt', 'r') as f:
    max_elf = 0
    curr_elf = 0
    for line in f.readlines():
        if line == '\n':
            max_elf = max(curr_elf, max_elf)
            curr_elf = 0
        else:
            curr_elf += int(line)
    print(max_elf)