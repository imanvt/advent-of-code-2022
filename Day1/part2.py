import heapq

def insert(heap, elf):
    # negate elf value since min heap
    heapq.heappush(heap, -elf)

with open('input.txt', 'r') as f:
    heap = []
    curr_elf = 0
    for line in f.readlines():
        if line == '\n':
            insert(heap, curr_elf)
            curr_elf = 0
        else:
            curr_elf += int(line)
    heapq.heapify(heap)
    top_three = heapq.nsmallest(3, heap)
    print(-sum(top_three))

