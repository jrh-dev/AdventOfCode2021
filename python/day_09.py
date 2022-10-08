import numpy as np

def find_basin(arr, coord):    

    in_basin = [[coord[0], coord[1]]]

    track_len = len(set([str(i) for i in in_basin]))

    run = True

    while run:
        for ii in in_basin:
        
            y = ii[0]
            x = ii[1]

            # north
            if (arr[y - 1, x] > arr[y,x]) & (arr[y - 1, x] < 9):
                in_basin.append([y - 1, x])

            # east
            if (arr[y, x + 1] > arr[y,x]) & (arr[y, x + 1] < 9):
                in_basin.append([y, x + 1])

            # south
            if (arr[y + 1, x] > arr[y,x]) & (arr[y + 1, x] < 9):
                in_basin.append([y + 1, x])

            # west
            if (arr[y, x - 1] > arr[y,x]) & (arr[y, x - 1] < 9):
                in_basin.append([y, x - 1])

        tmp = len(set([str(i) for i in in_basin]))

        if tmp == track_len:
            run = False
        else:
            track_len = tmp

    return tmp

# import and cleanse
f = open("day_09.txt", "r")

input = f.read().splitlines()

f.close()

x_len = len(input[0])

y_len = len(input)

input = "".join(input)

input = [int(char) for char in input]

arr = np.array(input)

arr = arr.reshape(y_len, x_len)

arr = np.pad(arr, pad_width=1, mode='constant', constant_values=10)

# Part 1 processing
low_point_val = []
low_point_coord = []

for ii in range(1, y_len + 1):
    for jj in range(1, x_len + 1):
        x, y = ii, jj
        if np.all(arr[x-1:x+2, y-1:y+2] >= arr[x,y]):
            low_point_val.append(arr[x,y] + 1)
            low_point_coord.append([x,y])
            arr[x,y] = 0

# Part 2 processing
basin_sizes = []

for ii in low_point_coord:
    basin_sizes.append(find_basin(arr, ii))

basin_sizes.sort(reverse = True)


# Part 1 answer
print(sum(low_point_val))

# Part 2 answer
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
