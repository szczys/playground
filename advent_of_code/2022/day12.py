class Pt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.depth = 0

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Node:
    def __init__(self, x, y, elevation):
        self.x = x
        self.y = y
        if elevation == 'S':
            self.elevation = ord('a')
        elif elevation == 'E':
            self.elevation = ord('z')
        else:
            self.elevation = ord(elevation)

    def get_elevation(self):
        return self.elevation

    def print(self):
        print(self.x, self.y, self.elevation, self.neighbors)

class Maze:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            self.rows = f.read().splitlines()
        self.h = len(self.rows)
        self.w = len(self.rows[0])
        self.grid = dict()
        self.queue = list()
        self.visited = list()

        for y,r in enumerate(self.rows):
            self.grid[y] = dict()
            for x,h in enumerate(r):
                if h == 'S':
                    self.start = Pt(x, y)
                    print("Found Start:", self.start)
                elif h == 'E':
                    self.end = Pt(x, y)
                    print("Found End:", self.end)

                self.grid[y][x] = Node(x, y, h)

    def get_grid(self):
        return self.grid

    def get_node(self, point):
        return self.grid[point.y][point.x]

    def get_el(self, point):
        return self.grid[point.y][point.x].get_elevation()

    def get_neighbors(self, p):
        points = list()
        n = self.get_node(p)
        target_el = n.get_elevation()
        if p.x > 0:
            points.append(Pt(p.x-1, p.y))
        if p.x < self.w - 1:
            points.append(Pt(p.x+1, p.y))
        if p.y > 0:
            points.append(Pt(p.x, p.y-1))
        if p.y < self.h - 1:
            points.append(Pt(p.x, p.y+1))

        valid = list()
        for i in points:
            if self.get_el(i) < target_el+2:
                valid.append(i)

        return valid

    def bfs(self):
        self.visited = [self.start]
        self.queue = [self.start]

        while self.queue:
            current_p = self.queue.pop(0)
            neighbors = self.get_neighbors(current_p)
            for n in neighbors:
                if n not in self.visited:
                    n.depth = current_p.depth+1
                    if n == self.end:
                        print("Found end:", n.depth)
                        return
                    self.visited.append(n)
                    self.queue.append(n)
        print("No solution found")
        print()

# m = Maze("day12_test.txt")
m = Maze("day12_input.txt")
m.bfs()

