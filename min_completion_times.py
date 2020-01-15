file = '/home/apuzyk/Documents/algorithms_coursera/jobs.txt'

with open(file) as f:
    o = f.readlines()

o = [i.rstrip().split(' ') for i in o][1:]

o = [[int(i[0]), int(i[1])] for i in o]

# based on differences

diff_a = [i + [i[0]-i[1]] for i in o]
#struct = [weight, length, weight-length]

diff_a = sorted(diff_a, key=lambda x: (-1*x[2], -1*x[0]))

for i in range(len(diff_a)):
    if i == 0:
        diff_a[i].append(diff_a[i][1])
        diff_a[i].append(diff_a[i][3] * diff_a[i][0])
    else:
        diff_a[i].append(diff_a[i][1] + diff_a[i-1][3])
        diff_a[i].append(diff_a[i][3] * diff_a[i][0])

print(sum([i[4] for i in diff_a]))
# 69119377652

## by divisor
div_a = [i + [i[0]/i[1]] for i in o]
#struct = [weight, length, weight/length]

div_a = sorted(div_a, key=lambda x: -1*x[2])

for i in range(len(div_a)):
    if i == 0:
        div_a[i].append(div_a[i][1])
        div_a[i].append(div_a[i][3] * div_a[i][0])
    else:
        div_a[i].append(div_a[i][1] + div_a[i-1][3])
        div_a[i].append(div_a[i][3] * div_a[i][0])

print(sum([i[4] for i in div_a]))
# 67311454237