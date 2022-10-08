import numpy as np

# define functions
def next_pos(track_array, visited):
  
  if len(visited) > 0:
    for ii in range(len(visited[0])):
      track_arr[visited[0][ii],visited[1][ii]] = float('inf')
  
  tmp = np.where(track_arr == np.amin(track_arr))
  tmp_y = list(tmp[0])
  tmp_x = list(tmp[1])
  
  return [tmp_y, tmp_x]

def get_moves(y_idx,x_idx, dim_y, dim_x):
  
  moves = []
  starts = []
  
  for ii in range(len(y_idx)):
    x = [y_idx[ii],x_idx[ii]+1]
    y = [y_idx[ii]+1,x_idx[ii]]
    nx = [y_idx[ii],x_idx[ii]-1]
    ny = [y_idx[ii]-1,x_idx[ii]]
  
    if (x[0] < dim_x) & (x[1] < dim_x):
      moves.append(x)
      starts.append([y_idx[ii],x_idx[ii]])
  
    if (y[0] < dim_y) & (y[1] < dim_y):
      moves.append(y)
      starts.append([y_idx[ii],x_idx[ii]])
      
    if (nx[0] >= 0) & (nx[1] >= 0):
      moves.append(nx)
      starts.append([y_idx[ii],x_idx[ii]])
  
    if (ny[0] >= 0) & (ny[1] >= 0):
      moves.append(ny)
      starts.append([y_idx[ii],x_idx[ii]])

  return([starts, moves])

def make_move(start_on, moves, base_arr, track_arr):
  
  for ii in range(len(moves)):
    move_to = base_arr[moves[ii][0],moves[ii][1]]
    cost = track_arr[start_on[ii][0],start_on[ii][1]] + move_to
    track_to = track_arr[moves[ii][0],moves[ii][1]]
  
    if (cost < track_to):
      track_arr[moves[ii][0],moves[ii][1]] = cost
    
  return track_arr

def solve(pos, dim_x, dim_y, base_arr, track_arr):

  run = True
  
  solution = [float('inf')]
  
  while run:

    moves = get_moves(pos[0],pos[1], dim_y, dim_x)
  
    track_arr = make_move(moves[0], moves[1], base_arr, track_arr)
  
    visited = pos[:]

    pos = next_pos(track_arr, visited)
    
    if track_arr[dim_y-1,dim_x-1] != float('inf'):
      solution.append(track_arr[dim_y-1,dim_x-1])
      
    if (len(pos[0]) == base_arr.size) | (np.amin(track_arr) > min(solution)):
      run = False
      
  return(min(solution))

def expand_arr(arr):
  
  arr_base = arr[:]
  
  arr_dev = arr[:]
  
  for ii in range(1,5):
    arr_tmp = arr_base + ii
    arr_tmp[arr_tmp > 9] = arr_tmp[arr_tmp > 9] - 9
    arr_dev = np.hstack((arr_dev, arr_tmp))
    
  arr_base = arr_dev[:]
    
  for ii in range(1,5):
    arr_tmp = arr_base + ii
    arr_tmp[arr_tmp > 9] = arr_tmp[arr_tmp > 9] - 9
    arr_dev = np.vstack((arr_dev, arr_tmp))

  arr_base = arr_dev[:]
  
  return arr_base

# import and cleanse
f = open("day_15.txt", "r")
input = f.read().splitlines()
f.close()

dim_y = len(input)
dim_x = len(input[0])

input = [[int(char) for char in line] for line in input]

input = [item for sublist in input for item in sublist]

base_arr = np.array(input)

base_arr = base_arr.reshape(dim_y,dim_x)

track_arr = np.array([float('inf')]*len(input))

track_arr = track_arr.reshape(dim_y,dim_x)

track_arr[0,0] = 0

pos = next_pos(track_arr, [])

# part 1 answer    
print(solve(pos, dim_x, dim_y, base_arr, track_arr))

base_arr = expand_arr(base_arr)

dim_y = base_arr.shape[0]
dim_x = base_arr.shape[1]

track_arr = np.array([float('inf')]*(dim_y*dim_y))

track_arr = track_arr.reshape(dim_y,dim_x)

track_arr[0,0] = 0

pos = next_pos(track_arr, [])

# part 2 answer    
print(solve(pos, dim_x, dim_y, base_arr, track_arr))
