import json
import math

class Packets:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            rows = f.read().splitlines()
        self.packets = [(json.loads(rows[i*3]), json.loads(rows[(i*3)+1])) for i in range(int(math.ceil(len(rows)/3)))]
        self.packets.insert(0, None) #Indexing is supposed to begin at 1

        self.unsorted = list()
        for i in range(1, len(self.packets)):
            self.unsorted.append(self.packets[i][0])
            self.unsorted.append(self.packets[i][1])
        self.unsorted.append([[2]])
        self.unsorted.append([[6]])

        for i in self.unsorted:
            print(i)

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

    def merge_sort(self, a):
        if len(a) == 1:
            return a
        split = int(math.ceil(len(a)/2))
        merged0 = self.merge_sort(a[:split])
        merged1 = self.merge_sort(a[split:])

        return self.merge(merged0, merged1)

    def merge(self, a, b):
        c = list()

        while (a and b):
            if self.is_correct_order((a[0],b[0])):
                c.append(a.pop(0))
            else:
                c.append(b.pop(0))
        while (a):
            c.append(a.pop(0))
        while (b):
            c.append(b.pop(0))

        return c

    def test_packets(self):
        sorted_correctly = list()
        for i in range(1,len(self.packets)):
            print("== Pair {} ==".format(i))
            x = self.is_correct_order(self.packets[i])
            print()
            if x:
                sorted_correctly.append(i)
        total = sum(sorted_correctly)
        print("Totals:", total)
        return total

    def sort_all(self):
        all_sorted = self.merge_sort(self.unsorted)
        all_sorted.insert(0,None) # Adjust to index at 1 (not 0)
        x = all_sorted.index([[2]])
        y = all_sorted.index([[6]])
        return x*y




# p = Packets("day13_test.txt")
p = Packets("day13_input.txt")
question_1 = p.test_packets()
question_2 = p.sort_all()

print()
print ("Question #1 solution:", question_1)
print ("Question #2 solution:", question_2)
