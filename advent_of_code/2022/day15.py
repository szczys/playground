import re

class Sensor:
    def __init__(self, sensor_x, sensor_y, beacon_x, beacon_y):
        self.x = int(sensor_x)
        self.y = int(sensor_y)
        self.beacon_x = int(beacon_x)
        self.beacon_y = int(beacon_y)
        self.distance = abs(self.x - self.beacon_x) + abs(self.y - self.beacon_y)
        self.y_start = self.y-self.distance
        self.y_end = self.y+self.distance

    def __repr__(self):
        return "Sensor: {},{} Beacon: {},{} Distance: {} Y_Start: {} Y_End: {}".format(
            self.x, self.y, self.beacon_x, self.beacon_y, self.distance,
            self.y_start, self.y_end)

    def get_spread(self, y):
        if self.y_start <= y <= self.y_end:
            offset = self.distance-abs(self.y - y)
            return (self.x-offset, self.x+offset)
        else:
            return None

class Survey:
    def __init__(self, f_name):
        with open(f_name, "r") as f:
            rows = f.read().splitlines()
        self.sensors = list()

        num_filter = re.compile(r'[\d-]+')
        for r in rows:
            self.sensors.append(Sensor(*num_filter.findall(r)))

        self.max = max([i.distance for i in self.sensors])

    def print(self):
        for s in self.sensors:
            print(s)
        print("Max distance:", self.max)
        print()

    def get_spread(self, target_y, sensor):
        offset = abs(target_y - sensor.y)

        if offset > sensor.distance:
            return set()
        elif offset == sensor.distance:
            return {sensor.x}
        else:
            spread = sensor.distance - offset
            return set(range(sensor.x-spread, sensor.x+spread+1))

    def calc_coverage(self, y, return_sets=False):
        y_range = range(y-self.max, y+self.max+1)
        covered = set()
        beacons = set()
        for s in self.sensors:
            if s.beacon_y == y:
                beacons.add(s.beacon_x)
            if s.y in y_range:
                covered = covered | self.get_spread(y, s)
        if return_sets:
            return covered,beacons
        for b in beacons:
            covered.discard(b)
        return len(covered)

    def graph_coverage(self):
        for j in range(0,23):
            covered, beacons = self.calc_coverage(j, True)
            out = ""
            for i in range(-2,36):
                if i in beacons:
                    out += 'B'
                elif i in covered:
                    out += '#'
                else:
                    out += '.'
            print(out)
            valid_slice = out[2:23]
            if '.' in valid_slice:
                print(j, valid_slice.index('.'))

    def find_unoccupied(self, limit_x, limit_y):
        '''
        1. Get y begin and end numbers for all sensors
        2. use algorithm to get x begin and end numbers for any sensor in a given y
        3. check to see if there are any gaps in the overlap
        '''
        for row in range(limit_y[0], limit_y[1]+1):
            span_list = list()
            for s in self.sensors:
                span = s.get_spread(row)
                if span:
                    span_list.append(span)
            span_list.sort()
            gap_list = list()
            parsed_list = [span_list[0]]
            for sp in span_list[1:]:
                left = parsed_list[-1][1]
                right = sp[0]
                if left < right-1:
                    gap_list.append((left+1, right-1))
                if sp[1] > left:
                    parsed_list.append(sp)
            if len(gap_list) > 0:
                print("Found gap at row: {} x-value: {}".format(row, gap_list))
                return ((gap_list[0][0]*4000000)+row)

# s = Survey("day15_test.txt")
# s.graph_coverage()
# solution_1 = s.calc_coverage(10)
# solution_2 = s.find_unoccupied((0,20), (0,20))

s = Survey("day15_input.txt")
solution_1 = s.calc_coverage(2000000)
solution_2 = s.find_unoccupied((0,4000001), (0,4000001))

print("Solution #1:", solution_1)
print("Solution #2:", solution_2)
