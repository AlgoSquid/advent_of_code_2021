# --- Day 7: The Treachery of Whales ---
# https://adventofcode.com/2021/day/7

from functools import reduce
from math import floor

with open("./input/dec_07_input.txt", encoding="utf-8", mode="r") as f:
    positions = [int(pos) for pos in f.readline().split(",")]

def calculate_fuel(positions, pos):
    return reduce(lambda x, y: x + abs(y - pos), positions, 0)


def calculate_crab_fuel(positions, pos):
    return reduce(lambda x, y: x + abs(y - pos) * (abs(y - pos) + 1) / 2, positions, 0)


def calc_fuel(positions, fuel_func):
    # Start out with median
    start = sorted(positions)[floor(len(positions)/2)]
    s_fuel = fuel_func(positions, start)

    # Try to find the nearest plateu
    fuel, val = s_fuel, start
    for i in range(start, max(positions)):
        new_f = fuel_func(positions, i)

        if new_f > fuel:
            break
        else:
            fuel, val = new_f, i
            print(val, fuel)

    for i in range(start, min(positions), -1):
        new_f = fuel_func(positions, i)

        if new_f > fuel:
            break
        else:
            fuel, val = new_f, i
            print(val, fuel)

    return val, fuel

print(calc_fuel(positions, calculate_fuel))
print(calc_fuel(positions, calculate_crab_fuel))