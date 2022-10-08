import pandas as pd

f = open("Coding/AdventOfCode_2021_python/day_1.txt", "r")

input = f.readlines()

f.close()

input = list(map(int, input))

input = pd.Series(input)

# Part 1 answer
print(sum(input.diff(periods = 1) > 0))

input = input.rolling(3).sum()

# Part 2 answer
print(sum(input.diff(periods = 1) > 0))
