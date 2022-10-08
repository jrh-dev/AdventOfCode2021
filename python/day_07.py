
import numpy as np

def solve(n):
        return sum(range(1,n + 1))

f = open("day_07.txt", "r")

input = f.read().splitlines()

f.close()

input = input[0].split(",")

input = np.array([int(x) for x in input])

res = []

for ii in range(len(input + 1)):
    res.append(sum(abs(ii - input)))

# Part 1 answer
print(min(res))

res = []

for ii in range(1, len(input + 1)):
    res.append(sum([solve(x) if x > 1 else x for x in abs(ii - input)]))

# Part 2 answer
print(min(res))