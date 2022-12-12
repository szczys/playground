from itertools import product

class Pt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Snake:
    def __init__(self, f_name, nodes=2):
        with open(f_name, "r") as f:
            self.moves = [[i.split(" ")[0], int(i.split(" ")[1])] for i in f.read().splitlines()]
        self.knots = list()
        for k in range(nodes):
            self.knots.append(Pt(0,0))
        self.tail_locs = [[0,0]]

    lut = { 'R' : [1, 0], 'D' : [0, -1], 'L' : [-1, 0], 'U' : [0, 1] }

    def move_head(self, dir, head):
        head.x += self.lut[dir][0]
        head.y += self.lut[dir][1]

    def must_move(self, head, tail):
        x = list(range(tail.x-1, tail.x+2))
        y = list(range(tail.y-1, tail.y+2))
        if (head.x, head.y) in product(x,y):
            return False
        return True

    def move_tail(self, head, tail):
        if self.must_move(head, tail):
            if head.x > tail.x:
                tail.x += 1
            if head.x < tail.x:
                tail.x -= 1
            if head.y > tail.y:
                tail.y += 1
            if head.y < tail.y:
                tail.y -= 1

    def process_moves(self):
        for move in self.moves:
            for i in range(move[1]):
                for k in range(len(self.knots)):
                    if k == 0:
                        self.move_head(move[0], self.knots[0])
                    else:
                        self.move_tail(self.knots[k-1], self.knots[k])
                if [self.knots[-1].x, self.knots[-1].y] not in self.tail_locs:
                    self.tail_locs.append([self.knots[-1].x, self.knots[-1].y])
        return len(self.tail_locs)

s = Snake("day9_input.txt")
# s = Snake("day9_test.txt")
print("Answer 1:", s.process_moves())
t = Snake("day9_input.txt", 10)
# t = snake("day9_test2.txt", 10)
print("Answer 2:", t.process_moves())
