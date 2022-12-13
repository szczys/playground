class CRT:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            self.commands = f.read().splitlines()
        self.pc = 1
        self.x = 1
        self.history = dict()
        self.screen = ""

    def execute(self, line):
        tokens = line.split(" ")
        self.pc += 1
        if tokens[0] == "addx":
            self.pc += 1
            self.x += int(tokens[1])
            self.history[self.pc] = self.x

    def process_commands(self):
        for c in self.commands:
            self.execute(c)

    def locate_register(self, cycle):
        changes = sorted(self.history.keys())
        for i, n in enumerate(changes):
            if n > cycle:
                return cycle * self.history[changes[i-1]]

    def calc_sig_strength(self, start, offset):
        idx = start
        total = 0
        while (idx < self.pc):
            score = self.locate_register(idx)
            print(score)
            total += score
            idx += offset
        return total

    def fill_screen(self):
        print("")
        sprite_loc = 1
        for i in range(1, self.pc):
            if i in self.history:
                sprite_loc = self.history[i]
#                 print(list(range(sprite_loc-1, sprite_loc+2)), i)
#                 print(self.screen[:40])
            if (i-1)%40 in range(sprite_loc-1, sprite_loc+2):
                self.screen += "#"
            else:
                self.screen += "."
        for i in range(7):
            print(self.screen[i*40:(i*40)+40])

# c = CRT("day10_test.txt")
c = CRT("day10_input.txt")
c.process_commands()
print("Solution #1:")
print("Total:", c.calc_sig_strength(20,40))
c.fill_screen()
