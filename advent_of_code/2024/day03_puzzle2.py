import re

from typing import List

class Multiply:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            self.data = f.read()

        p = re.compile("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")
        self.commands = p.findall(self.data)

    def process(self):
        p = re.compile("\d{1,3}")
        total = 0
        skip = False
        for c in self.commands:
            if c == "do()":
                skip = False
            elif c == "don't()":
                skip = True
            elif skip:
                continue
            else:
                nums = p.findall(c)
                total += (int(nums[0]) * int(nums[1]))
        return total


m = Multiply("day03_input1.txt")
print(m.process())
