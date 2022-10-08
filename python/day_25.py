import numpy as np

def move(grid, y_len, x_len):
    run = True
    itr = 0

    while run and itr < 1000:
        last_state = grid.copy()
        
        east = np.where(grid == ">")

        move_east = []

        for ii in range(0, len(east[0])):
            y = east[0][ii]
            x = east[1][ii]
            xo = x + 1
            if xo >= x_len:
                xo = 0

            if grid[y, xo] == ".":
                move_east.append(([y, x], [y, xo]))        

        for ii in range(0, len(move_east)):
            grid[move_east[ii][0][0], move_east[ii][0][1]] = "."
            grid[move_east[ii][1][0], move_east[ii][1][1]] = ">"

        south = np.where(grid == "v")

        move_south = []

        for ii in range(0, len(south[0])):
            y = south[0][ii]
            x = south[1][ii]
            yo = y + 1
            if yo >= y_len:
                yo = 0

            if grid[yo, x] == ".":
                move_south.append(([y, x], [yo, x]))

        for ii in range(0, len(move_south)):
            grid[move_south[ii][0][0], move_south[ii][0][1]] = "."
            grid[move_south[ii][1][0], move_south[ii][1][1]] = "v"
        
        itr += 1
        run = not (last_state==grid).all()
        grid
        run
        itr
    return itr

f = open("day_25.txt", "r")

input = f.read().splitlines()

f.close()

x_len = len(input[0])

y_len = len(input)

input = "".join(input)

input = list(input)

arr = np.array(input)

arr = arr.reshape(y_len, x_len)

# get part 1 answer
print(move(arr, y_len, x_len))
