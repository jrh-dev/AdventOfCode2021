
f = open("day_06.txt", "r")

input = f.read().splitlines()

f.close()

input = input[0].split(",")

input = [int(i) for i in input]

groups = []

for ii in range(1,10,1):
     groups.append(len(list(filter(lambda filt: filt == ii, input))))

def get_fish(start, iterations):
    for ii in range(iterations - 1):
        new = start[0]
        start[0:8] = start[1:9]
        start[6] = start[6] + new
        start[8] = new
    
    return sum(start)

# Part 1 answer
print(get_fish(groups[:], 80))

# Part 2 answer
print(get_fish(groups[:], 256))