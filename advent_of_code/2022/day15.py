import re

class Sensor:
    def __init__(self, sensor_x, sensor_y, beacon_x, beacon_y):
        self.x = int(sensor_x)
        self.y = int(sensor_y)
        self.beacon_x = int(beacon_x)
        self.beacon_y = int(beacon_y)
        self.distance = abs(self.x - self.beacon_x) + abs(self.y - self.beacon_y)
    def __repr__(self):
        return "Sensor: {},{} Beacon: {},{} Distance: {}".format(self.x, self.y, self.beacon_x, self.beacon_y, self.distance)

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
            return []
        elif offset == sensor.distance:
            return [sensor.x]
        else:
            spread = sensor.distance - offset
            return range(sensor.x-spread, sensor.x+spread+1)

    def calc_coverage(self, y):
        y_range = range(y-self.max, y+self.max+1)
        covered = list()
        beacons = list()
        for s in self.sensors:
            if s.beacon_y == y:
                beacons.append(s.beacon_x)
            if s.y in y_range:
                covered.extend(self.get_spread(y, s))
        covered = set(covered)
        for b in beacons:
            covered.discard(b)
        return len(covered)

# s = Survey("day15_test.txt")
# solution_1 = s.calc_coverage(10)
s = Survey("day15_input.txt")
solution_1 = s.calc_coverage(2000000)

print("Solution #1:", solution_1)
