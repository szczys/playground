import re

class Distance:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            self.rows = f.read().splitlines()

        self.list_a = list()
        self.list_b = list()


    def populate(self):
        for r in self.rows:
            input = r.split(' ')
            self.list_a.append(int(input[0]))
            self.list_b.append(int(input[-1]))

        self.list_a = sorted(self.list_a)
        self.list_b = sorted(self.list_b)

    def calculate(self):
        total = 0
        for i in range(len(self.list_a)):
            total += abs(self.list_a[i] - self.list_b[i])
        return total


d = Distance("day1_input1.txt")
d.populate()
print(d.calculate())
