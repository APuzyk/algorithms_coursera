from math import inf, sqrt
from itertools import combinations

file = '/home/apuzyk/Documents/algorithms_coursera/tsp.txt'

#import points
with open(file) as f:
    o = f.readlines()
o = o[1:]
o = [list(map(float, i.rstrip().split(' '))) for i in o]

# Create initial distance dict
# 0 for starting point else inf
curr_dist_dict = {}
for i in range(len(o)):
    bm = ['0'] * len(o)
    bm[i] = '1'
    if i == 0:
        curr_dist_dict[int(''.join(bm), 2)] = {0: 0}
    else:
        curr_dist_dict[int(''.join(bm), 2)] = {i: inf}


def get_euclid_dist(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


for m in range(1, len(o)):
    #sets of size m that contain 0
    print(f"Iterations {m} of {len(o)}")

    new_dist_dict = {} #store for this iteration

    # go through combinations that have m length
    # and include our points not 0
    for s in combinations(range(1, len(o)), m):
        # zero always true
        bm_s = ['1'] + ['0']*(len(o)-1)
        #set to 1 for points in this set
        for i in s:
            bm_s[i] = '1'

        #our current iteration
        bm_s_int = int(''.join(bm_s), 2)

        for j in s:
            #get previous s without j
            prev_bm = [i for i in bm_s]
            prev_bm[j] = '0'

            #find min for this destination
            # given previos subset of points not including this one
            new_min = inf
            if curr_dist_dict.get(int(''.join(prev_bm), 2)) is not None:
                for k, v in curr_dist_dict.get(int(''.join(prev_bm), 2)).items():
                    new_min = min([new_min, get_euclid_dist(o[k], o[j]) + v])
                if new_dist_dict.get(bm_s_int) is not None:
                    new_dist_dict[bm_s_int][j] = new_min
                else:
                    new_dist_dict[bm_s_int] = {j:new_min}

    # we're done searching for sets of this size let's use it next
    curr_dist_dict = new_dist_dict

#for the set of all points find
# the shortest path from some endpoint to the origin
min_dist = inf
for k, v in curr_dist_dict.items():
    for m, n in v.items():
        min_dist = min(min_dist,
                       get_euclid_dist(o[0], o[m]) + n)

print(f"The answer is: {min_dist}")