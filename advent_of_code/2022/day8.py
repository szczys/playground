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
        visible = (g_size-1)*4; #Trees on border are visible
        for x in range(1, g_size-1):
            for y in range(1, g_size-1):
                if self.is_visible(self.grid[y], x) or self.is_visible(self.rotated[x], y):
                    visible += 1
        return visible

    def get_right_sight_dist(self, r_slice, height):
        count = 0
        for n in r_slice:
            count += 1
            if n >= height:
                break
        return count

    def get_tree_sight_score(self, x, y):
        tree_h = self.grid[y][x]
        slices = list()
        slices.append(list(reversed(self.rotated[x][:y]))) #u_slice
        slices.append(list(reversed(self.grid[y][:x]))) #l_slice
        slices.append(self.grid[y][x+1:]) #r_slice
        slices.append(self.rotated[x][y+1:]) #d_slice

        sight_score = 1
        for s in slices:
            sight_score *= self.get_right_sight_dist(s, tree_h)

        return sight_score


    def calc_most_scenic(self):
        g_size = len(self.grid)
        scores = list()
        for x in range(1, g_size-1):
            for y in range(1, g_size-1):
                scores.append(self.get_tree_sight_score(x, y))
        return max(scores)



t = Trees("day8_input.txt")
# t = Trees("day8_test.txt")
print("")
print("Visible:", t.calc_visible())
print("")
print("Most scenic:", t.calc_most_scenic())
