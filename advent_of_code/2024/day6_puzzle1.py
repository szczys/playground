from typing import List
import re

class Maze:
    UP=0
    RIGHT=1
    DOWN=2
    LEFT=3

    class Point:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

    def __init__(self, f_name):
        with open(f_name, "r") as f:
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

    def mark_and_move(self) -> bool:
        self.maze[self.head.y][self.head.x] = 'X'

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
                return False

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
                return True

    def run_maze(self) -> int:
        while(self.mark_and_move()):
            pass

        total = 0
        for r in self.maze:
            total += r.count('X')
        return total

m = Maze("day6_input1.txt")
print(m.run_maze())
