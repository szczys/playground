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
            if self.branch_and_reduce(c.solution, c.values):
                total += c.solution
        return total

b = Bridge("day7_input1.txt")
print(b.sum_solvable())
