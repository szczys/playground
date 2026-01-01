import math
import numpy as np

class Extension:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            raw_lines = f.read().splitlines()

        self.boxes = dict()

        for i, line in enumerate(raw_lines):
            coords = [int(x) for x in line.split(',')]
            self.boxes[i] = np.array(coords)

        self.distances = list()
        keys = list(self.boxes.keys())

        for i, key in enumerate(keys):
            if i == len(keys) - 1:
                break
            for j in keys[i+1:]:
                self.distances.append([i,j,np.linalg.norm(self.boxes[keys[i]]-self.boxes[keys[j]])])

        self.distances = sorted(self.distances, key=lambda x: x[2])

    def make_connections(self, connection_num: int, calc_num: int):
        connections = dict()
        idx = 0
        for i in range(len(self.distances)):
            pt_a = self.distances[i][0]
            pt_b = self.distances[i][1]
            found_list = list()

            for circuit in connections.keys():
                if pt_a in connections[circuit]:
                    found_list.append(circuit)
                if pt_b in connections[circuit]:
                    found_list.append(circuit)
                if len(found_list) == 2:
                    break

            found_list = list(set(found_list))
            if len(found_list) == 0:
                connections[idx] = set([pt_a, pt_b])
                idx += 1
            elif len(found_list) == 1:
                connections[found_list[0]].add(pt_a)
                connections[found_list[0]].add(pt_b)
            else:
                circuit_a = list(connections.pop(found_list[0]))
                circuit_b = list(connections.pop(found_list[1]))
                connections[idx] = set(circuit_a + circuit_b)
                idx += 1

            if i == connection_num - 1:
                circuit_lengths = [len(connections[c]) for c in connections.keys()]
                circuit_lengths = sorted(circuit_lengths, reverse = True)
                print(f"Product first 3 of {connection_num} connections: {math.prod(circuit_lengths[:calc_num])}")


            # Stop when all boxes are connected
            if len(connections.keys()) == 1:
                keys = list(connections.keys())
                if len(connections[keys[0]]) == len(self.boxes):
                    print(f"{len(self.boxes)} connected: {self.boxes[pt_a][0] * self.boxes[pt_b][0]}")
                    return

test_t = Extension('test_input.txt')
puzzle_t = Extension('puzzle_input.txt')


print()
print("Running test set:")
test_t.make_connections(10, 3)
print()
print("Running puzzle set:")
puzzle_t.make_connections(1000, 3)
