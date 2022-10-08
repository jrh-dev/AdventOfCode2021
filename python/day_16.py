import numpy as np

h2b = {
  "0": '0000',
  "1": '0001',
  "2": '0010',
  "3": '0011',
  "4": '0100',
  "5": '0101',
  "6": '0110',
  "7": '0111',
  "8": '1000',
  "9": '1001',
  "A": '1010',
  "B": '1011',
  "C": '1100',
  "D": '1101',
  "E": '1110',
  "F": '1111'
}


class lit_val:
  def __init__(self, value):
    self.pak_ver = int(value[0:3], 2)
    self.pak_typ = self._is_lit(value)
    self._parse = self._value(value)
    self.value = self._parse[0]
    self.tot_len = self._parse[1]
    
  def _is_lit(self, value):
    typ = int(value[3:6], 2)
    if typ != 4:
      raise ValueError("Not a literal packet type")
    return typ
    
  def _value(self, value):
    subpak = value[6:]
    parsed = ""
    cont = True
    n = 0
    
    while cont:
      n += 1
      if subpak[0] == '1':
        parsed = parsed + subpak[1:5]
        subpak = subpak[5:]
      else:
        parsed = parsed + subpak[1:5]
        cont = False
    
    return [int(parsed, 2), (n * 5 + 6)]


class opr_val:
  def __init__(self, value):
    self.pak_ver = int(value[0:3], 2)
    self.pak_typ = self._is_lit(value)
    self.len_type = int(value[6])
    self._len_type_val = self._bit_len(value)
    self._intermediate = self._inter(value)
    self.sub_pak_len = self._intermediate[0]
    self.sub_pak_bit_len = self._intermediate[1]
    self.sub_pak_start = self._intermediate[2]
    self.value = -1
     
  def _inter(self, value):
    if self.len_type == 1:
      spl = int(value[7:7+self._len_type_val],2)
      spbl = None
      sps = 18 
    else:
      spbl = int(value[7:7+self._len_type_val],2)
      spl = None
      sps = 22
    return[spl,spbl,sps]
    
    
  def _is_lit(self, value):
    typ = int(value[3:6], 2)
    if typ == 4:
      raise ValueError("Not an operator packet type")
    return typ
  
  def _bit_len(self, value):
    bl = int(value[6])
    if bl == 0:
      v = 15
    else:
      v = 11
    
    return v
  
  def _sub_pak_len(self, value):
    bl = int(value[6])
    if bl == 0:
      v = int(value[7:22], 2)
    else:
      v = int(value[7:18], 2)
    
    return v

def unpack(inp):
  
  unpacked = []
  while int(inp,2) != 0:
  
    if int(inp[3:6], 2) == 4:
      t = lit_val(inp)
    else:
      t = opr_val(inp)
    
    unpacked.append(t)
  
    if t.pak_typ == 4:
      inp = inp[t.tot_len:]
    else:
      inp = inp[t.sub_pak_start:]

    if len(inp) == 0:
      break
    
  return unpacked

def evaluate(unpacked):

  for ii in range(len(unpacked)):
    
    x = unpacked[ii]
    pt = x.pak_typ
    if pt != 4:
      spl = x.sub_pak_len
      subs = [up.value for up in unpacked[ii+1:ii+1+spl]]
      if all([y > -1 for y in subs]):
        if pt == 0:
          x.value = sum(subs)
        if pt == 1:
          x.value = np.prod(subs)
        if pt == 2:
          x.value = min(subs)
        if pt == 3:
          x.value = max(subs)
        if pt == 5:
          if subs[0] > subs[1]:
            x.value = 1
          else:
            x.value = 0
        if pt == 6:
          if subs[0] < subs[1]:
            x.value = 1
          else:
            x.value = 0
        if pt == 7:
          if subs[0] == subs[1]:
            x.value = 1
          else:
            x.value = 0
        unpacked[ii].value = x.value
        del unpacked[ii+1:ii+1+spl]
        print(ii)
        break
      
  return unpacked

def hex_to_bin(input, dic):
  output = ""
  for i in input:
    output = output + dic.get(i)
  return output


f = open("day_16.txt", "r")
input = f.read().splitlines()
f.close()

hex = hex_to_bin(input, h2b)

unpacked = unpack(hex)

count = 0

for pak in unpacked:
  count += pak.pak_ver

ii=0
it = 1
n = 0

subs=[]
lens=[]

while len(unpacked) > 1:
  if unpacked[ii].value < 0:
    if unpacked[ii].sub_pak_len is not None:
      mx = unpacked[ii].sub_pak_len
  
      while it <= mx:
        subs.append(unpacked[ii+it].value)
        if unpacked[ii+it].pak_typ != 4:
          lens.append(unpacked[ii+it].sub_pak_start)
        else:
          lens.append(unpacked[ii+it].tot_len)
        it+=1
  
    else:
      mx = unpacked[ii].sub_pak_bit_len
  
      while n < mx:
        if unpacked[ii+it].pak_typ != 4:
          n += unpacked[ii+it].sub_pak_start
          if n <= mx:
            subs.append(unpacked[ii+it].value)
            lens.append(unpacked[ii+it].sub_pak_start)
        else:
          n += unpacked[ii+it].tot_len
          if n <= mx:
            subs.append(unpacked[ii+it].value)
            lens.append(unpacked[ii+it].tot_len)
        it+=1

    pt = unpacked[ii].pak_typ

    if all([y > -1 for y in subs]):
      if pt == 0:
        unpacked[ii].value = sum(subs)
      elif pt == 1:
        unpacked[ii].value = np.prod(subs)
      elif pt == 2:
        unpacked[ii].value = min(subs)
      elif pt == 3:
        unpacked[ii].value = max(subs)
      elif pt == 5:
        if subs[0] > subs[1]:
          unpacked[ii].value = 1
        else:
          unpacked[ii].value = 0
      elif pt == 6:
        if subs[0] < subs[1]:
          unpacked[ii].value = 1
        else:
          unpacked[ii].value = 0
      elif pt == 7:
        if subs[0] == subs[1]:
          unpacked[ii].value = 1
        else:
          unpacked[ii].value = 0
      if len(lens) > 0:
        unpacked[ii].sub_pak_start += sum(lens)
      del unpacked[ii+1:ii+len(subs)+1]
      subs=[]
      lens=[]
      ii=0
      it = 1
      terminal_len = len(unpacked)
      n=0
    else:
      ii+=1
      it=1
      subs=[]
      lens=[]
      n=0
  
  else:
    ii+=1
    it=1
    n=0

# part 1 answer
print(count)

# part 2 answer
print(unpacked[0].value)
