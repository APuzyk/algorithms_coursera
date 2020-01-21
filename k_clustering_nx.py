from networkx.utils import UnionFind
file = '/home/apuzyk/Documents/algorithms_coursera/clustering1.txt'
with open(file) as f:
    o = f.readlines()

o = [i.rstrip().split(' ') for i in o][1:]

o = [[int(i[0])-1, int(i[1])-1, int(i[2])] for i in o]

#test o
# o = [[0, 2, 1], [1, 2, 1], [2, 3, 4], [3, 4, 1], [3, 5, 1]]
# o = [[0, 1, 10], [0, 2, 130], [1, 2, 8], [2, 3, 7], [1, 3, 120],
#      [3, 4, 125], [3, 9, 1000], [3, 10, 200],
#      [4, 5, 9], [4, 9, 1000], [5, 7, 8], [5, 6, 3],
#      [6, 7, 2], [7, 4, 111],
#      [9, 10, 400], [9, 8, 7],
#      [10, 13, 9],
#      [13, 11, 15], [13, 12, 10]]
nodes = [i[0] for i in o] + [i[1] for i in o]
nodes = list(set(nodes))
#parent, size
uf = UnionFind(nodes)
# Make clusters
k = 4
edges = sorted(o, key=lambda x: x[2])
t = []

#combine step
while len(edges) > 0:
    if len(list(uf.to_sets())) == k:
        break
    i = edges.pop(0)
    if uf[i[0]] != uf[i[1]]:
        t.append(i)
        uf.union(i[0], i[1])

#clean off interior edges and get to next edge going
#  from cluster to cluster
while len(edges) > 0:
    i = edges.pop(0)
    if uf[i[0]] != uf[i[1]]:
        break
answer = i
print(answer)
node_dict = {}

for i in uf.clusters():
    node_dict[i] = []

for i in range(len(nodes)):
    node_dict[uf.find(i)] += [i]
for i in uf.clusters():
    print(i)
    print('Num nodes: {}'.format(len(node_dict[i])))
