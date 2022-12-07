def get_input():
    with open("day6_input.txt", "r") as f:
        return f.read().splitlines()

def got_preamble(new_char, buffer):
    buffer += new_char
    if len(buffer) > 3:
        if len(set(buffer[-4:])) == 4:
            return True, buffer
    return False, buffer

def stream_test(source):
    receive_buffer = ""
    for c in source:
        success, receive_buffer = got_preamble(c, receive_buffer)
        if success:
            print("Found preamble at:", len(receive_buffer))
            return
    print("No preamble found")

puzzle_stream = get_input()
stream_test(puzzle_stream[0])
