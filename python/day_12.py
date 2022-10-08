from itertools import compress
from collections import Counter

# define functions
def parse_input(x):
    sp = []
    ep = []

    for lines in input:
         s, e = lines.split("-")
         sp.extend([s,e])
         ep.extend([e,s])
    
    return [sp,ep]

def get_paths(sp, ep, small_doubles):
    checking = [['start']]
    paths = 0
    while len(checking) != 0:
        to_check = []

        for ii in range(len(checking)):
            lookup = [x == checking[ii][-1] for x in sp]
            moves = list(compress(ep, lookup))

            for jj in range(len(moves)):
                
                test_dup = checking[ii] + [moves[jj]]
                test_dup = list(filter(lambda x: x.islower(), test_dup))
                test_dup = list(Counter(test_dup).items())

                if (sum([i[1] > 2 for i in test_dup]) > 0 )|(sum([i[1] > 1 for i in test_dup]) > small_doubles )|(test_dup[0][1] > 1):
                    continue
                elif moves[jj] == 'end':
                    paths += 1
                else:
                    to_check.append(checking[ii] + [moves[jj]])

        checking = to_check[:]
    
    return paths


# Import and cleanse
f = open("day_12.txt", "r")
input = f.read().splitlines()
f.close()

points = parse_input(input)

# part 1 answer
print(get_paths(sp=points[0], ep=points[1], small_doubles=0))

# part 2 answer
print(get_paths(sp=points[0], ep=points[1], small_doubles=1))

