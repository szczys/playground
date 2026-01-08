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

    def reset_all_routes(self):
        for s in self.servers:
            s.routes = 0

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

    def calculate_path_through_nodes(self, start:str, node1:str, node2:str, end:str) ->int:
        print()
        print(f"Caculating routes from {start}, through {node1} and {node2}, to {end}")
        path1_seg1 = self.calc_routes(start, node1)
        print(f"\tRoutes from {start} to {node1}: {path1_seg1}")
        self.reset_all_routes()
        path1_seg2 = self.calc_routes(node1, node2)
        print(f"\tRoutes from {node1} to {node2}: {path1_seg2}")
        self.reset_all_routes()
        path1_seg3 = self.calc_routes(node2, end)
        print(f"\tRoutes from {node2} to {end}: {path1_seg3}")
        self.reset_all_routes()

        print()

        path2_seg1 = self.calc_routes(start, node2)
        print(f"\tRoutes from {start} to {node1}: {path2_seg1}")
        self.reset_all_routes()
        path2_seg2 = self.calc_routes(node2, node1)
        print(f"\tRoutes from {node2} to {node1}: {path2_seg2}")
        self.reset_all_routes()
        path2_seg3 = self.calc_routes(node1, end)
        print(f"\tRoutes from {node1} to {end}: {path2_seg3}")
        self.reset_all_routes()

        return (path1_seg1 * path1_seg2 * path1_seg3) + (path2_seg1 * path2_seg2 * path2_seg3)

test_n = Network('test_input.txt')
puzzle_n = Network('puzzle_input.txt')
test2_n = Network('test2_input.txt')

print("Total routes in test set:", test_n.calc_routes('you', 'out'))
print("Total routes in puzzle set:", puzzle_n.calc_routes('you', 'out'))

print("Test set routes through nodes:", test2_n.calculate_path_through_nodes('svr', 'dac', 'fft', 'out'))
print("Puzzle set routes through nodes:", puzzle_n.calculate_path_through_nodes('svr', 'dac', 'fft', 'out'))
