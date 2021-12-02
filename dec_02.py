# --- Day 2: Dive! ---
# https://adventofcode.com/2021/day/2

with open("./input/dec_02_input.txt", encoding="utf-8", mode="r") as f:
    course = [line.split() for line in f.read().splitlines()]

# Part One
# Simple solution O(n) time
depth, hoz_pos = 0, 0
for command in course:
    if command[0] == "forward":
        hoz_pos += int(command[1])
    elif command[0] == "down":
        depth += int(command[1])
    else:
        depth -= int(command[1])

print(depth * hoz_pos)


# Part Two
# Naive solution O(n) time
depth, hoz_pos, aim = 0, 0, 0
for command in course:
    if command[0] == "forward":
        hoz_pos += int(command[1])
        depth += aim * int(command[1])
    elif command[0] == "down":
        aim += int(command[1])
    else:
        aim -= int(command[1])

print(depth * hoz_pos)
