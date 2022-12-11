class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.dirs = set()
        self.files = dict()

    def add_subdir(self, new_dir_name):
        self.dirs.add(Dir(new_dir_name, self))

    def add_file(self, f_name, f_size):
        self.files[f_name] = int(f_size)

    def get_files(self):
        return self.files

    def get_parent(self):
        if self.parent == None:
            return self
        else:
            return self.parent

    def get_name(self):
        return self.name

    def get_size(self):
        size = 0;
        for d in self.dirs:
            size += d.get_size()
        for f in self.files:
            size += self.files[f]
        return size

    def get_subdir(self, subdir_name):
        for d in self.dirs:
            if d.get_name() == subdir_name:
                return d
        return None

    def get_subdir_list(self):
        return [x.get_name() for x in self.dirs]

class CommandParser:
    root_dir = Dir("/", None)

    def __init__(self, f_name):
        with open(f_name, "r") as f:
            self.commands = f.read().splitlines()
            self.cur_dir = self.root_dir

    def print_commands(self):
        for line in self.commands:
            print(line)

    def get_dir_size(self):
        return self.root_dir.get_size()

    def tree(self, dir=root_dir, indent=0):
        print(indent*"  " + "-", dir.get_name(), "(dir)")
        for d in sorted(dir.get_subdir_list()):
            self.tree(dir.get_subdir(d), indent+1)
        files = dir.get_files()
        for f in sorted(files.keys()):
            print((indent+1)*"  " + "-", f, "(file, size={})".format(files[f]))


    def crawl_commands(self):
        for c in self.commands:
            tokens = c.split(" ")
            if tokens[0] == "$":
                if tokens[1] == "cd":
                    if tokens[2] == "..":
                        self.cur_dir = self.cur_dir.get_parent()
                    elif tokens[2] == "/":
                        self.cur_dir == self.root_dir
                    else:
                        self.cur_dir = self.cur_dir.get_subdir(tokens[2])
                '''
                elif tokens[1] == "ls":
                    #maybe don't need anything for this?
                '''
            elif tokens[0] == "dir":
                self.cur_dir.add_subdir(tokens[1])
            else:
                self.cur_dir.add_file(tokens[1], tokens[0])

# cp = CommandParser("day7_input.txt")
cp = CommandParser("day7_test.txt")
cp.crawl_commands()
cp.tree()

print("\nTotal size:", cp.get_dir_size())
