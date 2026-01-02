import itertools
import math
import numpy as np
import matplotlib.pyplot as plt
import time

class Tile:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            raw_lines = f.read().splitlines()

        self.tiles = dict()
        for i, line in enumerate(raw_lines):
            coords = [int(x) for x in line.split(',')]
            self.tiles[i] = np.array(coords)

        self.populate_area_list()
        self.populate_green()
        self.populate_x_list()
        # self.plot_red_and_green()

    def populate_x_list(self):
        self.x_set = dict()

        for i in self.tiles.keys():
            x = self.tiles[i][0]
            y = self.tiles[i][1]

            if x in self.x_set.keys():
                self.x_set[x].add(y)
            else:
                self.x_set[x] = set([y])

        for i in self.green_points.keys():
            x = self.green_points[i][0]
            y = self.green_points[i][1]

            if x in self.x_set.keys():
                self.x_set[x].add(y)
            else:
                self.x_set[x] = set([y])

    def populate_area_list(self):
        self.areas = list()

        combos = itertools.combinations(self.tiles.keys(), 2)
        for c in combos:
            self.areas.append((self.calc_area(c), c))

        self.areas = sorted(self.areas, reverse=True)

    def populate_green(self):
        idx = max(self.tiles.keys()) + 1
        green_points = dict()

        red_points = [self.tiles[i] for i in self.tiles]
        red_points.append(red_points[0])

        for i in range(1, len(red_points)):
            x = sorted([red_points[i-1][0], red_points[i][0]])
            y = sorted([red_points[i-1][1], red_points[i][1]])

            if x[0] == x[1]:
                for j in range(y[0] + 1, y[1]):
                    green_points[idx] = np.array([x[0], j])
                    idx += 1
            elif y[0] == y[1]:
                for j in range(x[0] + 1, x[1]):
                    green_points[idx] = np.array([j, y[0]])
                    idx += 1

        self.green_points = green_points

    def plot_red_and_green(self):
        x = [self.tiles[i][0] for i in self.tiles.keys()]
        y = [self.tiles[i][1] for i in self.tiles.keys()]
        plt.plot(x,y, 'r.')
        x = [self.green_points[i][0] for i in self.green_points]
        y = [self.green_points[i][1] for i in self.green_points]
        plt.plot(x,y, 'g.')
        plt.show()

    def calc_area(self, tile_pair: tuple) -> int:
        return math.prod(abs(self.tiles[tile_pair[0]] - self.tiles[tile_pair[1]]) + 1)

    def get_largest_square_area(self) -> int:
        return int(self.areas[0][0])

    def bounded_is_valid(self, tile_pair: tuple) -> bool:
        #FIXME: This assumes box is at least 3 wide and 3 tall
        #FIXME: Check that edges with gaps always end in red

        #Check that there are no nodes inside of the box
        x = sorted([self.tiles[c][0] for c in tile_pair])
        y = sorted([self.tiles[c][1] for c in tile_pair])

        if x[1] - x[0] < 2 or y[1] - y[0] < 2:
            return False

        inner_x = range(x[0]+1, x[1])
        inner_y = set(range(y[0]+1, y[1]))

        for ix in inner_x:
            if not self.x_set[ix].isdisjoint(inner_y):
                return False

        return True

    def find_largest_bounded_area(self):
        for i, a in enumerate(self.areas):
            print(f"Testing {i} of {len(self.areas)}", end='\r')
            if self.bounded_is_valid(a[1]):
                return a[0]

test_t = Tile('test_input.txt')
puzzle_t = Tile('puzzle_input.txt')

print(f"Largest square in test set: {test_t.get_largest_square_area()}")
start = time.time()
print(f"Largest bounded square in test set: {test_t.find_largest_bounded_area()}")
print(f"\t(elapsed time: {time.time() - start})")
print(f"Largest square in puzzle set: {puzzle_t.get_largest_square_area()}")
start = time.time()
print(f"Largest bounded square in puzzle set: {puzzle_t.find_largest_bounded_area()}")
print(f"\t(elapsed time: {time.time() - start})")
