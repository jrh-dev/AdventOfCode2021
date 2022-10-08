class board:
    def __init__(self, cave, corridor, cost):
        self.cave = cave
        self.corridor = corridor
        self.cost = cost
        self.complete = cave == "aaaabbbbccccdddd"
        self.key = cave + corridor + str(cost)
        self.mi = self.mv_in(cave, corridor)
        self.mo = self.mv_out(cave, corridor)

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other.key
    
    def _mv_avail(self, cave, corridor, entry):
        avail = []
        for ii in reversed(range(0,entry)):
            if all([corridor[p] == "x" for p in range(ii,entry)]):
                avail.append(ii)
            else:
                break
        for ii in range(entry + 1, 11):
            if all([corridor[p] == "x" for p in range(entry + 1, ii + 1)]):
                avail.append(ii)
            else:
                break
        avail = [e for e in avail if e not in [2,4,6,8]]

        return avail

    def _mvs(self, cav_id, cave, corridor):
        if cav_id == "a":
           cur = cave[0:4]
           idx_start = 0
           ent = 2
        elif cav_id == "b":
           cur = cave[4:8]
           idx_start = 4
           ent = 4
        elif cav_id == "c":
           cur = cave[8:12]
           idx_start = 8
           ent = 6
        else:
           cur = cave[12:16]
           idx_start = 12
           ent = 8
        cur = cur.replace("x", "")
        cur_len = len(cur)
        if (cur_len == 0) or all([e == cav_id for e in cur]):
            return []
        else:
            tmp = self._mv_avail(cave, corridor, ent)
            mvs = []
            if len(tmp) > 0:
                for ii in range(0, len(tmp)):
                    mvs.append([idx_start + cur_len - 1, tmp[ii]])
            return mvs

    def mv_out(self, cave, corridor):
        mvs = []
        for l in ["a","b","c","d"]:
            mvs = mvs + self._mvs(l, cave, corridor)
        return mvs

    def mv_in(self, cave, corridor):
        open_caves = []
        if all([e in ["a", "x"] for e in cave[0:4]]) and any([e == "x" for e in cave[0:4]]):
            open_caves.append("a")
            a_open = len(cave[0:4].replace("x", ""))
        if all([e in ["b", "x"] for e in cave[4:8]]) and any([e == "x" for e in cave[4:8]]):
            open_caves.append("b")
            b_open = len(cave[4:8].replace("x", "")) + 4
        if all([e in ["c", "x"] for e in cave[8:12]]) and any([e == "x" for e in cave[8:12]]):
            open_caves.append("c")
            c_open = len(cave[8:12].replace("x", "")) + 8
        if all([e in ["d", "x"] for e in cave[12:16]]) and any([e == "x" for e in cave[12:16]]):
            open_caves.append("d")
            d_open = len(cave[12:16].replace("x", "")) + 12
        mvs = []

        for ii in range(0,11):
            tar = corridor[ii]
            if tar in open_caves:
                if (tar == "a") and all([corridor[p] == "x" for p in range(min(ii+1,2),max(ii,2))]):
                    rhs = a_open
                    mvs.append([ii, rhs])
                if (tar == "b") and all([corridor[p] == "x" for p in range(min(ii+1,4),max(ii,4))]):
                    rhs = b_open
                    mvs.append([ii, rhs])
                if (tar == "c") and all([corridor[p] == "x" for p in range(min(ii+1,6),max(ii,6))]):
                    rhs = c_open
                    mvs.append([ii, rhs])
                if (tar == "d") and all([corridor[p] == "x" for p in range(min(ii+1,8),max(ii,8))]):
                    rhs = d_open
                    mvs.append([ii, rhs])

        return mvs


# just need a function to perform moves and count cost

def _exit_cost(lhs, rhs):    
    if lhs in [0,1,2,3]:
        emerge = 2
        cap = 3
    if lhs in [4,5,6,7]:
        emerge = 4
        cap = 7
    if lhs in [8,9,10,11]:
        emerge = 6
        cap = 11
    if lhs in [12,13,14,15]:
        emerge = 8
        cap = 15

    cav_mv = cap - lhs
    cor_mv = len(range(min(emerge, rhs), max(emerge, rhs))) + 1

    return cav_mv + cor_mv

def _entry_cost(lhs, rhs):    
    if rhs in [0,1,2,3]:
        enter = 2
        cap = 3
    if rhs in [4,5,6,7]:
        enter = 4
        cap = 7
    if rhs in [8,9,10,11]:
        enter = 6
        cap = 11
    if rhs in [12,13,14,15]:
        enter = 8
        cap = 15

    cav_mv = cap - rhs
    cor_mv = len(range(min(enter, lhs), max(enter, lhs))) + 1

    return cav_mv + cor_mv

def _multiplier(x):
    if x == "a":
        return 1
    elif x == "b":
        return 10
    elif x == "c":
        return 100
    elif x == "d":
        return 1000


def solve(starter):
    boards = [starter]
    run = True    
    while run:
        new_boards = []
        found = []

        for b in boards:
            tmp_mv_out = b.mo[:]
            tmp_mv_in = b.mi[:] 
            tmp_cst = b.cost

            for ins in tmp_mv_in:
                tmp_cav = list(b.cave[:])
                tmp_cor = list(b.corridor[:])
                c_multi = _multiplier(tmp_cor[ins[0]])
                cost = (_entry_cost(ins[0], ins[1]) * c_multi) + tmp_cst
                tmp_cav[ins[1]] = tmp_cor[ins[0]]
                tmp_cor[ins[0]] = "x"
                new_boards.append(board(''.join(tmp_cav), ''.join(tmp_cor), cost))

            for out in tmp_mv_out:
                tmp_cav = list(b.cave[:])
                tmp_cor = list(b.corridor[:])
                c_multi = _multiplier(tmp_cav[out[0]])
                cost = (_exit_cost(out[0], out[1]) * c_multi) + tmp_cst
                tmp_cor[out[1]] = tmp_cav[out[0]]
                tmp_cav[out[0]] = "x"
                new_boards.append(board(''.join(tmp_cav), ''.join(tmp_cor), cost))

        boards = list(set(new_boards))

        run = not any([x.complete for x in boards])
        
    return min([x.cost for x in boards])

# part 1 answer
print(solve(board("aaddbbacccabddbc", "xxxxxxxxxxx", 0)))

# part 2 answer
print(solve(board("ddddabccaabbbcac", "xxxxxxxxxxx", 0)))