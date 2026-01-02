import math

class Worksheet:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            in_data = f.read().splitlines()

        self.count = len(in_data[0].strip().split())
        self.ops = in_data[-1].strip().split()

        self.problems = list()
        for i in range(self.count):
            problem = [int(x.strip().split()[i]) for x in in_data[:-1]]
            self.problems.append(problem)

    def solve_worksheet(self):
        total = 0
        for i, op in enumerate(self.ops):
            if op == '+':
                total += sum(self.problems[i])
            elif op == '*':
                total += math.prod(self.problems[i])
            else:
                raise ValueError("Operation was not + or *:", op)
        return total

test_w = Worksheet('/home/mike/compile/playground/advent_of_code/2025/day6/test_input.txt')

puzzle_w = Worksheet('/home/mike/compile/playground/advent_of_code/2025/day6/puzzle_input.txt')

print("Test worksheet:", test_w.solve_worksheet())
print("Puzzle worksheet:", puzzle_w.solve_worksheet())

class CephWorksheet:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            in_data = f.read().splitlines()

        self.raw_ops = in_data[-1]
        self.ops = self.raw_ops.strip().split()
        self.op_cols = list()

        for i in range(len(self.raw_ops) -1, -1, -1):
            if self.raw_ops[i] != ' ':
                self.op_cols.append(i)

        self.problems = list()
        next_col = len(self.raw_ops) - 1
        for oc in self.op_cols:
            problem = list()
            while next_col >= oc:
                number = ''
                for r in in_data[:-1]:
                    number += r[next_col]
                problem.append(int(number.strip()))
                next_col -= 1
            self.problems.append(problem)
            next_col -= 1

        self.problems = list(reversed(self.problems))

    def solve_worksheet(self):
        total = 0
        for i, op in enumerate(self.ops):
            if op == '+':
                total += sum(self.problems[i])
            elif op == '*':
                total += math.prod(self.problems[i])
            else:
                raise ValueError("Operation was not + or *:", op)
        return total

test_cw = CephWorksheet('/home/mike/compile/playground/advent_of_code/2025/day6/test_input.txt')

puzzle_cw = CephWorksheet('/home/mike/compile/playground/advent_of_code/2025/day6/puzzle_input.txt')

print("Test Cephalopod Worksheet:", test_cw.solve_worksheet())
print("Puzzle Cephalopod Worksheet:", puzzle_cw.solve_worksheet())
