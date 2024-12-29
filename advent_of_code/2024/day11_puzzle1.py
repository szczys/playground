from typing import List
import time
import threading

class Stones:
    def __init__(self, f_name):
        self.filename = f_name
        with open(self.filename, "r") as f:
            self.rows = f.read().splitlines()

        self.line = [int(s) for s in self.rows[0].split(' ')]

        self.max = 0
        self.start_time = time.time()
        self.solutions = list()

    def blink(self, num: int) -> List:
        if num == 0:
            return [1]
        elif len(str(num)) % 2 == 0:
            str_stone = str(num)
            half_width = int(len(str_stone) / 2 )
            left_stone = int(str_stone[:half_width])
            right_stone = int(str_stone[half_width:])

            return [left_stone, right_stone]
        else:
            return [num * 2024]

    def recurse(self, num: int, depth: int) -> int:
        if depth == 0:
            return 1

        count = 0
        line = self.blink(num)

        depth -= 1
        for n in line:
            if n in self.solutions[depth]:
                count += self.solutions[depth][n]
                continue

            solution = self.recurse(n, depth)
            count += solution
        self.solutions[depth + 1][num] = count
        if count > self.max:
            self.max = count
        return count

    def solve(self, num_set: List, blinks: int) -> int:
        self.solutions = list()
        for _ in range(blinks + 1):
            self.solutions.append(dict())

        count = 0
        for n in num_set:
            count += s.recurse(n, blinks)
        return count
 
s = Stones("day11_input1.txt")

s.start_time = time.time()
for i in [25, 75]:
    print(f"Total stones after {i} blinks:", s.solve(s.line, i))
