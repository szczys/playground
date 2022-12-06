import queue

def get_fresh_stacks():
    return [None, queue.LifoQueue(),queue.LifoQueue(),queue.LifoQueue(),queue.LifoQueue(),queue.LifoQueue(),queue.LifoQueue(),queue.LifoQueue(),queue.LifoQueue(),queue.LifoQueue()]

stacks = get_fresh_stacks()

def get_input():
    with open("day5_input.txt", "r") as f:
        return f.read().splitlines()

def load_queues(l):
    col_limit = len(l[0])
    row_limit = 0
    while (l[row_limit][0] == '['):
        row_limit += 1
    for i in range(row_limit, -1, -1):
        for j, n in enumerate(range(1, col_limit, 4)):
            this_char = l[i][n]
            if this_char != ' ':
                stacks[j+1].put(this_char)

def get_top_boxes():
    outstring = ""
    for i in range(1,10):
        if not stacks[i].empty():
            outstring += stacks[i].get()
    return outstring

def parse_instruction(l):
    inst = l.split(' ')
    return [int(inst[1]), int(inst[3]), int(inst[5])]

def operate(code):
    for i in range(code[0]):
        stacks[code[2]].put(stacks[code[1]].get())

def process_moves(l):
    for i in l:
        if not i.startswith("move"):
            continue
        operate(parse_instruction(i))

def operate_multiple_boxes(code):
    liftqueue = queue.LifoQueue()
    for i in range(code[0]):
        liftqueue.put(stacks[code[1]].get())
    while not liftqueue.empty():
        stacks[code[2]].put(liftqueue.get())

def process_moves_9001(l):
    for i in l:
        if not i.startswith("move"):
            continue
        operate_multiple_boxes(parse_instruction(i))

lines = get_input()
load_queues(lines)
process_moves(lines)
print("Cranemover 9000:", get_top_boxes())

lines = get_input()
stacks = get_fresh_stacks()
load_queues(lines)
process_moves_9001(lines)
print("Cranemover 9001:", get_top_boxes())

