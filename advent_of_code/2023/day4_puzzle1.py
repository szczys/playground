class Card:
    def __init__(self, id=None, winners="", players=""):
        self.id = id 
        self.winners = [int(num) for num in winners.strip().split(' ')]
        self.players = [int(num) for num in players.strip().split(' ')]

        power = -1
        for i in self.players:
            if i in self.winners:
                power += 1

        if power < 0:
            self.score = 0
        else:
            self.score = 2**power
        
    
    def __str__(self):
        return f"({self.id}, score={self.score}, winners={self.winners}, players={self.players})"
    def __repr__(self):
        return f"({self.id}, score={self.score}, winners={self.winners}, players={self.players})"

class Scratchers:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            rows = f.read().splitlines()

        self.cards = list()

        for r in rows:
            cardsplit = r.split(':')
            id = int(cardsplit[0].split(' ')[-1])
            values = cardsplit[1].split('|')
            self.cards.append(Card(id, values[0].replace('  ', ' '), values[1].replace('  ', ' ')))

    def get_total_score(self):
        total = 0
        for c in self.cards:
            total += c.score
        return total
            
s = Scratchers("day4_input1.txt")

for c in s.cards:
    print(c)

print("\nTotal Score:", s.get_total_score())
