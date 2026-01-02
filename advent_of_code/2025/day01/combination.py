with open('/home/mike/test_input.txt', 'r') as f:
    test_data = f.read().splitlines()

with open('/home/mike/puzzle_input.txt', 'r') as f:
    puzzle_data = f.read().splitlines()

start_value = 50
lut = { 'L': -1, 'R': 1}

def convert_num(test_string):
    return lut[test_string[0]] * int(test_string[1:])

def cal_new(start_place, clicks, max_value):
    position = start_place + clicks + max_value
    return position % max_value

def find_combo(start_value, target_number, max_dial):
    count = 0
    position = start_value
    total_pos = max_dial + 1
    for val in test_data:
        clicks = convert_num(val)
        position = (position + clicks + total_pos) % total_pos
        if position == 0:
            count += 1
    return count

def find_frequency(start_value, target_number, max_dial):
    count = 0
    position = start_value
    
    for val in puzzle_data:
        delta = convert_num(val)
        dir = 1 if delta >= 0 else -1
        
        for _ in range(abs(delta)):
            position += dir
            if position > max_dial:
                position = 0
            if position < 0:
                position = 99
            if position == 0:
                count += 1
            
    return count

print("Answer:", find_combo(50, 0, 99))
print("Answer:", find_frequency(50, 0, 99))
