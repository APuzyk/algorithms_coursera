file = '/home/apuzyk/Documents/algorithms_coursera/clustering1.txt'
with open(file) as f:
    o = f.readlines()

o = [i.rstrip().split(' ') for i in o][1:]

o = [[int(i[0]), int(i[1]), int(i[2])] for i in o]

nodes = [i[0] for i in o] + [i[1] for i in o]
nodes = list(set(nodes))

#parent, size
n_uf = [[i, 1] for i in nodes]

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


def num_clusters(uf):
    return len(list(set([uf_find(uf, i+1) for i in range(len(uf))])))
# Make clusters
k = 4

edges = sorted(o, key=lambda x: x[2])
t = []
#combine step
for i in edges:
    if num_clusters(n_uf) <= k:
        break
    if uf_find(n_uf, i[0]) != uf_find(n_uf, i[1]):
        t.append(i)
        uf_update(n_uf, i[0], i[1])

print(i[2])