from collections import deque

file = '/home/apuzyk/Documents/algorithms_coursera/SCC.txt'

with open(file) as f:
    o = f.readlines()

o = [i.rstrip().split(' ') for i in o]
o = [i for i in o if i[0] != i[1]]

# to test
o = [[5, 9],
[9,8],
[8,5],
[9,4],
[9,7],
[8,7],
[7,1],
[1,6],
[6,7],
[6,3],
[3,7],
[1,2],
[4,2]]

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
tracker = []
# Iterate through nodes
node = nodes[1]
for node in nodes:
    if not visited[node]:
        stack = deque()
        stack.append(node)
        while len(stack) > 0:
            v = stack.pop()
            if not visited[v]:
                visited[v] = True
                for w in g_r[v]:
                    stack.append(w)

                #we append to tracker as we discover new nodes
                # here we check if the current node is a child of the previous node
                # if not we add the previous nodes we iterated through until we reach the og parent
                # basically we're adding paths until we re reach the parent node
                while tracker and v not in g_r[tracker[-1]]:
                    order.append(tracker.pop())
                tracker.append(v)

order = tracker + order[::-1]
order
visited = [False] * len(nodes)

scc = []
num_scc = 0
for v in order:
    if not visited[v]:
        scc.append([])
        stack = deque()
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
print(o[:5])
scc