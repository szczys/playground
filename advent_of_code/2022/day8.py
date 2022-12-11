class Trees:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            self.grid = [[int(n) for n in line] for line in f.read().splitlines()]
        self.rotated = list(zip(*self.grid))

    def is_visible(self, row, idx):
        left = max(row[:idx])
        right = max(row[idx+1:])
        if row[idx] > left or row[idx] > right:
            return True
        return False

    def calc_visible(self):
        g_size = len(self.grid)
        visible = (g_size-1)*4;
        for x in range(1, g_size-1):
            for y in range(1, g_size-1):
                if self.is_visible(self.grid[y], x) or self.is_visible(self.rotated[x], y):
                    visible += 1
        return visible

t = Trees("day8_input.txt")
# t = Trees("day8_test.txt")
print("")
print("Visible:", t.calc_visible())
