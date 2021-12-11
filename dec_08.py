# --- Day 8: Seven Segment Search ---
# https://adventofcode.com/2021/day/8

from collections import Counter


with open("./input/dec_08_input.txt", encoding="utf-8", mode="r") as f:
    lines = [[["".join(sorted(letters)) for letters in digits.split()] for digits in line.split(" | ")] for line in f.read().splitlines()]

def contains(s1, s2):
    c1, c2 = Counter(s1), Counter(s2)
    return all(c1[c] <= c2[c] for c in s1)

total_easy, total_values = 0, 0
for line in lines:
    digits, output = sorted(line[0], key=lambda x: len(x)), line[1]
    
    converted = {
        1: digits[0],
        7: digits[1],
        4: digits[2],
        8: digits[9]
    }
    digits = [d for d in digits if d not in (1, 4, 7, 8)]

    for d in digits:
        # 3 is 7 + 2 letters
        if len(d) == 5 and contains(converted[7], d):
            converted[3] = d

        # 9 is 4 + 2 letters
        elif len(d) == 6 and contains(converted[4], d):
            converted[9] = d

    digits.remove(converted[3])
    digits.remove(converted[9])

    for d in digits:
        # 5 is 9 - 1 letters
        # Depends on 9 is found
        if len(d) == 5 and contains(d, converted[9]):
            converted[5] = d

        # 0 is 7 + 3 letters and not 9
        # Depends on 9 is found
        elif len(d) == 6 and contains(converted[7], d):
            converted[0] = d

    digits.remove(converted[5])
    digits.remove(converted[0])

    for d in digits:
        # 2 is the last of length 5
        # Depends on 9, 3 and 5
        if len(d) == 5:
            converted[2] = d

        # 6 is the last of length 6
        # Depends on 0 and 9
        elif len(d) == 6:
            converted[6] = d

    converted = {v: k for k, v in converted.items()}
    i_output = [converted[d] for d in output]

    total_easy += sum([1 for d in i_output if d in (1, 4, 7, 8)])
    total_values += int("".join([str(d) for d in i_output]))

print(total_easy, total_values)
