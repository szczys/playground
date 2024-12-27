class Puzzle:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            self.rows = f.read().splitlines()

        self.columns = list()
        for i in range(len(self.rows[0])):
            col = ""
            for r in self.rows:
                col += r[i]
            self.columns.append(col)

        self.fslash = list()
        for i in range(len(self.rows)):
            diag = ""
            col = 0
            while((i >= 0) and (col < len(self.rows[0]))):
                diag += self.rows[i][col]
                i -= 1
                col += 1
            self.fslash.append(diag)
        # edge case
        for c in range(1, len(self.rows[0])):
            row_idx = len(self.rows) - 1
            diag = ""
            while(c < len(self.rows[0])):
                diag += self.rows[row_idx][c]
                c += 1
                row_idx -= 1
            self.fslash.append(diag)

        self.bslash = list()
        # edge case
        for c in range(len(self.rows[0])-1, 0, -1):
            row_idx = 0
            diag = ""
            while(c < len(self.rows[0])):
                diag += self.rows[row_idx][c]
                c += 1
                row_idx += 1
            self.fslash.append(diag)
        for i in range(len(self.rows)):
            diag = ""
            col = 0
            while((i < len(self.rows)) and (col < len(self.rows[0]))):
                diag += self.rows[i][col]
                i += 1
                col += 1
            self.fslash.append(diag)



    def find_word(self, word: str) -> int:
        total = 0
        for r in self.rows:
            total += r.count(word)
            total += r.count(word[::-1])
        for c in self.columns:
            total += c.count(word)
            total += c.count(word[::-1])
        for b in self.bslash:
            total += b.count(word)
            total += b.count(word[::-1])
        for f in self.fslash:
            total += f.count(word)
            total += f.count(word[::-1])
        return total

p = Puzzle("day4_input1.txt")
print(p.find_word("XMAS"))
