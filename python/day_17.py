
class probe:
  def __init__(self, x, y, tar_x_start, tar_x_end, tar_y_start, tar_y_end):
    self.start_x = x
    self.start_y = y
    self.tar_x_range = range(tar_x_start, tar_x_end + 1)
    self.tar_y_range = range(tar_y_start, tar_y_end + 1)
    self._traj = self.trajectory(self.start_x, self.start_y, self.tar_x_range, self.tar_y_range)
    self.success = self._traj[0]
    self.x_path = self._traj[1]
    self.y_path = self._traj[2]
    self.highest = max(self.y_path)

  def trajectory(self, x, y, txr, tyr):
    cur_x = 0
    cur_y = 0
    x_vol = x
    y_vol = y
    hit = False
    x_path = []
    y_path = []
    
    while (cur_x <= max(txr)) & (cur_y >= min(tyr)):
      cur_x += x_vol
      cur_y += y_vol
      x_path.append(cur_x)
      y_path.append(cur_y)
      
      if x_vol > 0:
        x_vol -= 1
      elif x_vol < 0:
        x_vol += 1
      
      y_vol -= 1
      
      if (cur_x in txr) & (cur_y in tyr):
        hit = True
    
    return [hit, x_path, y_path]
      
class targeting:
  def __init__(self, tar_x_max, tar_y_max, tar_y_min):
    self.try_x = range(1,tar_x_max+1)
    self.try_y = self._get_try_y(tar_y_max, tar_y_min)
     
  def _get_try_y(self, tar_y_max, tar_y_min):
    if tar_y_min < 0:
      rng = range(tar_y_max, (abs(tar_y_min)+1) * 2)
    else:
      rng = range(tar_y_max, (tar_y_min * 2)+1)
    return rng

# import and calculate solution        

sols = targeting(73,-248,-194)

shots = []

for ii in sols.try_x:
  for jj in sols.try_y:
    shots.append(probe(ii,jj,29,73,-248,-194))
    
success = 0
highest = 0

for shot in shots:
  if shot.success:
    success += 1
    if (shot.highest > highest):
      highest = shot.highest

# part 1 solution
print(highest)

# part 2 solution
print(success)
