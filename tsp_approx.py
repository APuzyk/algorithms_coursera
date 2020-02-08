from math import inf, sqrt
from itertools import combinations

file = '/home/apuzyk/Documents/algorithms_coursera/nn.txt'

#import points
with open(file) as f:
    o = f.readlines()
o = o[1:]
o = [list(map(float, i.rstrip().split(' ')[1:2])) for i in o]
def get_euclid_dist(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

curr_loc = o.pop(0)
start_point = curr_loc.copy()
total_dist = 0
while len(o) > 0:
    #get min dist
    min_dist = inf
    idx = None
    for i in range(o):
        pt_dist = get_euclid_dist(curr_loc, o[i])
        if pt_dist < min_dist:
            min_dist = pt_dist
            idx = i 
    total_dist += min_dist
    curr_loc = o.pop(idx)

total_dist += get_euclid_dist(start_point, curr_loc)

print(f"The answer is {total_dist}")

