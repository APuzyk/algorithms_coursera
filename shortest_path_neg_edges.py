from numpy import ndarray
from math import inf
import sys

#g1_f = '/home/apuzyk/Documents/algorithms_coursera/g1.txt'
g1_f = sys.argv[1]
print(g1_f)


class Graph:
    def __init__(self, edge_list):
        self.edge_list = edge_list
        self.nodes = list(set([i[0] for i in edge_list]))
        self.nodes.extend(list(set([i[1] for i in edge_list])))
        self.nodes = list(set(self.nodes))
        self.num_nodes = len(self.nodes)
        self.num_edges = len(self.edge_list)
        self.adjacency = dict()
        self.make_adjacency()

    def make_adjacency(self):
        for i in self.nodes:
            self.adjacency[i] = {}

        for i in self.edge_list:
            k = str(i[0]) + '->' + str(i[1])
            self.adjacency[i[0]][k] = i[2]






def make_graph(file):
    with open(file) as f:
        o = f.readlines()
    o = o[1:]
    o = [list(map(int, i.rstrip().split(' '))) for i in o]
    o = [[i[0]-1, i[1] -1, i[2]] for i in o]
    return Graph(o)


g1 = make_graph(g1_f)

a_prev = ndarray(shape=(g1.num_nodes, g1.num_nodes), dtype=float)

# init array
for v in g1.nodes:
    for w in g1.nodes:
        if v == w:
            a_prev[v, w] = 0
        elif g1.adjacency[v].get(str(v) + '->' + str(w)) is not None:
            a_prev[v, w] = g1.adjacency[v].get(str(v) + '->' + str(w))
        else:
            a_prev[v, w] = inf

for k in g1.nodes:
    print(f"run {k} of {g1.num_nodes}")
    a_curr = ndarray(shape=(g1.num_nodes, g1.num_nodes), dtype=float)
    for v in g1.nodes: #source
        for w in g1.nodes: #dest
            c_1 = a_prev[v, w]
            c_2 = a_prev[v, k] + a_prev[k, w]
            a_curr[v, w] = min([c_1, c_2])
    a_prev = a_curr

if any(a_curr.diagonal() < 0):
    print('neg_cycle')
else:
    print(a_curr.min())


