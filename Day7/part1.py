# have a Dir that has 2 fields - list of files + list of dirs 
class Dir:
    def __init__(self, parent=None):
        self.files = [] # list of int = file size 
        self.dirs = {} # name -> dir obj
        self.parent = parent # Dir object parent
    def add_dir(self, name, dir):
        self.dirs[name] = dir
    def add_file(self, file):
        self.files.append(file)

def build_graph(lines):
    base = Dir()
    curr = base
    i = 0
    while i < len(lines):
        line = lines[i]
        args = line.split(' ')
        if args[1] == 'ls':
            i += 1
            args = lines[i].split(' ')
            while args[0] != '$':
                if args[0] == 'dir':
                    new = Dir(curr)
                    curr.add_dir(args[1], new)
                else:
                    curr.add_file(int(args[0]))
                i += 1
                if i == len(lines):
                    break
                args = lines[i].split(' ')
        else:
            if args[2] == '/':
                curr = base
            elif args[2] == '..':
                curr = curr.parent
            else:
                curr = curr.dirs[args[2]]
            i += 1
    return base

def graph_size(base, base_name, total, sizes): 
    size = sum(base.files)
    for name in base.dirs:
        size += graph_size(base.dirs[name], name, total, sizes)
    if size <= 100_000:
        # print(base_name, 'adding to total', size)
        total[0] += size
    sizes.append(size)
    return size

with open('input.txt', 'r') as f:
    lines = [line.strip('\n') for line in f.readlines()[1:]]
    base = build_graph(lines)
    total = [0]
    sizes = []
    size = graph_size(base, 'base', total, sizes)
    # print(total[0]) # part 1 ans
    need_to_remove = 30_000_000 - (70_000_000 - size)
    vals = sorted(sizes)
    for v in vals:
        if v >= need_to_remove:
            print(v)
            break