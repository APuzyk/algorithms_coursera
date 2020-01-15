file = '/home/apuzyk/Documents/algorithms_coursera/edges.txt'
with open(file) as f:
    o = f.readlines()

o = o[1:]
inter = lambda x: int(x)
o = [list(map(inter, i.rstrip().split(' '))) for i in o]

nodes = [i[0] for i in o]
nodes.extend([i[1] for i in o])
nodes = list(set(nodes))

processed = nodes[0]
processed = [processed]
mst = []
while len(processed) < len(nodes):
    curr_node = processed[-1]
    to_check = [i for i in o if i[0] in processed and i[1] not in processed]
    to_check.extend([i for i in o if i[1] in processed and i[0] not in processed])
    to_check = sorted(to_check, key=lambda x: x[2])
    to_add = to_check[0]
    o = [i for i in o if i != to_add]
    mst.append(to_add)
    if to_add[0] in processed:
        processed.append(to_add[1])
    else:
        processed.append(to_add[0])

print(sum([i[2] for i in mst]))
# -3612829