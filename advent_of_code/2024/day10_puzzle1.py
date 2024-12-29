from typing import List

class Topo:
    class Point:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

        def __str__(self):
            return f"({self.x}, {self.y})"

        def __eq__(self, p):
            return (self.x == p.x and self.y == p.y)

    class Node:
        def __init__(self, x: int, y: int, height: int):
            self.id = Topo.Point(x, y)
            self.height = height

        def __str__(self):
            return f"(id: {self.id}, height: {self.height})"

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
                self.map.append(self.Node(x,y, int(h)))

    def get_trailheads(self, map: List) -> List:
        trailheads = list()
        for n in map:
            if n.height == 0:
                trailheads.append(n)
        return trailheads

    def path_find(self, n, map: List) -> List:
        summits = list()
        if n.height == 9:
            summits.append(n)
            return summits

        neighbors = [
                Topo.Point(n.id.x    , n.id.y - 1),
                Topo.Point(n.id.x + 1, n.id.y    ),
                Topo.Point(n.id.x    , n.id.y + 1),
                Topo.Point(n.id.x - 1, n.id.y    ),
                ]

        for p in map:
            if p.id in neighbors and p.height == n.height + 1:
                summits += self.path_find(p, map)

        return summits

 
t = Topo("day10_input1.txt")
heads = t.get_trailheads(t.map)
print("Trailheads found:", len(heads))
total_trails = 0
for h in heads:
    summits = t.path_find(h, t.map)
    subtotal = len(set(summits))
    total_trails += subtotal
    print(h, "summits:", subtotal)
print("Total trails:", total_trails)


