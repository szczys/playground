class Tachyon:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            in_data = f.read().splitlines()

        self.source = [1 if c == 'S' else 0 for c in in_data[0]]

        self.splitters = list()
        for i, r in enumerate(in_data[2:]):
            if i % 2 != 0:
                continue
            self.splitters.append([1 if c == '^' else 0 for c in r])

    def squash_row(self, row: list, c: chr) -> str:
        outstr = ''
        for i in row:
            outstr += str(i)
        outstr = outstr.replace('0', '.')
        outstr = outstr.replace('1', c)
        return outstr

    def count_splits(self):
        split_count = 0
        beams = list(self.source)
        print(self.squash_row(beams, '|'))
        for step in self.splitters:
            print(self.squash_row(step, '^'))
            make_split = [sum(x) for x in zip(step, beams)]


            for i, b in enumerate(make_split):
                if b > 1:
                    split_count += 1
                    make_split[i-1] = 1
                    make_split[i+1] = 1
            for i, c in enumerate(step):
                if c > 0:
                    make_split[i] = 0
            print(self.squash_row(make_split, '|'))
            beams = make_split
        return split_count

    def count_quantum(self):
        q_table = [[1 for c in self.source]]

        for i, step in enumerate(reversed(self.splitters)):
            cur_level = list()
            for j, node in enumerate(step):
                if node == 0:
                    cur_level.append(q_table[i][j])
                else:
                    q_val = q_table[i][j-1] + q_table[i][j+1]
                    cur_level.append(q_val)

            q_table.append(cur_level)
        for q in q_table:
            print(q)
        print()

        return q_table[-1][self.source.index(1)]


test_t = Tachyon('/home/mike/compile/playground/advent_of_code/2025/day7/test_input.txt')

puzzle_t = Tachyon('/home/mike/compile/playground/advent_of_code/2025/day7/puzzle_input.txt')

print("Test split count:", test_t.count_splits())
print("Puzzle split count:", puzzle_t.count_splits())
print("Test quantum count:", test_t.count_quantum())
print("Puzzle quantum count:", puzzle_t.count_quantum())
