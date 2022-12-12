from itertools import product

class Snake:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            self.moves = [[i.split(" ")[0], int(i.split(" ")[1])] for i in f.read().splitlines()]
        self.hx = 0
        self.hy = 0
        self.tx = 0
        self.ty = 0

        self.tail_locs = [[0,0]]

    lut = { 'R' : [1, 0], 'D' : [0, -1], 'L' : [-1, 0], 'U' : [0, 1] }

    def move_head(self, dir):
        self.hx += self.lut[dir][0]
        self.hy += self.lut[dir][1]

    def must_move(self):
        x = list(range(self.tx-1, self.tx+2))
        y = list(range(self.ty-1, self.ty+2))
        if (self.hx, self.hy) in product(x,y):
            return False
        return True

    def move_tail(self):
        if self.must_move():
            if self.hx > self.tx:
                self.tx += 1
            if self.hx < self.tx:
                self.tx -= 1
            if self.hy > self.ty:
                self.ty += 1
            if self.hy < self.ty:
                self.ty -= 1
            if [self.tx, self.ty] not in self.tail_locs:
                self.tail_locs.append([self.tx, self.ty])

    def process_moves(self):
        for move in self.moves:
            for i in range(move[1]):
                self.move_head(move[0])
                self.move_tail()
        return len(self.tail_locs)

s = Snake("day9_input.txt")
# s = Snake("day9_test.txt")
print("Answer 1:", s.process_moves())
