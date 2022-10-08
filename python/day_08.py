
f = open("day_08.txt", "r")

input = f.read().splitlines()

f.close()

for ii in range(len(input)):
    input[ii] = input[ii].split("|")

for ii in range(len(input)):
    input[ii][0] = input[ii][0].split(" ")
    input[ii][1] = input[ii][1].split(" ")

def find_nine(x, y):
    for ii in x:
        if len(ii) == 6:
            if len(set(y) & set(ii)) == 4:
                return x[x.index(ii)]

def find_three(x, y):
    for ii in x:
        if len(ii) == 5:
            if len(set(y) & set(ii)) == 2:
                return x[x.index(ii)]

def find_zero(x, y, z):
    for ii in x:
        if (len(ii) == 6)  & (ii != z):
            if len(set(y) & set(ii)) == 2:
                return x[x.index(ii)]

def find_six(x, y, z):
    for ii in x:
        if (len(ii) == 6)  & (ii != y) & (ii != z):
            return x[x.index(ii)]

def find_five(x, y, z):
    for ii in x:
        if (len(ii) == 5)  & (ii != y) & (len(set(z) & set(ii)) == 5):
            return x[x.index(ii)]

def find_two(x, y, z):
    for ii in x:
        if (len(ii) == 5)  & (ii != y) & (len(set(z) & set(ii)) == 4):
            return x[x.index(ii)]

def get_base(x):
    lengths = [len(i) for i in x]
    
    out = {
        "one": x[lengths.index(2)],
        "four": x[lengths.index(4)],
        "seven": x[lengths.index(3)],
        "eight": x[lengths.index(7)]
        }

    out["nine"] = find_nine(x, out["four"])
    out["three"] = find_three(x, out["one"])
    out["zero"] = find_zero(x, out["one"], out["nine"])
    out["six"] = find_six(x, out["nine"], out["zero"])
    out["five"] = find_five(x, out["three"], out["nine"])
    out["two"] = find_two(x, out["three"], out["nine"])
    
    return out

decoded = []

for ii in range(len(input)):
    decoded.append(get_base(input[ii][0]))


cnt = 0

for ii in range(len(input)):
    for jj in ["one", "four", "seven", "eight"]:
        cnt += [sorted(i) for i in input[ii][1]].count(sorted(decoded[ii][jj]))

# Part 1 answer
print(cnt)

lookup = [1,4,7,8,9,3,0,6,5,2]

res = []

for ii in range(len(input)):
    tmp_dec = [sorted(i) for i in list(decoded[ii].values())]
    tmp_n = []
    for jj in range(4):
       tmp_n.append(lookup[tmp_dec.index([sorted(i) for i in input[ii][1][1:]][jj])])
    res.append(int(''.join(map(str,tmp_n))))

# Part 2 answer
print(sum(res))