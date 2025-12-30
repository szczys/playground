with open('/home/mike/compile/playground/advent_of_code/2025/day2/test_input.txt', 'r') as f:
    test_data = f.read().split(',')

with open('/home/mike/compile/playground/advent_of_code/2025/day2/puzzle_input.txt', 'r') as f:
    puzzle_data = f.read().split(',')

def is_invalid(num):
    str_num = str(num)
    str_len = len(str_num)
    if str_len % 2 != 0:
        return False
    
    half = int(str_len / 2)
    return str_num[:half] == str_num[half:]

def count_invalid(start, finish):
    count = 0
    while start <= finish:
        if is_invalid(start):
            count += 1
        start += 1
    return count

def total_invalid(start, finish):
    total = 0
    while start <= finish:
        if is_invalid(start):
            total += start
        start += 1
    return total

def test_puzzle_one(in_data, label):
    total = 0
    for d in in_data:
        start = int(d.split('-')[0])
        end = int(d.split('-')[1]) 
        total += total_invalid(start,end)
    print(label, total)

def is_repeating_invalid(num):
    num_str = str(num)
    if len(num_str) < 2:
        return False
    if num_str[0] * len(num_str) == num_str:
        return True
    count = 1
    while True:
        count += 1
        div = len(num_str) / count
        if count > div:
            break
        if len(num_str) % count != 0:
            continue
        div = int(div)
        if num_str[:count] * div == num_str:
            return True
        if num_str[:div] * count == num_str:
            return True
    return False

def find_repeating_invalid(start, finish):
    found = list()
    while start <= finish:
        if is_repeating_invalid(start):
            found.append(start)
        start += 1
    return found

def test_puzzle_two(in_data, label):
    found = list()
    for d in in_data:
        start = int(d.split('-')[0])
        end = int(d.split('-')[1]) 
        found += find_repeating_invalid(start,end)
    print(label, sum(found))

test_puzzle_one(test_data, "Test total:")
test_puzzle_one(puzzle_data, "Puzzle1 total:")
test_puzzle_two(test_data, "Test repeating total:")
test_puzzle_two(puzzle_data, "Puzzle2 total:")
