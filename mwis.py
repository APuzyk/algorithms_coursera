file = '/home/apuzyk/Documents/algorithms_coursera/mwis.txt'
with open(file) as f:
    o = f.readlines()

a = []
a[0] = 0
a[1] = o[0]
for i in range(2, len(o)+1):
    a[i] == max([a[i-1], a[i-2] + o[i-1]])

s = []
i = len(a) - 1

while i >= 2:
    if a[i-1] >= a[i-2] + o[i-1]:
        i -= 1
    else:
        s.append(i)
        i -= 2

    if i == 1:
        s.append(i)

to_check = [1, 2, 3, 4, 17, 117, 517, 997]

print(''.join([int(i in s) for i in to_check]))
