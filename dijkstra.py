# read data
file = '/home/apuzyk/Documents/algorithms_coursera/dijkstraData.txt'
with open(file) as f:
    o = f.readlines()
o = [i.rstrip().split('\t') for i in o]
# Create adjancency list using index as vert
# basically index = vertex, 0 pos = tail, 1 pos = len(e)
o = [i[1:] for i in o]
ajm = []
for i in o:
    w = [j.split(',') for j in i]
    w = [[int(k[0])-1, int(k[1])] for k in w]
    ajm.append(w)


# Where have we been?
x = [False] * len(o)
x[0] = True #init with our source vert

# init the distance list
dist = [1000000] * len(o)
dist[0] = 0
i = 1
while not all(x):
    print(f"loop number {i}")
    # Add edges with head in X and tail in G-X with their final potential distance
    to_check = []
    for j in [i for i, val in enumerate(x) if val]:
        # iterate through edges
        for k in ajm[j]:
            if not x[k[0]]:
                to_check.append([j, k[0], k[1] + dist[j]])
    print(to_check)
    if len(to_check) == 0:
        break #if the graph isn't connected
    idx = [i[2] for i in to_check].index(min([i[2] for i in to_check]))
    x[to_check[idx][1]] = True
    dist[to_check[idx][1]] = to_check[idx][2]
    i += 1

# to print 7,37,59,82,99,115,133,165,188,197
print(f"{dist[6]},{dist[36]},{dist[58]},{dist[81]},{dist[98]},{dist[114]},{dist[132]},{dist[164]},{dist[187]},{dist[196]}")
