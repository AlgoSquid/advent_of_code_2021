# --- Day 6: Lanternfish ---
# https://adventofcode.com/2021/day/6

from collections import deque
from functools import reduce


with open("./input/dec_06_input.txt", encoding="utf-8", mode="r") as f:
    timers = [int(timer) for timer in f.readline().split(",")]

def iterative_prediction(timers, day):
    """Simple iterative solution"""
    for _ in range(day):
        new_fish = 0
        for i in range(len(timers)):
            if timers[i] == 0:
                timers[i] = 6
                new_fish += 1
            else:
                timers[i] -= 1

        timers.extend([8]*new_fish)
    return len(timers)

def smart_iterative_prediction(timers, day):
    """Have a deque with the number of each fish in each age and rotate"""
    num_timers = deque()
    for i in range(9):
        num_timers.append(timers.count(i))

    for _ in range(day):
        spawns = num_timers.popleft()
        num_timers[6] += spawns
        num_timers.append(spawns)

    return reduce(lambda a, b: a + b, num_timers)

print(smart_iterative_prediction(timers, 256))
# print(iterative_prediction(timers, 256))
