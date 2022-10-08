from statistics import median

# define functions
def syntax_err(x, part_1 = True):

    illegal = False
    expect = []
    lookup = ['[','{','(','<']
    requires = [']','}',')','>']

    for ii in range(len(x)):
        if x[ii] not in [']','}',')','>']:
            tmp_idx = lookup.index(x[ii])
            expect.append(requires[tmp_idx])
        elif x[ii] == expect[len(expect)-1]:
            del expect[-1]
            continue
        else:
            illegal = True
            break
    
    if part_1:
        if illegal:
            return x[ii]
        else:
            return
    elif not illegal:
        return expect
    else:
        return

def auto_score(x):

    score = 0

    lookup = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }

    x = [lookup[i] for i in x]

    for ii in x:
        score = score * 5
        score += ii

    return score

# import data
f = open("day_10.txt", "r")

input = f.read().splitlines()

f.close()

# process part 1
illegal_chars = []

for ii in input:
    illegal_chars.append(syntax_err(ii))

illegal_chars = list(filter(None, illegal_chars))

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

illegal_chars = [scores[x] for x in illegal_chars]

# process part 2
auto_comp = []

for ii in input:
    auto_comp.append(syntax_err(ii, part_1=False))

auto_comp = list(filter(None, auto_comp))

for ii in range(len(auto_comp)):
    auto_comp[ii].reverse()

ac_scores = []

for ii in auto_comp:
    ac_scores.append(auto_score(ii))

# Part 1 answer
print(sum(illegal_chars))

# Part 2 answer
print(median(ac_scores))