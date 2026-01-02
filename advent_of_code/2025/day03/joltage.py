with open('/home/mike/compile/playground/advent_of_code/2025/day3/test_input.txt', 'r') as f:
    test_data = f.read().splitlines()

with open('/home/mike/compile/playground/advent_of_code/2025/day3/puzzle_input.txt', 'r') as f:
    puzzle_data = f.read().splitlines()

def get_joltage_recurse_digits(bank: list, num_digits: int) -> tuple:
    num_digits -= 1
    if num_digits == 0:
        return max(bank)

    largest = max(bank[:-num_digits])    
    return_value = largest * (10 ** num_digits)
    idx = bank.index(largest)
    return return_value + get_joltage_recurse_digits(bank[idx + 1:], num_digits)

def total_max_joltage(battery_banks, total_digits):
    total = 0
    for bank in battery_banks:
        new_joltage = get_joltage_recurse_digits([int(b) for b in bank], total_digits)
        total += new_joltage
    return total

print("Max joltage total 2 digits test set:", total_max_joltage(test_data, 2))
print("Max joltage total 2 digits puzzle set:", total_max_joltage(puzzle_data, 2))
print("Max joltage total 12 digits test set:", total_max_joltage(test_data, 12))
print("Max joltage total 12 digits puzzle set:", total_max_joltage(puzzle_data, 12))
