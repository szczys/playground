from os import walk
import re

rpl_list = [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]

class Calib:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            self.rows = f.read().splitlines()

    def get_word_and_idx(self, calib, wordlist):
        idx_dict = dict()
        for w in wordlist:
            try:
                idx_dict[calib.index(w)] = w
            except:
                continue
        
        if len(idx_dict) != 0:
            rep_word = idx_dict[min(idx_dict)]
            return (str(wordlist.index(rep_word) + 1), min(idx_dict))
        return (None, None)

    def get_digit_and_idx(self, calib):
        digits = re.sub('\D', '', calib)
        if digits is None:
            return (None, None)

        return (digits[0], calib.index(digits[0]))

    def find_edge(self, calib, reverse=False):
        if reverse:
            calib = calib[::-1]
            wordlist = [ x[::-1] for x in rpl_list]
        else:
            wordlist = rpl_list

        found_word = self.get_word_and_idx(calib, wordlist)
        found_digit = self.get_digit_and_idx(calib)

        if found_digit[0] is None:
            return found_word[0]

        elif found_word[0] is None:
            return found_digit[0]

        elif found_digit[1] < found_word[1]:
            return found_digit[0]
        else:
            return found_word[0]
 
    def get_calib_sum(self):
        sum = 0
        for r in self.rows:
            calib = self.find_edge(r) + self.find_edge(r, reverse=True)
            sum += int(calib)
        return sum
 

c = Calib("day1_input1.txt")

print(c.get_calib_sum())
