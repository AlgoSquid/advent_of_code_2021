# --- Day 14: Extended Polymerization ---
# https://adventofcode.com/2021/day/14

from math import ceil


with open("./input/dec_14_input.txt", encoding="utf-8", mode="r") as f:
    lines = f.read().splitlines()
    tmpl = lines[0]

    rules = {}
    for line in lines[2:]:
        pair, insertion = line.split(" -> ")
        rules[pair] = (pair[0] + insertion, insertion + pair[1])

# Create polymer as dict easy to apply rules on
polymer = {}
for i in range(len(tmpl) - 1):
    polymer[tmpl[i] + tmpl[i + 1]] = polymer.setdefault(tmpl[i] + tmpl[i + 1], 0) + 1

# Apply rules each step
steps = 40
for _ in range(steps):
    new_polymer = {}
    for p, val in polymer.items():
        for r in rules[p]:
            new_polymer[r] = new_polymer.setdefault(r, 0) + val

    polymer = new_polymer

# Count elements
elements = {}
for rule, amount in polymer.items():
    elements[rule[0]] = elements.setdefault(rule[0], 0) + amount
    elements[rule[1]] = elements.setdefault(rule[1], 0) + amount
elements = sorted([ceil(val / 2) for val in elements.values()])
print(elements[-1] - elements[0])