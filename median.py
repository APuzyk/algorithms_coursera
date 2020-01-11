from statistics import median
import heapq

file = '/home/apuzyk/Documents/algorithms_coursera/Median.txt'
with open(file) as f:
    o = f.readlines()

o = [int(i.rstrip()) for i in o]

def test_median(a):
    o = []
    for i in range(len(a)):
        o.append(median(a[0:(i+1)]))

    return sum(o)%10000

def median_maint(a):
    left = []
    heapq.heapify(left) # max heap
    right = []
    heapq.heapify(right)
    medians = []
    for i in a:
        # Insert first
        #pick top of left if they're equal
        if len(left) == 0 and len(right) == 0:
            heapq.heappush(left, i*-1)
        elif left[0]*-1 > i:
            # It's in left
            heapq.heappush(left, i*-1)
        elif right[0] < i or len(right) == 0:
            # it's in right
            heapq.heappush(right, i)
        else:
            #it's between the two
            if len(right) <= len(left):
                heapq.heappush(right, i)
            else:
                heapq.heappush(left, i*-1)
        # fix the heap
        if len(left) >= len(right) + 2:
            heapq.heappush(right, -1 * heapq.heappop(left))
        elif len(left) + 2 <= len(right):
            heapq.heappush(left, -1 * heapq.heappop(right))

        # output median
        if len(left) < len(right):
            medians.append(right[0])
        else:
            medians.append(left[0]*-1)

    return sum(medians)%10000

print(median_maint(o))
print(test_median(o)) #uses mid point in even scenario so it's useless here
