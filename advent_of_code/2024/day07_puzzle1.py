from typing import List
from copy import deepcopy

class Bridge:
    class Calib:
        def __init__(self, calib_str: str):
            self.solution = int(calib_str.split(":")[0])
            self.values = [int(v) for v in calib_str.split(":")[1].lstrip().split(" ")]
        def __str__(self):
            return f"<{self.solution}: {self.values}>"

    def __init__(self, f_name):
        self.filename = f_name
        with open(self.filename, "r") as f:
            self.rows = f.read().splitlines()

        self.cal = [self.Calib(r) for r in self.rows]

    def concat(self, a: int, b: int) -> int:
        return int((str(a) + str(b)))

    def branch_and_consume(self, total: int, tokens: List[int]) -> bool:
        test_value = tokens.pop(0)

        if len(tokens) == 0:
            return (total == test_value)

        next_value = tokens.pop(0)
        m_list = deepcopy(tokens)
        m_list.insert(0, test_value * next_value)
        multiple = self.branch_and_consume(total, m_list)

        s_list = deepcopy(tokens)
        s_list.insert(0, test_value + next_value)
        sum = self.branch_and_consume(total, s_list)

        c_list = deepcopy(tokens)
        c_list.insert(0, self.concat(test_value, next_value))
        concat = self.branch_and_consume(total, c_list)

        return (multiple or sum or concat)

    def branch_and_reduce(self, total: int, tokens: List[int]) -> bool:
        test_value = tokens.pop(-1)

        if len(tokens) < 1:
            if total == test_value:
                return True
            else:
                return False

        multiple = False
        compound = False

        if total % test_value ==  0:
            multiple = self.branch_and_reduce(int(total/test_value), deepcopy(tokens))
        if test_value <= total:
            compound = self.branch_and_reduce(total-test_value, deepcopy(tokens))

        return (multiple or compound)

    def sum_solvable(self) -> int:
        total = 0
        for c in self.cal:
            if self.branch_and_reduce(c.solution, deepcopy(c.values)):
                total += c.solution
        return total

    def sum_with_concat(self) -> int:
        total = 0
        print()
        for i, c in enumerate(self.cal):
            print(f"Calculate: {i}/{len(self.cal)} ({int(100 * float(i)/float(len(self.cal)))}%)", end = '\r')
            if self.branch_and_consume(c.solution, deepcopy(c.values)):
                total += c.solution
        return total

b = Bridge("day07_input1.txt")
print("Solvable:", b.sum_solvable())
print("With concat:", b.sum_with_concat())
