import itertools
import sympy as sp

class Machine:
    def __init__(self, initiator: str):
        self.name_str = initiator.split(':')[0]
        self.nodes_str = initiator.split(':')[1].split()

        self.name = hash(self.name_str)

        self.routes = 0

    def parse_nodes(self, server_dict):
        self.nodes = [server_dict[s] for s in self.nodes_str]

    def __eq__(self, other: int) -> bool:
        return id(self) == other

    def __repr__(self):
        return self.name_str

    def __hash__(self):
        return id(self)

class Network:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            raw_lines = f.read().splitlines()

        self.servers = [Machine(x) for x in raw_lines]
        self.servers.append(Machine("out:"))
        self.server_dict = dict()
        for s in self.servers:
            self.server_dict[s.name_str] = id(s)
        for s in self.servers:
            s.parse_nodes(self.server_dict)

    def calc_routes(self, start: str, end: str) -> int | None:
        unsolved = dict()
        for s in self.servers:
            unsolved[s] = s

        origin = unsolved[self.server_dict[start]]
        dest = unsolved[self.server_dict[end]]

        solved = dict()
        solved[dest] = unsolved.pop(dest)
        solved[dest].routes = 1

        while len(unsolved) > 0:
            new_found = list()
            for u in unsolved:
                if all([x in solved for x in u.nodes]):
                    # print(solved)
                    for n in u.nodes:
                        unsolved[u].routes += solved[n].routes
                    solved[u] = unsolved[u]
                    new_found.append(u)
                    if u == origin:
                        return solved[id(origin)].routes

            for n in new_found:
                unsolved.pop(n)

        return solved[id(origin)].routes

test_n = Network('test_input.txt')
puzzle_n = Network('puzzle_input.txt')

print("Total routes in test set:", test_n.calc_routes('you', 'out'))
print("Total routes in puzzle set:", puzzle_n.calc_routes('you', 'out'))

