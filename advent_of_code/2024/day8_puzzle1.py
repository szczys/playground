from typing import List

class Map:
    class Antenna:
        def __init__(self, x: int, y: int, freq: str):
            self.x = x
            self.y = y
            self.freq = freq

        def __str__(self):
            return f"<freq: {self.freq} (x: {self.x}, y: {self.y})>"

        def __eq__(self, a):
            return (self.x == a.x and self.y == a.y and self.freq == a.freq)

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

    def gen_antinodes(self, a, b, antinodes: List):
        center_x = (a.x + b.x) / 2
        center_y = (a.y + b.y) / 2

        x_diff = (a.x - b.x)/2
        y_diff = (a.y - b.y)/2

        x_inc = x_diff * 3
        y_inc = y_diff * 3

        an0 = self.Antenna(center_x - x_inc, center_y - y_inc, '#')
        an1 = self.Antenna(center_x + x_inc, center_y + y_inc, '#')

        for a in [an0, an1]:
            if (a not in antinodes and
                (0 <= a.x < self.size_x) and
                (0 <= a.y < self.size_y)):
                antinodes.append(a)

    def calc_antinodes(self) -> int:
        antinodes = list()

        for i, t in enumerate(self.towers):
            if i == len(self.towers) - 1:
                return len(antinodes)

            # print(i, len(self.towers[i+1:]))
            for n in self.towers[i + 1:]:
                if n.freq == t.freq:
                    self.gen_antinodes(t, n, antinodes)

        # We should never get here
        return -1

m = Map("day8_input1.txt")
print(f"Map size: {m.size_x}x{m.size_y}")
print("Total antinodes:", m.calc_antinodes())
