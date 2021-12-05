# --- Day 5: Hydrothermal Venture ---
# https://adventofcode.com/2021/day/5


class Line():
    def __init__(self, line_str):
        (self.x1, self.y1), (self.x2, self.y2) = [[int(c) for c in p_str.split(",")] for p_str in line_str.split(" -> ")]

    def is_hoz(self) -> bool:
        return self.y1 == self.y2

    def is_ver(self) -> bool:
        return self.x1 == self.x2

    def is_diag(self) -> bool:
        return abs(self.x1 - self.x2) == abs(self.y1 - self.y2)

    def points_in_line(self) -> list:
        if self.is_hoz():
            if self.x1 <= self.x2:
                return [f"{x},{self.y1}" for x in range(self.x1, self.x2 + 1)]
            else:
                return [f"{x},{self.y1}" for x in range(self.x2, self.x1 + 1)]

        elif self.is_ver():
            if self.y1 <= self.y2:
                return [f"{self.x1},{y}" for y in range(self.y1, self.y2 + 1)]
            else:
                return [f"{self.x1},{y}" for y in range(self.y2, self.y1 + 1)]

        else:
            m = (self.y1 - self.y2) / (self.x1 - self.x2)
            c = self.y1 - self.x1 * m

            if self.x1 <= self.x2:
                return [f"{x},{int(m * x + c)}" for x in range(self.x1, self.x2 + 1)]
            else:
                return [f"{x},{int(m * x + c)}" for x in range(self.x2, self.x1 + 1)]

    def __repr__(self) -> str:
        return f"{self.x1},{self.y1} -> {self.x2},{self.y2}"

with open("./input/dec_05_input.txt", encoding="utf-8", mode="r") as f:
    lines = [Line(line_str) for line_str in f.read().splitlines()]

diagram = {}
for line in lines:
    if line.is_hoz() or line.is_ver() or line.is_diag():
        for p in line.points_in_line():
            diagram[p] = diagram.setdefault(p, 0) + 1

print(len(list(filter(lambda v: v > 1, diagram.values()))))