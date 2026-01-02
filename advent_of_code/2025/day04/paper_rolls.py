with open('/home/mike/compile/playground/advent_of_code/2025/day4/test_input.txt', 'r') as f:
    in_data = f.read().splitlines()
    test_data = list()
    for l in in_data:
        test_data.append([0 if b == '.' else 1 for b in l])

with open('/home/mike/compile/playground/advent_of_code/2025/day4/puzzle_input.txt', 'r') as f:
    in_data = f.read().splitlines()
    puzzle_data = list()
    for l in in_data:
        puzzle_data.append([0 if b == '.' else 1 for b in l])

def count_surrounding(data_set: list, x: int, y:int) -> int:
    subset = list()
    limit_left = x-1 if x > 0 else x
    limit_right = x+2

    rows = [y]
    if (y > 0):
        rows.append(y-1)
    if (y < len(data_set) - 1):
        rows.append(y+1)

    for i in rows:
        subset += data_set[i][limit_left:limit_right]

    return sum(subset) - data_set[y][x]

def get_accessible_roll_locs(data_set: list, surround_fewer_than: int) -> list:
    accessible_roll_locs = list()

    for y in range(len(data_set)):
        for x in range(len(data_set[0])):
            if data_set[y][x] == 1:
                if (surround_fewer_than > count_surrounding(data_set, x, y)):
                    accessible_roll_locs.append((x,y))
    return accessible_roll_locs

def remove_accessible(data_set: list, surround_fewer_than: int):
    locs = get_accessible_roll_locs(data_set, surround_fewer_than)
    for roll in locs:
        data_set[roll[1]][roll[0]] = 0
    return (data_set, len(locs))

def count_total_removals(data_set: list, surround_fewer_than: int):
    total = 0
    test_set = data_set
    while True:
        (test_set, just_removed) = remove_accessible(test_set, surround_fewer_than)
        total += just_removed
        if 0 == just_removed:
            break;
    return total

print("Total with fewer than 4 in test set:", len(get_accessible_roll_locs(test_data, 4)))
print("Total with fewer than 4 in puzzle set:", len(get_accessible_roll_locs(puzzle_data, 4)))
print("Total removed with fewer than 4 in test set:", count_total_removals(test_data, 4))
print("Total removed with fewer than 4 in puzzle set:", count_total_removals(puzzle_data, 4))
