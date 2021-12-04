# --- Day 3: Binary Diagnostic ---
# https://adventofcode.com/2021/day/3


# Create list of lists of bits
with open("./input/dec_03_input.txt", encoding="utf-8", mode="r") as f:
    report = [[int(char) for char in line] for line in f.read().splitlines()]

# Part One: Power consumption
sums = [sum(x) for x in zip(*report)]

num_bits = len(report[0])
gamma, epsilon = 0, 0
for i in range(num_bits):
    if sums[i] > len(report)/2:
        gamma += 2**(num_bits-i-1)
    else:
        epsilon += 2**(num_bits-i-1)

print(gamma, epsilon, gamma * epsilon)


# Part Two: Life support
def sum_and_filter(numbers, place, rating):
    sums = [sum(x) for x in zip(*numbers)]

    def oxy_filter_func(num):
        if sums[place] >= len(numbers)/2 and num[place]:
            return True
        elif sums[place] < len(numbers)/2 and not num[place]:
            return True
        else:
            return False

    def co2_filter_func(num):
        if sums[place] < len(numbers)/2 and num[place]:
            return True
        elif sums[place] >= len(numbers)/2 and not num[place]:
            return True
        else:
            return False

    if rating == "oxy":
        return list(filter(oxy_filter_func, numbers))
    else:
        return list(filter(co2_filter_func, numbers))

oxy_report = co2_report = report
num_bits = len(report[0])
oxy, co2 = 0, 0
for i in range(num_bits):
    if len(oxy_report) > 1:
        oxy_report = sum_and_filter(oxy_report, i, "oxy")
    
    if len(co2_report) > 1:
        co2_report = sum_and_filter(co2_report, i, "co2")

    if oxy_report[0][i]:
        oxy += 2**(num_bits-i-1)
    
    if co2_report[0][i]:
        co2 += 2**(num_bits-i-1)

print(oxy, co2, oxy * co2)