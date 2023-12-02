from os import walk
import re

class Calib:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            self.rows = f.read().splitlines()

    def get_digits_first_last(self, str):
        digits_only = re.sub('\D', '', str)
        out_str = digits_only[0] + digits_only[-1]
        return out_str

    def get_calib_sum(self):
        sum = 0
        for r in self.rows:
            try:
                sum += int(self.get_digits_first_last(r))
            except:
                print("Error processing:", r)
        return sum
 

c = Calib("day1_input1.txt")

print(c.get_calib_sum())
