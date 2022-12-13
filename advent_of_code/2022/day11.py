class Monkey:
    def __init__(self, num, items, operation, test, m_true, m_false):
        self.num = num
        self.items = items
        self.operation = operation
        self.test = test
        self.m_true = m_true
        self.m_false = m_false

    def print(self):
        print(self.num, self.items, self.operation, self.test, self.m_true, self.m_false)

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
            print(self.commands[i:i+7])
            self.store_monkey(self.commands[i:i+7])

    def print_monkeys(self):
        for i in self.monkeys:
            self.monkeys[i].print()

b = Business("day11_test.txt")
# b = Business("day11_input.txt")
b.load_chunks()
b.print_monkeys()
