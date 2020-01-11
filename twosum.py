file = '/home/apuzyk/Documents/algorithms_coursera/algo1-programming_prob-2sum.txt'
with open(file) as f:
    o = f.readlines()

o = [int(i.rstrip()) for i in o]

o = dict.fromkeys(o, 1)
num_two_sums = 0
for t in range(-10000, 10001):
    for i in o.keys():
        if t-i != i:
            if o.get(t-i) is not None:
                num_two_sums += 1

print(num_two_sums)