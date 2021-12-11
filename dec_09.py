# --- Day 9: Smoke Basin ---
# https://adventofcode.com/2021/day/9

from functools import reduce
from collections import deque


with open("./input/dec_09_input.txt", encoding="utf-8", mode="r") as f:
    lines = [[int(char) for char in line] for line in f.read().splitlines()]


def search_basin(location):
    """BFS of basins from given location"""
    stack, inspected, size = deque([location]), {location}, 0
    
    while stack:
        r, c = stack.pop()
        size += 1

        if c > 0 and (r, c - 1) not in inspected and lines[r][c - 1] != 9:
            stack.append((r, c - 1))
            inspected.add((r, c - 1))

        if c < len(lines[0]) - 1 and (r, c + 1) not in inspected and lines[r][c + 1] != 9:
            stack.append((r, c + 1))
            inspected.add((r, c + 1))

        if r > 0 and (r - 1, c) not in inspected and lines[r - 1][c] != 9:
            stack.append((r - 1, c))
            inspected.add((r - 1, c))

        if r < len(lines) - 1 and (r + 1, c) not in inspected and lines[r + 1][c] != 9:
            stack.append((r + 1, c))
            inspected.add((r + 1, c))

    return size

basins, risk = [], 0
for r in range(len(lines)):
    for c in range(len(lines[0])):
        height = lines[r][c]
        if (
            (c == 0 or height < lines[r][c - 1])
            and (c == len(lines[0]) - 1 or height < lines[r][c + 1])
            and (r == 0 or height < lines[r - 1][c])
            and (r == len(lines) - 1 or height < lines[r + 1][c])
        ):
            risk += height + 1
            basins.append(search_basin((r, c)))

print(risk, reduce(lambda a, b: a * b, sorted(basins, reverse=True)[0:3]))