from typing import List

class Publish:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            self.rows = f.read().splitlines()

        div = self.rows.index("")

        self.rules = dict()
        self.entries = list()

        for i in range(div):
            rule = self.rows[i].split("|")
            l_rule = int(rule[0])
            r_rule = int(rule[1])

            if l_rule in self.rules:
                self.rules[l_rule].append(r_rule)
            else:
                self.rules[l_rule] = [r_rule]

        for i in range(div + 1, len(self.rows)):
            self.entries.append([int(n) for n in self.rows[i].split(',')])

    def get_middle(self, entry: List[int]) -> int:
        mid = int(len(entry) / 2)
        return entry[mid]

    def follows_rules(self, entry: List[int]) -> bool:
        for i, e in enumerate(entry):
            if e not in self.rules:
                continue
            before = entry[:i]
            for r in self.rules[e]:
                if r in before:
                    return False
        return True

    def sum_of_correct(self) -> int:
        total = 0
        for e in self.entries:
            if self.follows_rules(e):
                total += self.get_middle(e)
        return total

p = Publish("day5_input1.txt")
print(p.sum_of_correct())
