# Read Lines
fn = '/home/apuzyk/Documents/algorithms_coursera/kargerMinCut.txt'

with open(fn) as f:
    r = f.readlines()

r = [i.split('\t') for i in r]
r = [[i[0], i[1:(len(i)-1)]] for i in r]

#now it's node + adjecent nodes
# create edge list
e = []
for i in r:
    for j in i[1]:
        e.append([i[0], j])

for i in range(len(e)):
    tmp = e[i]
    if tmp[0] > tmp[1]:
        tmp = [tmp[1], tmp[0]]
    e[i] = tmp

#hack as hell to remove dupes
tmp = [i[0] + '_' + i[1] for i in e]
e = [i.split('_') for i in list(set(tmp))]

v = [i[0] for i in r]

#now we have a list of unique edges as well as verticies
from random import randint

def min_cut(v, e):
    while len(v) > 2:
        e_1 = e[randint(0, len(e) - 1)]
        v, e = contract(v, e, e_1)

    return v, e, len(e)


def contract(v, e, e_1):
    v1 = e_1[0]
    v2 = e_1[1]
    new_vert = v1 + '_' + v2
    for i in range(len(v)):
        if v[i] in (v1, v2):
            v[i] = new_vert

    for i in range(len(e)):
        if e[i][0] in (v1, v2):
            e[i][0] = new_vert
        if e[i][1] in (v1, v2):
            e[i][1] = new_vert

    # unique verts
    v = list(set(v))

    # remove loops
    i = 0
    while i < (len(e)):
        if e[i][0] == e[i][1]:
            e.pop(i)
        else:
            i += 1

    return v, e

v_o, e_o, num_cuts = min_cut(v, e)


