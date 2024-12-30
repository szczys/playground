from typing import List
from copy import deepcopy

class Garden:
    class Point:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

        def __str__(self):
            return f"({self.x}, {self.y})"

        def __eq__(self, p):
            return (self.x == p.x and self.y == p.y)

    class Node:
        def __init__(self, x: int, y: int, plant: str):
            self.id = Garden.Point(x, y)
            self.plant = plant

        def __str__(self):
            return f"(id: {self.id}, plant: {self.plant})"

        def __eq__(self, n):
            return self.id == n.id

        def __hash__(self):
            return hash(str(self))

    def __init__(self, f_name):
        self.filename = f_name
        with open(self.filename, "r") as f:
            self.rows = f.read().splitlines()

        self.size_x = len(self.rows[0])
        self.size_y = len(self.rows)

        self.map = list()
        for y, r in enumerate(self.rows):
            for x, h in enumerate(r):
                self.map.append(self.Node(x, y, h))

    def find_perimeter(self, n, map):
        neighbors = [
                Garden.Point(n.id.x    , n.id.y - 1),
                Garden.Point(n.id.x + 1, n.id.y    ),
                Garden.Point(n.id.x    , n.id.y + 1),
                Garden.Point(n.id.x - 1, n.id.y    ),
                ]

        perimeter = 4
        for p in map:
            if p.id in neighbors and p.plant == n.plant:
                perimeter -= 1

        return perimeter

    def get_group(self, plant, map: List, found: List):
        if plant not in found:
            found.append(plant)
        neighbors = [
                Garden.Point(plant.id.x    , plant.id.y - 1),
                Garden.Point(plant.id.x + 1, plant.id.y    ),
                Garden.Point(plant.id.x    , plant.id.y + 1),
                Garden.Point(plant.id.x - 1, plant.id.y    ),
                ]

        for p in self.map:
            if (p.id in neighbors and
                p.plant == plant.plant and
                p not in found):
                found.append(p)
                self.get_group(p, map, found)

    def crawl_prices(self, map):
        nodes = deepcopy(map)
        total_price = 0

        while(len(nodes)):
            p = nodes[0]
            same_plant = list()
            self.get_group(p, nodes, same_plant)

            plant_type = p.plant
            area = len(same_plant)
            perimeter = 0
            for i in same_plant:
                perimeter += self.find_perimeter(i, same_plant)
                nodes.pop(nodes.index(i))

            print(f"{plant_type}: area: {str(area).rjust(3)} perimeter: {str(perimeter).rjust(3)} Remaining Nodes: {str(len(nodes)).rjust(5)}")
            total_price += (area * perimeter)

        return total_price

g = Garden("day12_input1.txt")
print("Fence prices:", g.crawl_prices(g.map))
