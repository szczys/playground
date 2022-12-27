import json
import math

class Packets:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            rows = f.read().splitlines()
        self.packets = [(json.loads(rows[i*3]), json.loads(rows[(i*3)+1])) for i in range(int(math.ceil(len(rows)/3)))]
        self.packets.insert(0, None) #Indexing is supposed to begin at 1

    def is_correct_order(self, t, indent=""):
        left = t[0]
        right = t[1]

        print("{}- Compare {} vs {}".format(indent, left, right))

        # test for mismatch
        if type(left) != type(right):
            if type(left) == int:
                print("{}- Mixed types; convert {} to [{}] and retry comparison".format(indent+"  ", "left", left))
                left = [left]
            elif type(right) == int:
                print("{}- Mixed types; convert {} to [{}] and retry comparison".format(indent+"  ", "right", right))
                right = [right]
            return self.is_correct_order((left, right), indent+"  ")


        for i in range(len(left)):
            L = left[i]
            try:
                R = right[i]
            except:
                # right ran out of items and shouldn't have
                print("{}- Right side ran out of items, so inputs are **not** in the right order".format(indent+"  "))
                return False


            if type(L) == list or type(R) == list:
                # Always step into lists
                result = self.is_correct_order((L,R), indent+"  ")
                if result == None:
                    continue
                else:
                    return result


            print("{}- Compare {} vs {}".format(indent+"  ", L, R))
            if L > R:
                print("{}- Right side is smaller, so inputs are **not** in the right order".format(indent+"    "))
                return False
            elif L < R:
                print("{}- Left side is smaller, so inputs are in the right order".format(indent+"    "))

                print("  ")
                return True

        else:
            if len(left) < len(right):
                print("{}- Left side ran out of items, so inputs are in the right order".format(indent+"  "))
                return True
        return None # Returning True here will allow inner recursion to continue

    def test_packets(self):
        sorted_correctly = list()
        for i in range(1,len(self.packets)):
            print("== Pair {} ==".format(i))
            x = self.is_correct_order(self.packets[i])
            print()
            if x:
                sorted_correctly.append(i)
        print("Totals:", sum(sorted_correctly))




# p = Packets("day13_test.txt")
p = Packets("day13_input.txt")
p.test_packets()
