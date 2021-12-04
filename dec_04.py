# --- Day 4: Giant Squid ---
# https://adventofcode.com/2021/day/4


# Create list of lists of bits
with open("./input/dec_04_input.txt", encoding="utf-8", mode="r") as f:
    lines = [line for line in f.read().splitlines()]

# Retrieve data
draws = [int(num) for num in lines[0].split(",")]
raw_boards, board = [], []
for line in lines[1:]:
    if line == "":
        board = []
        continue

    board.append([int(num) for num in line.split(" ") if num != ""])
    if len(board) == 5:
        raw_boards.append(board)

""" Data structure and algorithm description

Each board is represented as a dict and two lists. The two list are of length 5 and
represent the columns and rows of the board. The dict contains the numbers as keys and
references to the lists as values. Such that a number has references to the col and row
that it is a part of. 

With each draw check all the dicts for the number and if it exists, get the two
references in the lists and add 1 to the values. If the value is 5 afterwards, we
have a winner. When a number has been drawn it is removed from the dict.

In order to solve part two we just count number of bingos and terminate when we hit the
last one.
"""

# Construct data structures
def construct_ds():
    boards = []
    for board in raw_boards:
        board_dict, cols, rows = {}, [0]*5, [0]*5
        for r in range(5):
            for c in range(5):
                board_dict[board[r][c]] = (r, c)
        boards.append([board_dict, cols, rows])

    return boards


# Perform algorithm - Part 1
boards = construct_ds()
bingo = False
for num in draws:
    for board in boards:
        if num in board[0]:
            r, c = board[0][num]
            board[1][r] +=1
            board[2][c] +=1

            # Remove number since it has been drawn
            board[0].pop(num)

            # Check for BINGO
            if board[1][r] == 5 or board[2][c] == 5:
                bingo = True
                break

    if bingo:
        # Print the result of the first board to win
        print(sum(board[0].keys()) * num)
        break


# Perform algorithm - Part 2
boards = construct_ds()
num_bingos, last_bingo = 0, False
for num in draws:
    for board in boards:
        if num in board[0]:
            r, c = board[0][num]
            board[1][r] +=1
            board[2][c] +=1

            # Remove number since it has been drawn
            board[0].pop(num)

            # Check for BINGO
            if board[1][r] == 5 or board[2][c] == 5:
                num_bingos += 1
                if num_bingos == len(boards):
                    last_bingo = True
                    break
                else:
                    # Remove all keys so the board cannot bingo anymore
                    board[0] = {}

    if last_bingo:
        # Print the result of the last board to win
        print(sum(board[0].keys()) * num)
        break
