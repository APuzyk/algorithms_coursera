def quick_sort(a, l=None, r=None):
    if l is None and r is None:
        l = 0
        r = len(a)-1

    if l >= r:
        return a, 0

    p = get_pivot(a, l, r)
    a1 = a[l]
    a[l] = a[p]
    a[p] = a1
    i = l+1
    comparisons = 0
    for j in range((l+1), (r+1)):
        if a[j] <= a[l]:
            comparisons += 1
            hold = a[j]
            a[j] = a[i]
            a[i] = hold
            i += 1
        else:
            comparisons += 1
    hold = a[i-1]
    a[i-1] = a[l]
    a[l] = hold

    a, c_l = quick_sort(a, l, (i-2))
    a, c_r = quick_sort(a, i, r)
    comparisons = c_l + c_r + comparisons
    return a, comparisons


with open('/home/apuzyk/Documents/algorithms_coursera/QuickSort.txt') as f:
    to_sort = f.readlines()
    to_sort = [int(i) for i in to_sort]



def get_pivot(a, l, r):
    return l
o, c = quick_sort(to_sort)
print('comparisons first element pivot: {}'.format(c))
to_sort.sort()

assert o == to_sort


with open('/home/apuzyk/Documents/algorithms_coursera/QuickSort.txt') as f:
    to_sort = f.readlines()
    to_sort = [int(i) for i in to_sort]



def get_pivot(a, l, r):
    return r

o, c = quick_sort(to_sort)
print('comparisons last element pivot: {}'.format(c))
to_sort.sort()
assert o == to_sort


with open('/home/apuzyk/Documents/algorithms_coursera/QuickSort.txt') as f:
    to_sort = f.readlines()
    to_sort = [int(i) for i in to_sort]



def get_pivot(a, l, r):
    length = ((r-l) + 1)
    middle = length/2

    if int(middle)*2 != length:
        middle = int(middle)
    else:                      
        middle = int(middle
                     C
        CCC) - 1

    middle += l

    if a[r] < a[l] < a[middle]:
        return l
    if a[middle] < a[l] < a[r]:
        return l
    if a[l] < a[middle] < a[r]:
        return middle
    if a[r] < a[middle] < a[l]:
        return middle
    return r


o, c = quick_sort(to_sort)
print('comparisons: {}'.format(c))
to_sort.sort()
assert o == to_sort

