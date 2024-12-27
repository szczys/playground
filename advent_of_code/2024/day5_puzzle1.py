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

    def fix_incorrect_entry(self, entry: List[int]) -> List[int]:
        fixed = entry.copy()
        is_fixed = False
        while(not is_fixed):
            is_fixed = True
            for i, e in enumerate(fixed):
                if e not in self.rules:
                    continue
                before = fixed[:i]
                insert_idx = i
                for r in self.rules[e]:
                    if r in before:
                        insert_idx = min(insert_idx, fixed.index(r))
                if (insert_idx != i):
                    val = fixed.pop(i)
                    fixed.insert(insert_idx, val)
                    is_fixed = False
                    break
        return fixed

    def sum_of_correct(self) -> int:
        total = 0
        for e in self.entries:
            if self.follows_rules(e):
                total += self.get_middle(e)
        return total

    def correct_and_sum(self) -> int:
        total = 0
        for e in self.entries:
            if not self.follows_rules(e):
                total += self.get_middle(self.fix_incorrect_entry(e))
        return total

p = Publish("day5_input1.txt")
print(p.correct_and_sum())
