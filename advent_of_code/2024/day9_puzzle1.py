class Disc:
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

    def get_checksum(self, blocks):
        checksum = 0

        for i, b in enumerate(blocks):
            if b == -1:
                break;
            checksum += (i * b)

        return checksum


d = Disc("day9_input1.txt")
blocks = d.get_blocks(d.map)
d.defrag(blocks, False)
print("checksum:", d.get_checksum(blocks))
