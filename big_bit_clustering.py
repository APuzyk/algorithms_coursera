import itertools
file = '/home/apuzyk/Documents/algorithms_coursera/clustering_big.txt'
with open(file) as f:
    o = f.readlines()

o = [i.strip().replace(' ', '') for i in o][1:]
o = [int(i, 2) for i in o]
for i in range(len(o)):
    o[i] = [bool(int(j)) for j in o[i]]

def h_dist(v0, v1):
    #calc hamming dist
    o = 0
    for i in range(len(v1)):
        if v0[i] == v1[i]:
            o += 1
    return o
#create bit mask outputs
bit_masks = [0]
zeros = [0 for i in range(24)]
for i in range(24):
    tmp = [str(i) for i in zeros]
    tmp[i] = '1'
    bit_masks.append(int(''.join(tmp), 2))

for i in itertools.combinations(range(24), 2):
    tmp = [str(i) for i in zeros]
    tmp[i[0]] = '1'
    tmp[i[1]] = '1'
    bit_masks.append(int(''.join(tmp), 2))

#parent, size
n_uf = [[i+1, 1] for i in range(len(o))]

#node, parent
def uf_find(uf, v):
    if uf[v-1][0] == v:
        return v
    while uf[v-1][0] != v:
        v = uf[v-1][0]
    return v

def uf_update(uf, v, u):
    if uf[u-1][1] >= uf[v-1][1]:
        #update parent
        uf[v-1][0] = u
        #update depth
        uf[v-1][1] = uf[u-1][1] + 1
    else:
        #update parent
        uf[u - 1][0] = v
        #update depth
        uf[u - 1][1] = uf[v - 1][1] + 1