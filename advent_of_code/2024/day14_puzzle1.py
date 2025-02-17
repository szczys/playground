from re import X
from typing import List
from copy import deepcopy
import numpy

class Map:
    class Robot:
        def __init__(self, x: int, y: int, v_x: int, v_y: int):
            self.x = x
            self.y = y
            self.v_x = v_x
            self.v_y = v_y

        def __str__(self):
            return f"({self.x}, {self.y}) ({self.v_x}, {self.v_y})"

        def __eq__(self, r):
            return self.x == r.x and self.y == r.y

        def __hash__(self):
            return hash((self.x, self.y))

    def __init__(self, f_name):
        self.filename = f_name
        with open(self.filename, "r") as f:
            self.rows = f.read().splitlines()

        self.robots = list()

        for r in self.rows:
            values = r.split(" ")
            coords = values[0].split('=')[1].split(',')
            velocities = values[1].split('=')[1].split(',')
            self.robots.append(self.Robot(int(coords[0]),
                                          int(coords[1]),
                                          int(velocities[0]),
                                          int(velocities[1])
                                          )
                               )

    def calculate_robots(self, robots: List, times: int, size_x: int, size_y: int):
        quad_totals = [0,0,0,0]
        middle_x = int(size_x / 2)
        middle_y = int(size_y / 2)

        for r in robots:
            r.x = (r.x + (r.v_x * times)) % size_x
            r.y = (r.y + (r.v_y * times)) % size_y

            if r.x < 0:
                r.x = size_x + r.x
                r.y = size_y + r.y

            if r.x < middle_x and r.y < middle_y:
                quad_totals[0] += 1
            if r.x > middle_x and r.y < middle_y:
                quad_totals[1] += 1
            if r.x < middle_x and r.y > middle_y:
                quad_totals[2] += 1
            if r.x > middle_x and r.y > middle_y:
                quad_totals[3] += 1

        return numpy.prod(quad_totals)

    def find_easter_egg(self, robots: List, percent: int, size_x: int, size_y: int):
        max_pct = 0

        outline = list()
        center_x = int(size_x / 2)
        increment = (center_x) / (size_y - 1)

        for y in range(size_y):
            x = int(y * increment)
            for j in range(x, size_x - x):
                inverted_y = size_y - 1 - y
                outline.append(self.Robot(j, inverted_y, 0, 0))

        for y in range(size_y):
            outstr = ""
            for x in range(size_x):
                if self.Robot(x,y,0,0) in outline:
                    outstr += "X"
                else:
                    outstr += "."
            print(outstr)

        iterations = 1
        while(True):
            if iterations % 10000 == 0:
                print("Iterations:", iterations)
            center_robots = 0
            for r in robots:
                r.x = (r.x + (r.v_x)) % size_x
                r.y = (r.y + (r.v_y)) % size_y

                if r.x < 0:
                    r.x = size_x + r.x
                    r.y = size_y + r.y

            center_robots = len(list(set(outline).intersection(robots)))
            if center_robots > max_pct:
                max_pct = center_robots
                inside_pct = (center_robots * 100) / len(outline)

                tree = list()
                for y in range(size_y):
                    branch = ['.'] * size_x
                    tree.append(branch)

                for r in robots:
                    tree[r.y][r.x] = "X"
                for b in tree:
                    print(''.join(b))

                print("Iter: {0} {1:.2f}%".format(iterations, inside_pct))

            iterations += 1




m = Map("day14_input1.txt")
newbots = deepcopy(m.robots)
print(m.calculate_robots(newbots, 100, 101, 103))
easter_egg = deepcopy(m.robots)
print(m.find_easter_egg(easter_egg, 60, 101, 103))
