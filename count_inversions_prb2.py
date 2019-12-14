def count_inv(a):
    if len(a) <= 1:
        return 0, a

    left_inv, b = count_inv(a[:int(len(a)/2)])
    right_inv, c = count_inv(a[int(len(a)/2):])

    split_inv, d = merge_and_count_split_inv(b, c)

    return (left_inv+right_inv+split_inv), d


def merge_and_count_split_inv(a, b):
    j = 0
    i = 0
    o = []
    inv = 0
    for k in range((len(a) + len(b))):
        if i > len(a) - 1:
            # Finished A - no more inversions
            o.extend(b[j:])
            break
        elif j > len(b) - 1:
            # Finished B no more inversions
            o.extend(a[i:])
            break
        elif a[i] < b[j]:
            o.append(a[i])
            i += 1
        else:
            o.append(b[j])
            j += 1
            inv += len(a[i:])
    return inv, o


with open('/home/apuzyk/Documents/algorithms_coursera/algorithms_coursera/IntegerArray.txt') as f:
    a = f.readlines()
a = [int(i) for i in a]


test = [1, 3, 5, 2, 4, 6]
assert count_inv(test)[0] == 3
test = [6, 5, 4, 3, 2, 1]
assert count_inv(test)[0] == 15
count_inv(a)[0]
2407905288