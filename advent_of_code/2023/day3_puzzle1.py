from enum import Enum
from os import walk
import string

class State(Enum):
    IDLE = 0
    NUM = 1

class Ranges:
    def __init__(self, x=list(), y=list()):
        self.xrange = x
        self.yrange = y
    def __repr__(self):
        return f"{self.xrange}\n{self.yrange}"

class Member:
    def __init__(self, value="", x=0, y=0):
        self.value = value
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.value}, [{self.x}, {self.y}])"
    def __repr__(self):
        return f"({self.value}, [{self.x}, {self.y}])"

class Grid:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            rows = f.read().splitlines()

        self.nums = list()
        self.syms = list()

        self.state = State.IDLE
        self.cur_member = None

        for y, r in enumerate(rows):
            for x, c in enumerate(r):
                if self.state == State.IDLE:
                    if c != '.':
                        if c in string.digits:
                            self.cur_member = Member(c, x, y)
                            self.state = State.NUM
                        else:
                            self.add_symbol(c, x, y)
                            
                elif self.state == State.NUM:
                    if c in string.digits:
                        self.cur_member.value += c
                    else:
                        self.close_member()
                        self.state = State.IDLE

                        if c != '.':
                            self.add_symbol(c, x, y)

            self.close_member()
        self.close_member()

    def add_symbol(self, sym, x, y):
        m = Member(sym, x, y)
        self.syms.append(m)

    def close_member(self):
        if self.state == State.NUM and self.cur_member != None:
            self.nums.append(self.cur_member)
        self.cur_member = None

    def get_ranges(self, num):
        ranges = Ranges()
        for n in self.nums:
            if n == num:
                ranges.xrange = list(range(n.x-1,n.x+len(num.value)+1))
                ranges.yrange = list(range(n.y-1, n.y+2))
        return ranges

    def sum_all_parts(self):
        sum = 0

        for n in g.nums:
            r = g.get_ranges(n)
            invalid = True
            for s in g.syms:
                if s.x in r.xrange and s.y in r.yrange:
                    invalid = False
                    break
            if invalid:
                # print("Invalid:", n)
                pass
            else:
                # print("Part #", n)
                sum += int(n.value)

        print("Sum:", sum)
            
g = Grid("day3_input1.txt")
g.sum_all_parts()
