import heapq

class Node:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None


class HuffmanCodes:
    def __init__(self, nodes, weights):
        self.code_dict = {}

        self.heap = []
        if len(nodes) != len(weights):
            raise RuntimeError
        for i in range(len(nodes)):
            self.heap.append([weights[i], nodes[i]])

        heapq.heapify(self.heap)

    def create_graph(self):
        while len(self.heap) > 1:
            # Pop Two Lowest Weights
            t1 = heapq.heappop(self.heap)
            t2 = heapq.heappop(self.heap)

            # create new node and push with weight of below
            t3 = Node(name=None, left=t1[1], right=t2[1])
            heapq.heappush(self.heap, [t1[0] + t2[0], t3])

    def create_codes(self):
        if len(self.heap) > 1:
            raise RuntimeError("heap too big, did you create the graph")
        self._descend(self.heap[0][1].left, [0])
        self._descend(self.heap[0][1].right, [1])


    def _descend(self, node, curr_path):
        if node.is_leaf():
            self.code_dict[node.name] = curr_path
        else:
            left_path = curr_path + [0]
            right_path = curr_path + [1]

            self._descend(node.left, left_path)
            self._descend(node.right, right_path)



file = '/home/apuzyk/Documents/algorithms_coursera/huffman.txt'
with open(file) as f:
    o = f.readlines()

o = [int(i.rstrip()) for i in o[1:]]
nodes = []
for i in range(len(o)):
    nodes.append(Node(i))

hm = HuffmanCodes(nodes, o)
hm.create_graph()
hm.create_codes()

print('max len is: {}'.format(max([len(i) for i in hm.code_dict.values()])))

print('min len is: {}'.format(min([len(i) for i in hm.code_dict.values()])))
