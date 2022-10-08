import itertools
from collections import Counter

def get_range(in_0, in_1):
    
    in_0 = int(in_0)
    in_1 = int(in_1)

    if in_0 > in_1:
        return list(range(in_0, in_1 - 1, -1))
    else:
        return list(range(in_0, in_1 + 1, 1))


def diag_product(x, y):
    out = []
    for ii in range(len(x)):
        out.append((x[ii], y[ii]))
    return out

def x_product(x, y):
    out = []
    for ii in range(len(y)):
        out.append((x, y[ii]))
    return out

def y_product(x, y):
    out = []
    for ii in range(len(x)):
        out.append((x[ii], y))
    return out

def process(input, allow_diag):

    hashed = []

    for ii in input:
        x = []
        y = []

        tmp = ii.split(" -> ")
        x.append(tmp[0].split(","))
        y.append(tmp[1].split(","))

        if not any([x[0][0] == y[0][0], x[0][1] == y[0][1]]):
            if allow_diag:
              x_range = get_range(x[0][0], y[0][0])
              y_range = get_range(x[0][1], y[0][1])
              z = diag_product([str(i) for i in x_range], [str(i) for i in y_range])
            else:
                continue
        elif x[0][0] == y[0][0]:
             x_range = x[0][0]
             y_range = get_range(x[0][1], y[0][1])
             z = x_product(str(x_range), [str(i) for i in y_range])
        else:
            x_range = get_range(x[0][0], y[0][0])
            y_range = x[0][1]
            z = y_product([str(i) for i in x_range], str(y_range))

        for i in z:
            hashed.append(hash(i))

    return hashed

def intersections(input):
    cnt = Counter(input)
    return len([k for k, v in cnt.items() if v > 1])

# Setup
f = open("day_05.txt", "r")

input = f.read().splitlines()

f.close()

processed = process(input, False)

# Part 1 answer
print(intersections(processed))

processed = process(input, True)

# Part 2 answer
print(intersections(processed))