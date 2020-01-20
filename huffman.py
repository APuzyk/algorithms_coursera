file = '/home/apuzyk/Documents/algorithms_coursera/huffman.txt'
with open(file) as f:
    o = f.readlines()


# node, weight, Left, right
t = [[i, o[i], None, None] for i in range(len(o))] #nodes
t = sorted(t, key=lambda x: x[1])
parent_dict = {}
for i in range(len(o)):
    parent_dict[i] = None

o_tree = [[i, i, i] for i in range(len(o))]
meta_node = len(o)
while len(t) > 1:
    t1 = t.pop()
    t2 = t.pop()
    t3 = [meta_node, t1[1] + t2[1], t1[0], t2[0]]
    parent_dict[t1[0]] = meta_node
    parent_dict[t2[0]] = meta_node
    f.append(t3)
    f = sorted(f, key=lambda x: x[1]) #todo improve with heap
    meta_node += 1

#reconstruct
o_depths = []
traces = []
for i in range(o):
    root = f[0][0]
    trace = []
    search = i
    depth = 0
    while parent_dict[search] != root:
        trace.append(search)
        search = parent_dict[search]
        depth += 1

    trace.append(search)
    traces.append(trace)
