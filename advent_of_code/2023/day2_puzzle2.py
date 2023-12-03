class Game:
    def __init__(self, gamedata):
        self.id = int(gamedata.split(":")[0].split(' ')[1])

        allrounds = gamedata.split(":")[1]
        self.max = {'red': 0, 'green': 0, 'blue': 0}
        self.rounds = list()
        for r in allrounds.split(';'):
            cubes = dict()
            for c in r.split(','):
                members = c.lstrip().split(' ')
                color = members[1]
                count = int(members[0])
                cubes[color] = int(count)
                if count > self.max[color]:
                    self.max[color] = count 
            self.rounds.append(cubes)
        self.power = self.max['red'] * self.max['green'] * self.max['blue'] 

    def get_max(self):
        return self.max

class Match:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            rows = f.read().splitlines()
        self.games = list()
        for r in rows:
            self.games.append(Game(r))

    def test_games(self, red, green, blue):
        totals = 0
        for g in self.games:
            max = g.get_max()
            if max['red'] > red or max['green'] > green or max['blue'] > blue:
                print("Impossible:", g.id, max)
            else:
                totals += g.id
        print("Total Possible:", totals)

    def show_power(self):
        for g in self.games:
            print(g.id, g.power)

    def sum_power(self):
        sum = 0
        for g in self.games:
            sum += g.power
        return sum

m = Match("day2_input1.txt")
print(m.sum_power())
