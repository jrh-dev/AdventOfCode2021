import numpy as np

def detect_flash(arr, flash, flashed):
    for yy in range(1,y_len + 1):
        for xx in range(1,x_len + 1):
            if arr[yy,xx] > 9:
                coord = [yy,xx]
                if (coord not in flash) & (coord not in flashed):
                    flash.append([yy,xx])
                else:
                    continue
    return flash

def apply_flash(arr, flash):
    for ii in range(len(flash)):
        y = flash[ii][0]
        x = flash[ii][1]
        arr[y-1:y+2, x-1:x+2] += 1
    return arr

def simulate(arr, times):
    arr = np.pad(arr, pad_width=1, mode='constant', constant_values=0)
    ran = 0
    n_flashes = 0
    for _ in range(times):
        ran += 1
        arr += 1

        flash = detect_flash(arr, [], [])

        if len(flash) > 0:
            n_flashes += len(flash)
            arr = apply_flash(arr,flash)

            cont = True
            flashed = []

            while cont:
                for i in flash:
                    flashed.append(i)
                flash = detect_flash(arr, [], flashed)
                if len(flash) > 0:
                    n_flashes += len(flash)
                    arr = apply_flash(arr,flash)
                else:
                    cont = False

            arr[arr > 9] = 0

            if np.all(arr[1:y_len+1, 1:x_len+1] == 0):
                break
        else:
            continue
    
    arr = arr[1:y_len+1, 1:x_len+1]

    return [arr, n_flashes, ran]

# Import and cleanse
f = open("day_11.txt", "r")

input = f.read().splitlines()

f.close()

x_len = len(input[0])

y_len = len(input)

input = "".join(input)

input = [int(char) for char in input]

arr = np.array(input)

arr = arr.reshape(y_len, x_len)

# Part 1 answer
print(simulate(arr, 100)[1])

# Part 2 answer - set a suitably high number of iterations
print(simulate(arr, 500)[2])