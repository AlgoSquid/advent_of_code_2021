# --- Day 12: Passage Pathing ---
# https://adventofcode.com/2021/day/12

from collections import deque
from copy import deepcopy


# Some notes can be re-visited (uppercase) and some cannot (lowercase)
# The 3 examples only has (lowercase - lowercase) and (uppercase - lowercase) edges
# There will therefore be no cycles and a finite set of solutions
# Usually an NP-Hard problem, but is this reduction P? - Yes at least O(N^2).


caves = {}
with open("./input/dec_12_input.txt", encoding="utf-8", mode="r") as f:
    for edge in f.read().splitlines():
        c1, c2 = edge.split("-")

        if c1 == "start":
            caves.setdefault(c1, []).append(c2)
        elif c2 == "start":
            caves.setdefault(c2, []).append(c1)
        else:
            caves.setdefault(c1, []).append(c2)
            caves.setdefault(c2, []).append(c1)

# Stack with tuples of cave to explore, visited lowercase caves, 
# and whether a small cave has been visited twice in this path 
stack = deque([("start", [], False)])
paths = 0
while stack:
    cave, visited, twice = stack.pop()

    # Lowercase caves cannot be revisited in path
    if cave == "end":
        paths += 1
        continue
    elif cave.islower():
        visited.append(cave)

    # Add new options to stack
    for c in filter(lambda x: x not in visited, caves[cave]):
        stack.append((c, deepcopy(visited), twice))

    # Add options to revist connected lowercase caves if possible
    if not twice:
        for c in filter(lambda x: x in visited, caves[cave]):
            stack.append((c, deepcopy(visited), True))

print(paths)