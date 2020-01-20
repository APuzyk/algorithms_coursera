import itertools
file = '/home/apuzyk/Documents/algorithms_coursera/clustering_big.txt'
with open(file) as f:
    o = f.readlines()

o = [i.strip().replace(' ', '') for i in o][1:]
o = [int(i, 2) for i in o]

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

#create dict of nodes
n_uf = [[i+1, 1] for i in range(len(o))]
nodes_vals = list(set(o))
nd = {}
for i in range(len(nodes_vals)):
    print(i)
    nd[i] = [j + 1 for j, x in enumerate(o) if x == nodes_vals[i]]

#save because slow as fuck
import pickle
filename = '/home/apuzyk/Documents/algorithms_coursera/clustering_big_dict.pickle'
with open(filename, ‘wb’) as f:
    pickle.dump(nd, f)

for i in bit_masks:
    for k, v in nd:
        to_compare = k ^ i
        if nd.get(to_compare) is not None:
            to_union = [j for j in v]
            to_union.extend([j for j in nd.get(to_compare)])
            start = to_union.pop()
            for j in to_union:
                uf_update(n_uf, start, j)

