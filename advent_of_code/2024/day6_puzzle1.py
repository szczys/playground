from typing import List
import re
from copy import deepcopy

class Maze:
    UP=0
    RIGHT=1
    DOWN=2
    LEFT=3

    CONTINUE=0
    OFFGRID=1
    LOOPING=2

    class Point:
        def __init__(self, x: int, y: int, dir: int | None = None):
            self.x = x
            self.y = y
            self.dir = dir

        def __str__(self):
            return(f"<x: {self.x} y: {self.y} dir: {self.dir}>")

        def __eq__(self, p):
            return self.x == p.x and self.y == p.y and self.dir == p.dir

        def copy(self, p):
            self.x = p.x
            self.y = p.y
            self.dir = p.dir

    def __init__(self, f_name):
        self.filename = f_name
        with open(self.filename, "r") as f:
            self.rows = f.read().splitlines()

        self.size_x = len(self.rows[0])
        self.size_y = len(self.rows)

        self.maze = list()
        p = re.compile("[/^<>V]")
        for i, r in enumerate(self.rows):
            self.maze.append([c for c in r])
            y = p.search(r)
            if y:
                self.head = self.Point(y.span()[0], i)
                if y.group(0) == '^':
                    self.dir = self.UP
                if y.group(0) == '>':
                    self.dir = self.RIGHT
                if y.group(0) == 'V':
                    self.dir = self.DOWN
                if y.group(0) == '<':
                    self.dir = self.LEFT

    def mark_and_move(self, path_points: List | None = None) -> int:
        self.maze[self.head.y][self.head.x] = 'X'

        if path_points is not None:
            p = self.Point(self.head.x, self.head.y, self.dir)

            if p in path_points:
                return self.LOOPING
            path_points.append(p)

        if self.dir == self.UP:
            self.head.y -= 1
        elif self.dir == self.RIGHT:
            self.head.x += 1
        elif self.dir == self.DOWN:
            self.head.y += 1
        elif self.dir == self.LEFT:
            self.head.x -= 1

        while(True):
            if (self.head.x >= self.size_x or
                self.head.x < 0 or
                self.head.y >= self.size_y or
                self.head.y < 0):
                return self.OFFGRID

            if self.maze[self.head.y][self.head.x] == '#':
                if self.dir == self.UP:
                    self.head.y += 1
                    self.head.x += 1
                elif self.dir == self.RIGHT:
                    self.head.x -= 1
                    self.head.y += 1
                elif self.dir == self.DOWN:
                    self.head.y -= 1
                    self.head.x -= 1
                elif self.dir == self.LEFT:
                    self.head.x += 1
                    self.head.y -= 1
                self.dir = (self.dir + 1) % 4
            else:
                return self.CONTINUE

    def run_maze(self) -> int:
        while(self.mark_and_move() == self.CONTINUE):
            pass

        total = 0
        for r in self.maze:
            total += r.count('X')
        return total

    def find_maze_blockers(self) -> int:
        path_points = list()

        while(self.mark_and_move(path_points) == self.CONTINUE):
            pass

        # Ensure x/y pairs are unique (discard dir values)
        unique_blockers = list()
        for p in path_points:
            next_p = self.Point(p.x, p.y)
            if next_p not in unique_blockers:
                unique_blockers.append(next_p)

        total = 0
        for p in range(1, len(unique_blockers)):
            test_maze = Maze(self.filename)

            test_maze.maze[unique_blockers[p].y][unique_blockers[p].x] = '#'

            test_points = list()
            while(True):
                status = test_maze.mark_and_move(test_points)
                if status == self.CONTINUE:
                    continue

                if status == self.LOOPING:
                    total += 1
                    print("Looping:", total, "Blockers Tested:", p)

                break
        return total

m = Maze("day6_input1.txt")
print("Total valid blockers found:", m.find_maze_blockers())
