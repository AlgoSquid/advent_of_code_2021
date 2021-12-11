# --- Day 11: Dumbo Octopus ---
# https://adventofcode.com/2021/day/11


with open("./input/dec_11_input.txt", encoding="utf-8", mode="r") as f:
    octopus = [[int(char) for char in line] for line in f.read().splitlines()]

# Pad with zeroes around
octopus.insert(0, [0] * len(octopus))
octopus.append([0] * len(octopus))
for line in octopus:
    line.insert(0, 0)
    line.append(0)

def step():
    """Increase all energy levels"""
    flashes = []
    for i in range(1, len(octopus) - 1):
        for j in range(1, len(octopus[0]) - 1):
            octopus[i][j] += 1
            if octopus[i][j] == 10:
                flashes.append((i, j))
    return flashes

iterations, num_flashes = 1000, 0
for k in range(iterations):
    flashes = step()
    num_flashes_before_step = num_flashes

    while flashes:
        r, c = flashes.pop()
        octopus[r][c] = 0
        num_flashes += 1

        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                if 0 < octopus[i][j] < 10:
                    octopus[i][j] += 1
                    if octopus[i][j] == 10:
                        flashes.append((i, j))

    if num_flashes - num_flashes_before_step == 100:
        print(k + 1)
        break

print(num_flashes)