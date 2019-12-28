from collections import deque

file = '/home/apuzyk/Documents/algorithms_coursera/SCC.txt'

with open(file) as f:
    o = f.readlines()

o = [i.rstrip().split(' ') for i in o]
nodes = [j for i in o for j in i]
nodes = list(set(nodes))
len(nodes)

def dfs (g, )