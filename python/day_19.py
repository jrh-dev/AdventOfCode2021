import copy
import itertools
import numpy as np
import time

def manhattan(a, b):
  return sum(abs(v1-v2) for v1, v2 in zip(a,b))

class scanner:
  def __init__(self, coords, spos=[0,0,0]):
    self.orig_coord = coords
    self._dist = self._get_distances(coords)
    self.dist = self._dist
    self.shared = []
    self.adj_coord = []
    self.scanner_pos = spos
    
  def _get_distances(self, coords):
    distances = []

    for ii in range(len(coords)):
      tmp_d = []
      for jj in range(len(coords)):
        if ii == jj:
          continue
        else:
          tmp_d.append(sum([abs(coords[ii][kk] - coords[jj][kk]) for kk in [0,1,2]]))
      distances.append(tmp_d)
      
    return distances

def rotations():
    vectors = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ]
    vectors = list(map(np.array, vectors))
    for vi in vectors:
        for vj in vectors:
            if vi.dot(vj) == 0:
                vk = np.cross(vi, vj)
                yield lambda x: np.matmul(x, np.array([vi, vj, vk]))
                
def adjuster(input_a, input_b):

  t1 = copy.deepcopy(input_a)

  t2 = copy.deepcopy(input_b)

  for ii in range(len(t2.orig_coord)):
    for jj in range(len(t1.orig_coord)):
      if sum([dist in t2.dist[ii] for dist in t1.dist[jj]]) > 10:
        t2.shared.append([t1.orig_coord[jj], t2.orig_coord[ii]])
  
  if len(t2.shared) < 12:
    return [t1.orig_coord, False]
  else:
    tar1 = t2.shared[0][0]
    tar2 = t2.shared[1][0]

    star1 = t2.shared[0][1]
    star2 = t2.shared[1][1]


    for rot in rotations():
      st1 = rot(star1)
      st2 = rot(star2)
      if (
          (tar1[0] - st1[0] == tar2[0] - st2[0]) &
          (tar1[1] - st1[1] == tar2[1] - st2[1]) &
          (tar1[2] - st1[2] == tar2[2] - st2[2])
          ):
            for coord in t2.orig_coord:
              t2.adj_coord.append(list(rot(coord)))
            break
            
    x_adj = tar1[0] - st1[0]
    y_adj = tar1[1] - st1[1]
    z_adj = tar1[2] - st1[2]
    
    for ii in range(len(t2.adj_coord)):
      t2.adj_coord[ii][0] = t2.adj_coord[ii][0] + x_adj
      t2.adj_coord[ii][1] = t2.adj_coord[ii][1] + y_adj
      t2.adj_coord[ii][2] = t2.adj_coord[ii][2] + z_adj
      
  return [t2.adj_coord, True, [x_adj, y_adj, z_adj]]

def joins(input_a, input_b):
  
  if input_a == input_b:
    return False
  
  t1 = copy.deepcopy(input_a)

  t2 = copy.deepcopy(input_b)

  for ii in range(len(t2.orig_coord)):
    for jj in range(len(t1.orig_coord)):
      if sum([dist in t2.dist[ii] for dist in t1.dist[jj]]) > 10:
        t2.shared.append([t1.orig_coord[jj], t2.orig_coord[ii]])
  
  if len(t2.shared) < 12:
    return False
  else:
    return True
    
  
#--------
f = open("day_19.txt", "r")
input = f.read().split("\n\n")
f.close()


raw_scan = [
        list(map(lambda x: list(map(int, x.split(","))), s.split("\n")[1:]))
        for s in input
    ]

scanners = []

for ii in range(len(raw_scan)):
  scanners.append(scanner(raw_scan[ii]))

zerod = [scanners[0]]
todo = scanners[1:]

ii=0
jj=0

while len(todo) > 0:
  if joins(zerod[ii], todo[jj]):
    tmp = adjuster(zerod[ii],todo[jj])
    zerod.append(scanner(tmp[0],tmp[2]))
    del todo[jj]
    ii=0
    jj=0
  else:
    ii+=1
    if ii >= len(zerod):
      ii=0
      jj+=1
      if jj >= len(todo):
        break


values = []

for scan in zerod:
  values.append([hash(tuple(cord)) for cord in scan.orig_coord])

values = list(itertools.chain.from_iterable(values))

scanner_pos = [scan.scanner_pos for scan in zerod]

# part 1 answer
print(len(set(values)))

# part 2 answer
max([manhattan(i,j) for i in scanner_pos for j in scanner_pos])
