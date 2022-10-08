
import numpy as np
import matplotlib.pyplot as plt

# Import and cleanse
f = open("day_13.txt", "r")
input = f.read().splitlines()
f.close()

def split_input(input):
    index = input.index('')
    return [input[:index], input[index + 1:]]

input = split_input(input)

for ii in range(len(input[0])):
    input[0][ii] = input[0][ii].split(',')

for ii in range(len(input[1])):
    input[1][ii] = input[1][ii].split(' ')[2]

cords = [[int(i) for i in l] for l in input[0]]

folds = input[1]

def fold(fold, cords):

    fold = fold.split("=")

    fold_on = int(fold[1])

    if fold[0] == 'y':
        xory = 1
    else:
        xory = 0

    to_rm = []

    for ii in range(len(cords)):
        test = cords[ii][xory]
        if test == fold_on:
            to_rm.append(ii)
        elif test > fold_on:
            cords[ii][xory] = fold_on - (test - fold_on)
        else:
            continue

    for rm in to_rm:
        cords.remove(rm)

    return cords


cords = fold(folds[0], cords)

# part 1 answer
len([list(y) for y in set([tuple(x) for x in cords])])

for ii in folds[1:]:
    cords = fold(ii, cords)

x_min = max([i[0] for i in cords])
y_min = max([i[1] for i in cords])

arr = np.zeros(shape=[y_min+1,x_min+1])

for i in cords:
    arr[i[1],i[0]] = 1

# part 2 answer (with a bit of squinting at the console)
print(arr)