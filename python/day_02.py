import pandas as pd

f = open("Coding/AdventOfCode_2021_python/day_2.txt", "r")

input = f.readlines()

f.close()

def split_input(x):
  return x.split(" ", -1)

up = 0
dwn = 0
fwd = 0

for ii in input:
  tmp = split_input(ii)
  if tmp[0] == "up":
    up += int(tmp[1])
  elif tmp[0] == "down":
    dwn += int(tmp[1])
  elif tmp[0] == "forward":
    fwd += int(tmp[1])

# part 1 answer    
print((dwn - up) * fwd)

aim = 0
dpt = 0

for ii in input:
  tmp = split_input(ii)
  if tmp[0] == "forward":
    dpt += (aim * int(tmp[1]))
  if tmp[0] == "up":
    aim += int(tmp[1]) * -1
  elif tmp[0] == "down":
    aim += int(tmp[1])

# part 2 answer
print(dpt * fwd)
