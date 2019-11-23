# basic implementation of merge sort


# merge subroutine
def merge(a, b):
    j = 0
    i = 0
    o = []
    for k in range((len(a) + len(b))):
        if i > len(a) - 1:
            o.extend(b[j:])
            break
        elif j > len(b) - 1:
            o.extend(a[i:])
            break
        elif a[i] < b[j]:
            o.append(a[i])
            i += 1
        else:
            o.append(b[j])
            j += 1
    return o

def merge_sort(c):
    if len(c) <= 1:
        return c

    a = c[:int(len(c)/2)]
    b = c[int(len(c)/2):]
    a = merge_sort(a)
    b = merge_sort(b)
    return merge(a, b)