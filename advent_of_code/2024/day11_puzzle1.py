class Stones:
    def __init__(self, f_name):
        self.filename = f_name
        with open(self.filename, "r") as f:
            self.rows = f.read().splitlines()

        self.line = [int(s) for s in self.rows[0].split(' ')]

    def blink(self, line):
        for i in range(len(line) - 1, -1, -1):
            if line[i] == 0:
                line[i] += 1
            elif len(str(line[i])) % 2 == 0:
                str_stone = str(line[i])
                half_width = int(len(str_stone) / 2 )
                left_stone = int(str_stone[:half_width])
                right_stone = int(str_stone[half_width:])

                if i == len(line) - 1:
                    line.append(right_stone)
                else:
                    line.insert(i + 1, right_stone)

                line[i] = left_stone
            else:
                line[i] *= 2024
 
s = Stones("day11_input1.txt")
# print(' '.join([str(n) for n in s.line]))

for _ in range(25):
    s.blink(s.line)

print("Total stones:", len(s.line))
