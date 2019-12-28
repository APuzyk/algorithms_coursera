from collections import deque

file = '/home/apuzyk/Documents/algorithms_coursera/SCC.txt'

with open(file) as f:
    o = f.readlines()

o = [i.rstrip().split(' ') for i in o]
o = [i for i in o if i[0] != i[1]]

#index at 0 to make things easier
nodes = list(set([j for i in o for j in i]))
len(nodes)
nodes = [i for i in range(len(nodes))]
g = [[] for i in range(len(nodes))]
g_r = [[] for i in range(len(nodes))]

for i in o:
    g[int(i[0]) - 1].append(int(i[1]) - 1)
    g_r[int(i[1]) - 1].append(int(i[0]) - 1)

visited = [False] * len(nodes)
order = []

# Iterate through nodes
for node in nodes:
    #If a node isn't visited go through it
    if not visited[node]:
        # Create a stack for DFS and init with node
        stack = deque()
        stack.append(node)
        while len(stack) > 0:
            # Pop from the top of the stack (last one in)
            # for first iter it'll be our first node
            # otherwise it's last one we've visited
            v = stack.pop()
            if not visited[v]:
                # IF we haven't been to the node
                # set visited to true and append each edge to the list
                # that we haven't been to yet
                #TODO how do we figure out when to label the thing
                visited[v] = True
                for w in g_r[v]:
                    if not visited[w]:
                        stack.append(w)
            #
            order.append(v)

order.reverse()

visited = [False] * len(nodes)

scc = []
num_scc = 0
stack = deque()
for v in order:
    if not visited[v]:
        scc.append([])
        stack.append(v)
        while len(stack) > 0:
            w = stack.pop()
            if not visited[w]:
                visited[w] = True
                scc[len(scc) - 1].append(w)
                for u in g[w]:
                    stack.append(u)

o = [len(i) for i in scc]
o.sort(reverse=True)
o
