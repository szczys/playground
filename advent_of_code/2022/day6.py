class elf_stream:
    def __init__(self):
        self.receive_buffer = ""
        self.elfstream = self.get_input()[0]

    def get_input(self):
        with open("day6_input.txt", "r") as f:
            return f.read().splitlines()

    def got_preamble(self, new_char, unique):
        self.receive_buffer += new_char
        if len(self.receive_buffer) >= unique:
            if len(set(self.receive_buffer[-unique:])) == unique:
                return True
        return False

    def stream_find_preamble(self, source, unique_count):
        self.receive_buffer = ""
        for c in source:
            success = self.got_preamble(c, unique_count)
            if success:
                print("Found preamble at:", len(self.receive_buffer))
                return
        print("No preamble found")

transmission = elf_stream()
transmission.stream_find_preamble(transmission.elfstream, 4)
transmission.stream_find_preamble(transmission.elfstream, 14)
