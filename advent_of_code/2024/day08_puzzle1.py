from typing import List
from copy import deepcopy

class Map:
    class Antenna:
        def __init__(self, x: int, y: int, freq: str):
            self.x = x
            self.y = y
            self.freq = freq

        def __str__(self):
            return f"<freq: {self.freq} (x: {self.x}, y: {self.y})>"

        def __eq__(self, a):
            return (self.x == a.x and self.y == a.y)

    def __init__(self, f_name):
        self.filename = f_name
        with open(self.filename, "r") as f:
            self.rows = f.read().splitlines()

        self.size_x = len(self.rows[0])
        self.size_y = len(self.rows)

        self.towers = list()
        for y, row in enumerate(self.rows):
            for x, freq in enumerate(row):
                if freq != '.':
                    self.towers.append(self.Antenna(x, y, freq))

    def gen_antinodes(self, a, b, antinodes: List, extended: bool = False):
        center_x = (a.x + b.x) / 2
        center_y = (a.y + b.y) / 2

        x_diff = (a.x - b.x)/2
        y_diff = (a.y - b.y)/2

        multiplier = 3

        while(True):
            x_inc = x_diff * multiplier
            y_inc = y_diff * multiplier

            an0 = self.Antenna(int(center_x - x_inc), int(center_y - y_inc), '#')
            an1 = self.Antenna(int(center_x + x_inc), int(center_y + y_inc), '#')

            valid_count = 0

            for a in [an0, an1]:
                if a in antinodes:
                    valid_count += 1
                    antinodes[antinodes.index(a)].freq = a.freq
                    continue

                if ((0 <= a.x < self.size_x) and
                    (0 <= a.y < self.size_y)):
                    antinodes.append(a)
                    valid_count += 1

            if not extended or valid_count == 0:
                return
            else:
                multiplier += 2

    def visualize(self, antinodes: List):
        map = list()
        for _ in range(self.size_y):
            map.append([d for d in "." * self.size_x])

        for t in self.towers:
            map[t.y][t.x] = t.freq

        for a in antinodes:
            map[a.y][a.x] = a.freq

        for row in map:
            print("".join(row))


    def calc_antinodes(self,
                       antinodes: List | None = None,
                       extended: bool = False) -> int:
        if antinodes is None:
            antinodes = list()

        for i, t in enumerate(self.towers):
            if i == len(self.towers) - 1:
                return len(antinodes)

            for n in self.towers[i + 1:]:
                if n.freq == t.freq:
                    if extended:
                        for tower in [t, n]:
                            if tower not in antinodes:
                                antinodes.append(deepcopy(tower))

                    self.gen_antinodes(t, n, antinodes, extended)

        # We should never get here
        return -1

m = Map("day08_input1.txt")
print(f"Map size: {m.size_x}x{m.size_y}")

antinodes = list()
print()
print("\tTotal antinodes:", m.calc_antinodes(antinodes))
m.visualize(antinodes)
print()

antinodes = list()
print()
print("\tTotal antinodes (include harmonics):", m.calc_antinodes(antinodes, True))
m.visualize(antinodes)
print()
