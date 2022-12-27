from collections import Counter

class Rocks:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            rows = f.read().splitlines()
        self.vectors = list()
        for r in rows:
            new_entry = [list(map(int,i.split(','))) for i in r.split(" -> ")]
            self.vectors.append(new_entry)

        allx = [x[0] for i in self.vectors for x in i]
        ally = [y[1] for i in self.vectors for y in i]
        self.min_x = min(allx)
        self.max_x = max(allx)
        self.min_y = min(ally)
        self.max_y = max(ally)
        self.grid_zero = self.min_x-1

        width = (self.max_x-self.min_x)+3
        height = self.max_y+2
        self.grid = ['.'*width for i in range(height)]
        for v in self.vectors:
            for i in range(len(v)-1):
                a,b = v[i:i+2]
                cols = range(a[0], b[0]+1) if a < b else range(b[0], a[0]+1)
                rows = range(a[1], b[1]+1) if a < b else range(b[1], a[1]+1)
                for row in rows:
                    for col in cols:
                        grid_col = col-self.grid_zero
                        self.grid[row] = self.grid[row][:grid_col] + '#' + self.grid[row][grid_col+1:]

    def is_overflowing(self):
        return 'o' in self.grid[-1]

    def print_grid(self):
        for g in self.grid:
            print(g)

    def drop_sand(self, x, y):
        if y != self.max_y+1:
            if self.grid[y+1][x-self.grid_zero] == '.':
                self.drop_sand(x,y+1)
                return
            elif self.grid[y+1][x-self.grid_zero-1] == '.':
                self.drop_sand(x-1,y+1)
                return
            elif self.grid[y+1][x-self.grid_zero+1] == '.':
                self.drop_sand(x+1,y+1)
                return
        grid_col = x-self.grid_zero
        self.grid[y] = self.grid[y][:grid_col] + 'o' + self.grid[y][grid_col+1:]

    def hourglass(self, x, y):
        while not self.is_overflowing():
            self.drop_sand(x, y)

        total = 0
        for g in self.grid:
            total += Counter(g)['o']
        return total-1

# r = Rocks("day14_test.txt")
r = Rocks("day14_input.txt")

print()
answer_1 = r.hourglass(500,0)
r.print_grid()
print()
print("Answer #1:", answer_1)
