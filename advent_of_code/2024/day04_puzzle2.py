class Puzzle:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            self.rows = f.read().splitlines()

    def find_cross_mas(self, x: int, y: int) -> bool:
        if (x > len(self.rows) - 3) or (y > len(self.rows[0]) - 3):
            return False

        bslash = ""
        fslash = ""

        for i in range(3):
            bslash += self.rows[x + i][y + i]
            fslash += self.rows[x + i][2 + y - i]

        found_bslash = ("MAS" in bslash) or ("SAM" in bslash)
        found_fslash = ("MAS" in fslash) or ("SAM" in fslash)

        if found_fslash and found_bslash:
            return True
        else:
            return False

    def find_plus_mas(self, x: int, y: int) -> bool:
        if (x > len(self.rows) - 3) or (y > len(self.rows[0]) - 3):
            return False

        vert = ""
        hori = self.rows[y + 1][x:x + 3]

        for i in range(3):
            vert += self.rows[x + 1][y + i]

        found_vert = ("MAS" in vert) or ("SAM" in vert)
        found_hori = ("MAS" in hori) or ("SAM" in hori)

        if found_vert and found_hori:
            return True
        else:
            return False

    def iter_puzzle(self) -> int:
        count = 0
        for x in range(len(self.rows) - 3):
            for y in range(len(self.rows[0]) - 3):
                if self.find_cross_mas(x, y):
                    count += 1
                    continue
                if self.find_plus_mas(x, y):
                    count += 1
        return count

p = Puzzle("day04_input1.txt")
print(p.iter_puzzle())
