# --- Day 10: Syntax Scoring ---
# https://adventofcode.com/2021/day/10

from collections import deque


with open("./input/dec_10_input.txt", encoding="utf-8", mode="r") as f:
    lines = f.read().splitlines()

corrupt_score_table = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
incomplate_score_table = {
    40: 1,
    91: 2,
    123: 3,
    60: 4
}

corrupt_score, incomplete_scores = 0, [] 
for line in lines:
    stack = deque()
    for char in line:
        if char in "<({[":
            stack.append(ord(char))
        else:
            if ord(char) - stack.pop() not in (1,2):
                corrupt_score += corrupt_score_table[char]
                break
    else:
        score = 0
        stack.reverse()
        for char in stack:
            score = score * 5 + incomplate_score_table[char]

        if score > 0:
            incomplete_scores.append(score)
            
print(corrupt_score, sorted(incomplete_scores)[len(incomplete_scores)//2])