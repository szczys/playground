from collections import defaultdict

class Card:
    def __init__(self, id=None, winners="", players=""):
        self.id = id 
        self.winners = [int(num) for num in winners.strip().split(' ')]
        self.players = [int(num) for num in players.strip().split(' ')]

        self.match_count = 0
        for i in self.players:
            if i in self.winners:
                self.match_count += 1

        if self.match_count < 1:
            self.score = 0
        else:
            self.score = 2 ** (self.match_count - 1)
    
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
        
    def get_total_multiples(self):
        multiples = defaultdict(int)
        for c in self.cards:
            multiples[c.id] = 1

        for c in self.cards:
            for i in range(1, c.match_count + 1):
                multiples[c.id + i] += (1 * multiples[c.id])

        return sum(multiples.values())
            
s = Scratchers("day4_input1.txt")
print("\nTotal Multiples:", s.get_total_multiples())
