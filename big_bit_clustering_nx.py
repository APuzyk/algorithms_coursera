import itertools
from networkx.utils import UnionFind
file = '/home/apuzyk/Documents/algorithms_coursera/clustering_big.txt'
with open(file) as f:
    o = f.readlines()

o = [i.strip().replace(' ', '') for i in o][1:]
print(o[0])
o = [int(i, 2) for i in o]
print(o[0])
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

uf = UnionFind([i for i in range(len(o))])
#create dict of nodes
nodes_vals = list(set(o))
nd = {}
for i in range(len(o)):
    if nd.get(o[i]) is not None:
        nd[o[i]].extend([i])
    else:
        nd[o[i]] = [i]

#union dupes:
for k, v in nd.items():
    if len(v) > 1:
        uf.union(*v)

for i in range(len(bit_masks)):
    print('Iteration: {0} of {1}'.format(i + 1, len(bit_masks)))
    mask = bit_masks[i]
    for k, v in nd.items():
        to_compare = k ^ mask
        if nd.get(to_compare) is not None:
            to_union = [j for j in nd.get(k)]
            to_union += nd.get(to_compare)
            uf.union(*to_union)


print(len(list(uf.to_sets())))
