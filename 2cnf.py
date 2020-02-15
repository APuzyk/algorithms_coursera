from collections import deque

fns = []
for i in range(1, 7):
    fns.append(f"/home/apuzyk/Documents/algorithms_coursera/2sat{i}.txt")

# 2cnf
# Each clause is item in list
# negative items are a negation of the other

#  will implement 2-cfn reduction to scc
#  1 or 2 =>
#  -1 => 2 OR -2 => 1
#  If i => -i on path then can't sat
#  eg if i and -i in scc then can't sat


def check_2cnf_sat(f):
    sccs = get_sccs(f)
    return check_sat(sccs)


def get_sccs(f):
    edges = prep_edges(f)
    nodes = get_nodes(edges)
    g, g_r = gen_graphs_both_directions(nodes, edges)
    order = get_order(g_r, nodes)
    sccs = find_sccs(g, order, nodes)
    return sccs


def prep_edges(file):
    with open(file) as f:
        o = f.readlines()
    o = o[1:]
    o = [list(map(int, i.rstrip().split(' '))) for i in o]

    # generate edges from the clauses
    edges = []
    for i in o:
        edges.append(f"{i[0]*-1} {i[1]}")
        edges.append(f"{i[1]*-1} {i[0]}")
    edges = [list(map(int, i.split(' '))) for i in list(set(edges))]

    edges = [i for i in edges if i[0] != i[1]]
    return edges


def get_nodes(edges):
    #index at 0 to make things easier
    nodes = list(set([j for i in edges for j in i]))
    return nodes


def gen_graphs_both_directions(nodes, edges):
    g = {}
    for i in nodes:
        g[i] = []
    g_r = {}
    for i in nodes:
        g_r[i] = []

    for i in edges:
        g[i[0]] += [i[1]]
        g_r[i[1]] += [i[0]]
    return g, g_r


def get_order(g_r, nodes):
    visited = {}
    for i in nodes:
        visited[i] = False
    order = []
    tracker = []
    # Iterate through nodes
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
    return order


def find_sccs(g, order, nodes):
    visited = {}
    for i in nodes:
        visited[i] = False

    scc = []
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
    return scc


def check_sat(sccs):
    # check if we have both positive and neg in same scc
    sat = True
    for i in sccs:
        for j in i:
            if j*-1 in i:
                sat = False
                break
    return sat


answer = ''

for f in fns:
    print(f)
    answer += str(int(check_2cnf_sat(f)))

print(f"Answer for quiz is: {answer}")