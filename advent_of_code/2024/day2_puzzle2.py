from typing import List

class Report:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            self.rows = f.read().splitlines()

    def is_safe(self, values: List[int]) -> bool:
        prev = values[0]
        is_increasing = (values[1] > values [0])
        for next in values[1:]:
            if (next > prev) != is_increasing:
                return False
            if not (0 < abs(next - prev) < 4 ):
                return False
            prev = next

        return True

    def calculate(self):
        count = 0
        for r in self.rows:
            report = [int(i) for i in r.split(' ')]
            for i in range(len(report)):
                sub_list = report.copy()
                sub_list.pop(i)
                if self.is_safe(sub_list):
                    count += 1
                    break

        return count

r = Report("day2_input1.txt")
print(r.calculate())
