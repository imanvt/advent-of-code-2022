import sys
import os

python_template = '''
with open('test.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip('\\n')
'''

day = int(sys.argv[1])
dir = f'./Day{day}'
os.mkdir(dir)
open(dir+'/input.txt', 'x')
open(dir+'/test.txt', 'x')
f = open(dir+'/part1.py', 'w')
f.write(python_template)
f.close()
f = open(dir+'/part2.py', 'w')
f.write(python_template)
f.close()




