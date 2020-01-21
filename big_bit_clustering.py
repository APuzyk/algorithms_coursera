import itertools
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

uf = UnionFind(len(o))
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
        to_start = v[0]
        to_end = v[1:]
        for j in to_end:
            uf.union(to_start, j)

for i in bit_masks:
    for k, v in nd.items():
        to_compare = k ^ i
        if nd.get(to_compare) is not None:
            to_union = [j for j in nd.get(k)]
            to_union += nd.get(to_compare)
            start = to_union[0]
            to_merge = to_union[1:]
            for j in to_merge:
                if uf.find(j) != uf.find(start):
                    uf.union(start, j)


print(uf.num_clusters())
