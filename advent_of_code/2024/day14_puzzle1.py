from typing import List
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

    def iterate_robots(self, robots: List, times: int, size_x: int, size_y: int):
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

        print(quad_totals)
        return numpy.prod(quad_totals)


m = Map("day14_input1.txt")
print(m.iterate_robots(m.robots, 100, 101, 103))
