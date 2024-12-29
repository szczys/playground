from typing import List
from copy import deepcopy

class Disc:
    class Node:
        def __init__(self, block_id: int, block_size: int, trailing_space: int):
            self.id = block_id
            self.size = block_size
            self.space = trailing_space

        def __str__(self):
            return f"(id: {self.id}, size: {self.size}, space: {self.space})"

        def __eq__(self, n):
            return self.id == n.id

    def __init__(self, f_name):
        self.filename = f_name
        with open(self.filename, "r") as f:
            self.rows = f.read().splitlines()

        self.map = [int(b) for b in self.rows[0]]

    def blocks_to_string(self, blocks):
        return "".join([str(n) for n in blocks]).replace("-1", ".")

    def get_blocks(self, map):
        blocks = list()

        for i, e in enumerate(map):
            if i % 2 == 0:
                try:
                    block_idx = int(i / 2)
                except:
                    block_idx = 0

                blocks += ([block_idx] * e)

            else:
                blocks += ([-1] * e)

        return blocks

    def get_node_map(self, map: List):
        nodes = list()
        for i in range(0, len(map), 2):
            try:
                id = int(i / 2)
            except:
                id = 0

            size = map[i]

            if (i == len(map) - 1):
                trailing_space = 0
            else:
                trailing_space = self.map[i + 1]

            new_node = self.Node(id, size, trailing_space)
            nodes.append(new_node)
        return nodes

    def swap_blocks(self, blocks):
        try:
            next_empty = blocks.index(-1)
            if next_empty >= len(blocks) - 1:
                return False
        except:
            return False

        remaining_unique = sorted(list(set(blocks[next_empty + 1:])))

        if len(remaining_unique) == 1 and remaining_unique[0] == -1:
            return False

        last_filled = -blocks[::-1].index(remaining_unique[-1]) - 1

        blocks[next_empty] = blocks[last_filled]
        blocks[last_filled] = -1

        return True

    def defrag(self, blocks, show_output: bool = False):
        moves = 0
        if show_output:
            print(d.blocks_to_string(blocks))
        while(True):
            status = d.swap_blocks(blocks)
            if not status:
                break
            moves += 1
            if moves % 100 == 0:
                print("Moves:", moves, end="\r")
            if show_output:
                print(d.blocks_to_string(blocks))
        print()

    def optimize(self, nodes: List):
        id_to_move = nodes[-1].id

        while (id_to_move > 0):
            print(f"Attempt to move: {str(id_to_move).rjust(5)}", end = '\r')
            target_idx = None
            for j, target in enumerate(nodes):
                if target.id == id_to_move:
                    target_idx = j
                    break

            for i, n in enumerate(nodes):
                if n.id == id_to_move:
                    id_to_move -= 1
                    break

                if target_idx == None:
                    print("Error: can't find target idx")
                    return

                if n.space < nodes[target_idx].size:
                    continue

                node_to_move = nodes.pop(target_idx)

                # Add newly freed space to node before target
                nodes[target_idx - 1].space += (node_to_move.size +
                                                node_to_move.space)

                # Update space in node being moved
                node_to_move.space = n.space - node_to_move.size

                # Node before moved block now has no space
                n.space = 0

                # Insert node
                nodes.insert(i + 1, node_to_move)

                id_to_move -= 1

                break

        print()

    def get_checksum(self, blocks):
        checksum = 0

        for i, b in enumerate(blocks):
            if b == -1:
                break;
            checksum += (i * b)

        return checksum

    def get_node_checksum(self, nodes) -> int:
        checksum = 0
        idx = 0
        for n in nodes:
            for _ in range(n.size):
                checksum += idx * n.id
                idx += 1

            for _ in range(n.space):
                idx += 1
        return checksum

d = Disc("day09_input1.txt")
blocks = d.get_blocks(d.map)
d.defrag(blocks, False)
print("checksum:", d.get_checksum(blocks))

nodes = d.get_node_map(d.map)
d.optimize(nodes)
print("checksum:", d.get_node_checksum(nodes))
