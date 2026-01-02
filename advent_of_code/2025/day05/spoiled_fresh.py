def squash_ranges(in_data: list) -> list:
    test_ranges = list()
    for r in in_data:
        processed_bounds = False
        for t in test_ranges:
            if r[1] < t[0] - 1:
                # comes before set
                continue

            if r[0] > t[1] + 1:
                # comes after set
                continue

            if r[0] >= t[0] and r[1] <= t[1]:
                # is inside existing set
                processed_bounds = True
                break

            if r[0] <= t[0] and r[1] <= t[0]:
                # expands beginning of set
                t[0] = r[0]
                processed_bounds = True
                break

            if r[1] >= t[1] and r[0] >= t[0]:
                # expands end of set
                t[1] = r[1]
                processed_bounds = True
                break

            if r[0] < t[0] - 1 and r[1] > t[1] + 1:
                # surrounds existing set
                t[0] = r[0]
                t[1] = r[1]
                processed_bounds = True
                break

        if processed_bounds is False:
            test_ranges.append(r)

    test_ranges = sorted(test_ranges, key=lambda x: x[0])
    return test_ranges

def load_input(filename):
    with open(filename, 'r') as f:
        in_data = f.read().splitlines()
        idx = in_data.index('')

        test_nums = list()
        for n in in_data[idx + 1:]:
            test_nums.append(int(n))

        source_ranges = list()
        test_ranges = list()
        for d in in_data[:idx]:
            bound = d.split('-')
            test_ranges.append([int(bound[0]), int(bound[1])])

        while test_ranges != source_ranges:
            source_ranges = test_ranges
            test_ranges = list()
            test_ranges = squash_ranges(source_ranges)


    return (test_ranges, test_nums)

(test_ranges, test_nums) = load_input('/home/mike/compile/playground/advent_of_code/2025/day5/test_input.txt')

(puzzle_ranges, puzzle_nums) = load_input('/home/mike/compile/playground/advent_of_code/2025/day5/puzzle_input.txt')

def total_in_set(this_set: list, test_nums: list) -> int:
    fresh = list()
    start_count = len(test_nums)

    for t in test_nums:
        for r in this_set:
            if t >= r[0] and t <= r[1]:
                fresh.append(t)
                break
    return len(fresh)


def get_total_fresh_count(count_set: list) -> int:
    total = 0
    for r in count_set:
        total += r[1] - r[0] + 1
    return total

print("Total fresh in test nums:", total_in_set(test_ranges, test_nums))
print("Total fresh in puzzle nums:", total_in_set(puzzle_ranges, puzzle_nums))
print("Total fresh ids in test:", get_total_fresh_count(test_ranges))
print("Total fresh ids in puzzle:", get_total_fresh_count(puzzle_ranges))
