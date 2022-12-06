import string

def get_input():
    with open("day3_input.txt", "r") as f:
        return f.read().splitlines()

def stored_wrong(packing_list):
    half_len = int(len(packing_list)/2)
    comp_1 = packing_list[:half_len]
    comp_2 = packing_list[half_len:]
    for i in set(comp_1):
        if i in comp_2:
            return i

def get_score(letter):
    return string.ascii_letters.index(letter)+1

def tally_scores(all_packing_lists):
    score = 0
    for p_list in all_packing_lists:
        score += get_score(stored_wrong(p_list))
    return score

def find_badge(group):
    badge = [x for x in set(group[0]) if x in group[1] and x in group[2]]
    return badge[0]

def tally_badges(all_packing_lists):
    score = 0
    for i in range(0, len(all_packing_lists), 3):
        badge = find_badge(all_packing_lists[i:i+3])
        score += get_score(badge)
    return score

lines = get_input()
print()
print("Cumalitive priority:", tally_scores(lines))
print("Badge priority:", tally_badges(lines))
