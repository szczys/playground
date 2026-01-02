class Machine:
    def __init__(self, initiator: str):
        self.buttons = list()

        for i in initiator.split():
            # Use chr() for square bracket so vim indenting doesn't freak out
            if i[0] == chr(91):
                self.lights = i[1:-1]

            # Use chr() for parenthesis so vim indenting doesn't freak out
            elif i[0] == chr(40):
                button = [int(x) for x in i[1:-1].split(',')]
                self.buttons.append(button)

            # Use chr() for curly bracket so vim indenting doesn't freak out
            elif i[0] == chr(123):
                self.joltages = [int(x) for x in i[1:-1].split(',')]

            else:
                raise ValueError(f"Failed to parse: {i[0]}")

        self.lights_b = 0b0
        for i, c in enumerate(self.lights):
            if c == '#':
                self.lights_b = self.lights_b | (1<<i)

        self.buttons_b = dict()
        for i, b in enumerate(self.buttons):
            bin_val = 0b0
            for j in b:
                bin_val = bin_val | (1<<j)
            self.buttons_b[i] = bin_val

        self.moves = dict()
        for bb in self.buttons_b:
            self.moves[self.buttons_b[bb]] = [bb]

    def find_shortest(self):
        target = self.lights_b
        while target not in self.moves:
            moves = [m for m in self.moves.keys()]
            for i in moves:
                for j in self.buttons_b:
                    result = self.buttons_b[j] ^ i
                    if result not in moves:
                        self.moves[result] = self.moves[i] + [j]
        return len(self.moves[target])


    def __repr__(self):
        return f"Machine:\n  Lights: {self.lights}\n  Buttons: {self.buttons}\n  Joltages: {self.joltages}"

class Collective:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            raw_lines = f.read().splitlines()

        self.machines = list()

        for rl in raw_lines:
            self.machines.append(Machine(rl))

    def calc_shortest(self):
        total = 0

        for m in self.machines:
            shortest = m.find_shortest()
            total += shortest
            print(f"Shortest {m.lights_b:b}: {shortest}")

        return total

test_m = Collective('test_input.txt')
puzzle_m = Collective('puzzle_input.txt')

print()
print(f"Fewest button presses in test set: {test_m.calc_shortest()}")
print()
print(f"Fewest button presses in puzzle set: {puzzle_m.calc_shortest()}")
