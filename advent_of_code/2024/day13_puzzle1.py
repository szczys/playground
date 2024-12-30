from typing import List
import re

class Machine:
    class Button:
        def __init__(self, x: int, y: int, cost: int):
            self.x = x
            self.y = y
            self.cost = cost

        def __str__(self):
            return f"({self.x}, {self.y}), {self.cost}"

    class Prize:
        def __init__(self, x: int, y: int, buttons: List):
            self.x = x
            self.y = y
            self.buttons = buttons

        def __str__(self):
            return f"({self.x}, {self.y}), [{self.buttons[0]}, {self.buttons[1]}]"

    def __init__(self, f_name):
        self.filename = f_name
        with open(self.filename, "r") as f:
            self.rows = f.read().splitlines()

        self.arcade = list()

        p = re.compile('\d+')
        for i in range(0, len(self.rows), 4):
            button_a = re.findall(p, self.rows[i])
            button_b = re.findall(p, self.rows[i + 1])
            prize_loc = re.findall(p, self.rows[i + 2])

            self.arcade.append(self.Prize(int(prize_loc[0]),
                                          int(prize_loc[1]),
                                          [self.Button(int(button_a[0]),
                                                       int(button_a[1]),
                                                       3),
                                           self.Button(int(button_b[0]),
                                                       int(button_b[1]),
                                                       1)]
                                          )
                               )

    def calc_lowest_cost(self, machine):
        solutions = list()

        n = int(machine.x / machine.buttons[0].x)

        while n >= 0:
            product = n * machine.buttons[0].x
            difference = (machine.x - product)
            if difference % machine.buttons[1].x == 0:
                j = int(difference / machine.buttons[1].x)
                if (n * machine.buttons[0].y) + (j * machine.buttons[1].y) == machine.y:
                    cost = (n * machine.buttons[0].cost) + (j * machine.buttons[1].cost)
                    solutions.append(cost)
            n -= 1

        try:
            return min(solutions)
        except:
            return 0

    def calc_total_cost(self, arcade):
        total = 0
        for a in arcade:
            total += self.calc_lowest_cost(a)
        return total


m = Machine("day13_input1.txt")
print("Total cost of all wins:", m.calc_total_cost(m.arcade))
