from copy import deepcopy
from typing import List, Tuple

class Map:
    WALL=0
    BOX=1
    ROBOT=2
    BOX_LEFT=3
    BOX_RIGHT=4

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
            return f"({self.x}, {self.y}), kind: {self.kind} fixed: {self.fixed}"

        def __eq__(self, r):
            return self.x == r.x and self.y == r.y

        def __hash__(self):
            return hash((self.x, self.y))

        def try_move(self, dir: Tuple, obstacles: List, dry_run: bool = False) -> bool:
            if self.fixed:
                return False

            can_move = False
            move_to = Map.Obstacle(self.x + dir[0], self.y + dir[1], Map.BOX)

            try:
                neighbor = obstacles[obstacles.index(move_to)]

                if ((neighbor.kind == Map.BOX_LEFT or neighbor.kind == Map.BOX_RIGHT) and
                    (dir == Map.UP or dir == Map.DN)):

                    if neighbor.kind == Map.BOX_LEFT:
                        twin_x = neighbor.x + 1
                    else:
                        twin_x = neighbor.x - 1

                    twin = obstacles[obstacles.index(Map.Obstacle(twin_x, neighbor.y, Map.BOX))]

                    neighbor_test_move = neighbor.try_move(dir, obstacles, dry_run = dry_run)
                    twin_test_move = twin.try_move(dir, obstacles, dry_run =dry_run)

                    if neighbor_test_move and twin_test_move:
                        can_move = True
                    else:
                        can_move = False

                else:
                    can_move = neighbor.try_move(dir, obstacles, dry_run = dry_run)
            except:
                can_move = True

            if can_move:
                if not dry_run:
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

        self.obstacles_double = list()
        for y, r in enumerate(self.map):
            for x, c in enumerate([i for i in r]):
                if c == "#":
                    self.obstacles_double.append(self.Obstacle(x * 2, y, self.WALL, True))
                    self.obstacles_double.append(self.Obstacle((x * 2) + 1, y, self.WALL, True))
                elif c == "O":
                    self.obstacles_double.append(self.Obstacle(x * 2, y, self.BOX_LEFT))
                    self.obstacles_double.append(self.Obstacle((x * 2) + 1, y, self.BOX_RIGHT))
                elif c == "@":
                    self.obstacles_double.append(self.Obstacle(x * 2, y, self.ROBOT))

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

    def print_map(self, obstacles: List, double: bool = False):
        if double:
            multiplier = 2
        else:
            multiplier = 1

        display = list()
        display_row = ["."] * (self.size_y * multiplier)
        for _ in range(self.size_y):
            display.append(deepcopy(display_row))

        for o in obstacles:
            if o.kind == self.WALL:
                display[o.y][o.x] = "#"
            if o.kind == self.BOX:
                display[o.y][o.x] = "O"
            if o.kind == self.ROBOT:
                display[o.y][o.x] = "@"
            if o.kind == self.BOX_LEFT:
                display[o.y][o.x] = "["
            if o.kind == self.BOX_RIGHT:
                display[o.y][o.x] = "]"

        print()
        for m in display:
            print(''.join(m))

    def move_robot(self, obstacles: List, commands: List, double: bool = False):
        robot = None
        for o in obstacles:
            if o.kind == self.ROBOT:
                robot = o

        if robot is None:
            return robot

        for c in commands:
            if robot.try_move(c, obstacles, dry_run = True):
                robot.try_move(c, obstacles)

        self.print_map(obstacles, double)

    def calc_box_gps(self, obstacles):
        gps_totals = 0

        for o in obstacles:
            if o.kind == self.BOX:
                gps_totals += (100 * o.y) + o.x
            if o.kind == self.BOX_LEFT:
                gps_totals += (100 * o.y) + o.x

        return gps_totals

m = Map("day15_input1.txt")
m.move_robot(m.obstacles, m.commands)
print("Box GPS Totals:", m.calc_box_gps(m.obstacles))

m.move_robot(m.obstacles_double, m.commands, True)
print("Double Box GPS Totals:", m.calc_box_gps(m.obstacles_double))
