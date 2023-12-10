def get_numlist(str_list):
    return [int(x) for x in str_list.split(' ')]

def exrange(start, members):
    return range(start, start+members)

class MRange:
    def __init__(self, range_list):
        self.dst = range_list[0]
        self.src = range_list[1]
        self.r = range_list[2]

    def __repr__(self):
        return f"[Dst: {self.dst}, Src={self.src}, Range={self.r}]"

class Map:
    def __init__(self, name, id, rangelist):
       self.name = name
       self.id = id
       self.ranges = rangelist

    def __repr__(self):
        return f"Name: {self.name} Id: {self.id} Ranges: {self.ranges}"

    def get_destination(self, value, show_work = False):
        for this_range in self.ranges:
            s_range = exrange(this_range.src, this_range.r)
            if value in s_range:
                s_idx = s_range.index(value)
                solution = exrange(this_range.dst, this_range.r)[s_idx]
                if (show_work):
                    print(solution)
                return solution

        # Default
        if (show_work):
            print(value)
        return value

class Almanac:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            blocks = f.read().split("\n\n")

        self.seeds = [int(x) for x in get_numlist(blocks[0].split("seeds: ")[1])]

        self.maps = list()

        for i,m in enumerate(blocks[1:]):
            m = m.rstrip('\n').split('\n')
            name = m[0].split(" map:")[0]
            ranges = list()
            for r in m[1:]:
                ranges.append(MRange(get_numlist(r)))

            self.maps.append(Map(name, i, ranges))

    def find_dest(self, src_idx, dest_idx, value):
        cur_idx = src_idx
        data = value

        while cur_idx < len(self.maps):
            data = self.maps[cur_idx].get_destination(data, show_work=False)
            if cur_idx == dest_idx:
                return data
            else:
                cur_idx += 1

        return None

    def process_seeds(self, dest_idx):
        dests = list()
        for s in self.seeds:
            dest = self.find_dest(0, dest_idx, s)
            dests.append(dest)
            print("Source:", s, "Destination", dest)
        print()
        print("Lowest: ", min(dests))


a = Almanac("day5_input1.txt")
a.process_seeds(6)
