# --- Day 1: Sonar Sweep ---
# https://adventofcode.com/2021/day/1

with open("./input/dec_01_input.txt", encoding="utf-8", mode="r") as f:
    report = [int(i) for i in f.read().splitlines()]

# Part One
# Naive solution O(n) time
increases = 0
for i in range(1, len(report)):
    if report[i] > report[i-1]:
        increases += 1

print(increases)


# Part Two
# Naive solution O(n) time
increases = 0
for i in range(3, len(report)):
    if sum(report[i-2:i+1]) > sum(report[i-3:i]):
        increases += 1

print(increases)


# Bonus ugly one liner
print(len(list(filter(lambda x: x[1] > x[0], zip(report, report[1:])))))