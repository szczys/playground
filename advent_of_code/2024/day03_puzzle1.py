import re

from typing import List

class Multiply:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            self.data = f.read()

        p = re.compile("mul\(\d{1,3},\d{1,3}\)")
        self.commands = p.findall(self.data)

    def process(self):
        p = re.compile("\d{1,3}")
        total = 0
        for c in self.commands:
            nums = p.findall(c)
            total += (int(nums[0]) * int(nums[1]))
        return total


m = Multiply("day03_input1.txt")
print(m.process())
