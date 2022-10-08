# define functions
def split_polymer(times, cnt, map_a, map_b, map_c):
  
  main_cnt = [0]*len(main_map)

  for letter in ini_seq:
    main_cnt[main_map.index(letter)] += 1

  ini = []

  for ii in range(len(ini_seq)):
      if ii < len(ini_seq) - 1:
          ini.append(ini_seq[ii:(ii+2)])
        
  cnt = [0]*len(map_b)

  for ele in ini:
      cnt[map_a.index(ele)] += 1
  
  for _ in range(times):
  
    tmp_cnt = [0]*len(map_b)
  
    for ii in range(len(cnt)):
      if cnt[ii] == 0:
        continue
      else:
        n_split = cnt[ii]
        splitting = map_a[ii]
        new_lhs = map_b[map_a.index(splitting)][0]
        new_rhs = map_b[map_a.index(splitting)][1]
        lets_count = map_c[map_a.index(splitting)][0]
        tmp_cnt[map_a.index(new_lhs)] += n_split
        tmp_cnt[map_a.index(new_rhs)] += n_split
        main_cnt[main_map.index(lets_count)] += n_split
      
    cnt = tmp_cnt
  
  return(max(main_cnt) - min (main_cnt))

# Import and cleanse

f = open("day_14.txt", "r")
input = f.read().splitlines()
f.close()

ini_seq = input[0]

mapping = input[2:]

map_a = []
map_b = []
map_c = []

for ele in mapping:
    tmp = ele.split(" -> ")
    map_a.append(tmp[0])
    map_b.append([tmp[0][0]+tmp[1],tmp[1]+tmp[0][1]])
    map_c.append(tmp[1])

main_map = list(set(map_c))

main_cnt = [0]*len(main_map)

for letter in ini_seq:
  main_cnt[main_map.index(letter)] += 1

ini = []

for ii in range(len(ini_seq)):
    if ii < len(ini_seq) - 1:
        ini.append(ini_seq[ii:(ii+2)])
        
cnt = [0]*len(map_b)

for ele in ini:
    cnt[map_a.index(ele)] += 1

# Part 1 answer
print(split_polymer(10, cnt, map_a, map_b, map_c))

# Part 2 answer
print(split_polymer(40, cnt, map_a, map_b, map_c))
