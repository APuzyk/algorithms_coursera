weights = [.2,.05,.17,.1,.2,.03,.25]
a = [[0] * (len(weights) + 1) for i in range(len(weights) + 1)]

for i in range(len(a)):
    a[i][i] = 0

for s in range(len(weights)):
    for i in range(len(weights)-s):
        to_check = []
        for k in range(i, i+s):

