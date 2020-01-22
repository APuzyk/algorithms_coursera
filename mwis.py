file = '/home/apuzyk/Documents/algorithms_coursera/mwis.txt'
with open(file) as f:
    o = f.readlines()

o = [int(i.rstrip()) for i in o[1:]]
a = list()
a.append(0)
a.append(o[0])
for i in range(2, len(o)+1):
    a.append(max([a[i-1], a[i-2] + o[i-1]]))

s = []
i = len(a) - 1

while i >= 2:
    if a[i-1] >= a[i-2] + o[i-1]:
        i -= 1
    else:
        s.append(i) #nice because reindexes to 1
        i -= 2

    if i == 1:
        # if we land on the one case we didn't include 2
        # so include it
        s.append(i)

to_check = [1, 2, 3, 4, 17, 117, 517, 997]

print(''.join([str(int(i in s)) for i in to_check]))
