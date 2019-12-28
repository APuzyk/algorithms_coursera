file = '/home/apuzyk/Documents/algorithms_coursera/SCC.txt'

with open(file) as f:
    o = f.readlines()

o = [i.rstrip().split(' ') for i in o]
o = [i for i in o if i[0] != i[1]]

nodes = [j for i in o for j in i]
nodes = list(set(nodes))
len(nodes)
g = {}
for i in o:
    if g.get(i[0]) is None:
        g[i[0]] = [i[1]]
    else:
        g[i[0]].append(i[1])
g_rev = {}
for i in o:
    if g_rev.get(i[1]) is None:
        g[i[1]] = [i[0]]
    else:
        g[i[1]].append(i[0])

explore_list = [0 for i in nodes]
f_s = {}
for i in nodes:
    f_s[i] = 999999999
curLabel = len(nodes)


def dfs_topo(g, s):
    global curLabel
    global f_s

    explore_list[int(s)-1] = 1
    for i in g[s]:
        if explore_list[int(i)-1] == 0:
            dfs_topo(g, i)
    f_s[curLabel] = s
    curLabel = curLabel-1

#get order for grev:
dfs_topo(g_rev, '1')

#create new explore list for g
explore_list = [0 for i in nodes]

#scc tracking
scc = {}
num_scc = 0
for i in range(len(nodes)):
    v = f_s[i]
    if explore_list[int(v) - 1] == 0:
        num_scc += 1
        dfs_scc(g, v)


def dfs_scc(g, s):
    global explore_list
    global num_scc
    global scc

    explore_list[int(s) - 1] = 1
    if scc.get(num_scc) is None:
        scc[num_scc] = [s]
    else:
        scc[num_scc].append(s)
    for v in g[s]:
        if explore_list[int(v) - 1] == 0:
            dfs_scc(g, v)
