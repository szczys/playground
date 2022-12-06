def get_input():
    with open("day4_input.txt", "r") as f:
        return f.read().splitlines()

def get_set(str_pair):
    pair = str_pair.split('-')
    return set(range(int(pair[0]), int(pair[1])+1))

def test_sets(encoded_pair):
    return_vals = [False, False]
    pairs = encoded_pair.split(',')
    set_group = [get_set(pairs[0]), get_set(pairs[1])]
    if set_group[0].issubset(set_group[1]) or set_group[1].issubset(set_group[0]):
        return_vals[0] = True
    if set_group[0].intersection(set_group[1]):
        return_vals[1] = True
    return return_vals

def tally_scores(l):
    scores = [0,0]
    for i in l:
        pairing = test_sets(i)
        if pairing[0]:
            scores[0] += 1
        if pairing[1]:
            scores[1] += 1
    return scores

lines = get_input()
set_scores = tally_scores(lines)
print("Fully contained:", set_scores[0], '\n', "Overlap:", set_scores[1])
