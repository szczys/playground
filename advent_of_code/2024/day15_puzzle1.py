from copy import deepcopy
from typing import List, Tuple

class Map:
    WALL=0
    BOX=1
    ROBOT=2

    UP=( 0,-1)
    RT=( 1, 0)
    DN=( 0, 1)
    LT=(-1, 0)

    class Obstacle:
        def __init__(self, x: int, y: int, kind: int, fixed: bool = False):
            self.x = x
            self.y = y
            self.kind = kind
            self.fixed = fixed

        def __str__(self):
            return f"({self.x}, {self.y})"

        def __eq__(self, r):
            return self.x == r.x and self.y == r.y

        def __hash__(self):
            return hash((self.x, self.y))

        def try_move(self, dir: Tuple, obstacles: List) -> bool:
            if self.fixed:
                return False

            can_move = False
            move_to = Map.Obstacle(self.x + dir[0], self.y + dir[1], Map.BOX)

            try:
                neighbor = obstacles[obstacles.index(move_to)]
                can_move = neighbor.try_move(dir, obstacles)
            except:
                can_move = True

            if can_move:
                self.x = move_to.x
                self.y = move_to.y
                return True

            return False

    def __init__(self, f_name):
        self.filename = f_name
        with open(self.filename, "r") as f:
            self.rows = f.read().splitlines()

        self.map = list()
        for r in self.rows:
            if r == "":
                break
            self.map.append([x for x in r])

        self.size_x = len(self.map[0])
        self.size_y = len(self.map)

        self.obstacles = list()
        for y, r in enumerate(self.map):
            for x, c in enumerate([i for i in r]):
                if c == "#":
                    self.obstacles.append(self.Obstacle(x, y, self.WALL, True))
                elif c == "O":
                    self.obstacles.append(self.Obstacle(x, y, self.BOX))
                elif c == "@":
                    self.obstacles.append(self.Obstacle(x, y, self.ROBOT))

        self.commands = list()
        for r in self.rows:
            if r == "" or r[0] == "#":
                continue

            for i in r:
                if i == '^':
                    self.commands.append(self.UP)
                elif i == '>':
                    self.commands.append(self.RT)
                elif i == 'v':
                    self.commands.append(self.DN)
                elif i == '<':
                    self.commands.append(self.LT)

    def print_map(self, obstacles: List):
        display = list()
        display_row = ["."] * self.size_y
        for _ in range(self.size_y):
            display.append(deepcopy(display_row))

        for o in obstacles:
            if o.kind == self.WALL:
                display[o.y][o.x] = "#"
            if o.kind == self.BOX:
                display[o.y][o.x] = "O"
            if o.kind == self.ROBOT:
                display[o.y][o.x] = "@"

        print()
        for m in display:
            print(''.join(m))

    def move_robot(self, obstacles: List, commands: List):
        robot = None
        for o in obstacles:
            if o.kind == self.ROBOT:
                robot = o

        if robot is None:
            return robot

        for c in commands:
            robot.try_move(c, obstacles)

        self.print_map(obstacles)

    def calc_box_gps(self, obstacles):
        gps_totals = 0

        for o in obstacles:
            if o.kind == self.BOX:
                gps_totals += (100 * o.y) + o.x

        return gps_totals

m = Map("day15_input1.txt")
m.move_robot(m.obstacles, m.commands)
print("Box GPS Totals:", m.calc_box_gps(m.obstacles))

