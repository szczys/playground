from math import floor

class Monkey:
    def __init__(self, num, items, operation, test, m_true, m_false):
        self.num = num
        self.items = items
        self.operation = operation
        self.test = test
        self.m_true = m_true
        self.m_false = m_false
        self.inspections = 0

    def catch(self, new_item):
        self.items.append(new_item)

    def print(self):
        print(self.num, self.items, self.operation, self.test, self.m_true, self.m_false)

    def get_inspections(self):
        return self.inspections

    def operate(self, operand):
        if self.operation[1] == "old":
            return operand * operand
        if self.operation[0] == "+":
            return operand + int(self.operation[1])
        if self.operation[0] == "-":
            return operand - int(self.operation[1])
        if self.operation[0] == "*":
            return operand * int(self.operation[1])
        if self.operation[0] == "/":
            return operand / int(self.operation[1])

    def process_items(self, monkey_list):
        while(len(self.items) != 0):
            current = self.items.pop(0)
            inspected = self.operate(current)
            self.inspections += 1
            inspected = floor(inspected/3)  #divided worry
            if inspected % self.test == 0:
                monkey_list[self.m_true].catch(inspected)
            else:
                monkey_list[self.m_false].catch(inspected)

class Business:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            self.commands = f.read().splitlines()
        self.monkeys = dict()

    def store_monkey(self, chunk):
        num = int(chunk[0].split(':')[0].split(" ")[-1])
        items = [int(x) for x in chunk[1].split(":")[1].lstrip().split(", ")]
        parse_op = chunk[2].split(" ")
        operation = parse_op[-2:]
        test = int(chunk[3].split(" ")[-1])
        m_true = int(chunk[4].split(" ")[-1])
        m_false = int(chunk[5].split(" ")[-1])
        self.monkeys[num] = Monkey(num, items, operation, test, m_true, m_false)

    def load_chunks(self):
        for i in range(0, len(self.commands), 7):
            self.store_monkey(self.commands[i:i+7])

    def print_monkeys(self):
        for i in self.monkeys:
            self.monkeys[i].print()

    def go_round(self, iterations):
        for rpt in range(iterations):
            for i in self.monkeys:
                self.monkeys[i].process_items(self.monkeys)

    def print_inspections(self):
        i_list = list()
        for i in self.monkeys:
            work = self.monkeys[i].get_inspections()
            i_list.append(work)
            print("Monkey {}: {}".format(i, work))
        a = i_list.pop(i_list.index(max(i_list)))
        print("Question 1:", a * max(i_list))

# b = Business("day11_test.txt")
b = Business("day11_input.txt")

b.load_chunks()
b.go_round(20)
b.print_inspections()
# print("")
# b.print_monkeys()
