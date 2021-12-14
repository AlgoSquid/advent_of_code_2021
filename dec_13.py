# --- Day 13: Transparent Origami ---
# https://adventofcode.com/2021/day/13


with open("./input/dec_13_input.txt", encoding="utf-8", mode="r") as f:
    coords, folds = [], []
    for line in f.readlines():
        if "," in line:
            coords.append([int(num) for num in line.split(",")])
        elif "fold" in line:
            fold = line.split("=")
            folds.append((fold[0][-1], int(fold[1])))

for fold in folds:
    if fold[0] == "x":
        coords = sorted(coords, key=lambda x: x[0])
        coords = [[coord[0] - 2*(coord[0] - fold[1]), coord[1]] if coord[0] > fold[1] else coord for coord in coords]
    else:
        coords = sorted(coords, key=lambda x: x[1])
        coords = [[coord[0], coord[1] - 2*(coord[1] - fold[1])] if coord[1] > fold[1] else coord for coord in coords]

# Part 1
print(len(set([tuple(coord) for coord in coords])))

# Part 2
p_coords = [
    ["." for _ in range(max([coord[0] for coord in coords]) + 1)]
    for _ in range(max([coord[1] for coord in coords]) + 1)
] 
for coord in coords:
    p_coords[coord[1]][coord[0]] = "#"

for line in p_coords:
    print(line)