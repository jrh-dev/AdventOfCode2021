import numpy as np

f = open("day_3.txt", "r")

input = f.read().splitlines()

f.close()

gam = []
eps = []

for ii in range(12):
  
  n_1 = 0

  for jj in range(len(input)):
    if list(input[jj])[ii] == '1':
      n_1 += 1
    
  if n_1 > 500:
    gam.append('1')
    eps.append('0')
  else:
    gam.append('0')
    eps.append('1')
    
gam = ''.join(gam)
eps = ''.join(eps)

# part 1 answer
print(int(gam, 2) * int(eps, 2))


oxy = co2 = input

for ii in range(12):
  
  n_1 = 0
  keep = []

  for jj in range(len(oxy)):
    if list(oxy[jj])[ii] == '1':
      n_1 += 1

  if n_1 >= len(oxy) / 2:
    big = '1'
  else:
    big = '0'
    
  for kk in range(len(oxy)):
    if list(oxy[kk])[ii] == big:
      keep.append(oxy[kk])
  
  oxy = [x for x in oxy if x in keep]
  
  if len(oxy) == 1:
    break

for ii in range(12):
  
  n_1 = 0
  keep = []

  for jj in range(len(co2)):
    if list(co2[jj])[ii] == '1':
      n_1 += 1

  if n_1 < len(co2) / 2:
    big = '1'
  else:
    big = '0'
    
  for kk in range(len(co2)):
    if list(co2[kk])[ii] == big:
      keep.append(co2[kk])
  
  co2 = [x for x in co2 if x in keep]
  
  if len(co2) == 1:
    break
  
# part 2 answer
print(int(oxy[0],2) * int(co2[0],2))
