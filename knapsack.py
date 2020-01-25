class KnapsackFiller:
    def __init__(self, size, items):
        self.size = size
        self.items = items
        self._to_fill = []
        self._last_pass = []

    def fill_knapsack(self):
        self.forward_pass()
        self.reconstruct()

    def forward_pass(self):
        self._to_fill = [[None] * (self.size + 1) for i in range(len(self.items) + 1)]
        for i in range(self.size + 1):
            self._to_fill[0][i] = 0

        for i in range(1, len(self.items)+1):
            for c in range(self.size + 1):
                s_i = self.items[i-1][1]
                if s_i > c:
                    self._to_fill[i][c] = self._to_fill[i-1][c]
                else:
                    o_1 = self._to_fill[i-1][c]
                    if c - s_i > 0:
                        o_2 = self._to_fill[i - 1][c - s_i] + self.items[i - 1][0]
                    else:
                        o_2 = self._to_fill[i - 1][0] + self.items[i - 1][0]
                    self._to_fill[i][c] = max([o_1, o_2])

    def forward_pass_copy(self):
        self._to_fill = [[None] * (self.size + 1) for i in range(len(self.items) + 1)]
        for i in range(self.size + 1):
            self._to_fill[0][i] = 0

        for i in range(1, len(self.items)+1):
            for c in range(self.size + 1):
                s_i = self.items[i-1][1]
                if s_i > c:
                    self._to_fill[i][c] = self._to_fill[i-1][c]
                else:
                    o_1 = self._to_fill[i-1][c]
                    if c - s_i > 0:
                        o_2 = self._to_fill[i - 1][c - s_i] + self.items[i - 1][0]
                    else:
                        o_2 = self._to_fill[i - 1][0] + self.items[i - 1][0]
                    self._to_fill[i][c] = max([o_1, o_2])

    def forward_pass_noreconstruction(self):
        self._last_pass = [0]*(self.size + 1)

        for i in range(1, len(self.items)+1):
            print(f"Run {i} of {len(self.items)}")
            curr_pass = [0] * (self.size + 1)
            for c in range(self.size + 1):
                s_i = self.items[i-1][1]
                v_i = self.items[i - 1][0]
                if s_i > c:
                    curr_pass[c] = self._last_pass[c]
                else:
                    o_1 = self._last_pass[c]
                    if c - s_i > 0:
                        o_2 = self._last_pass[c - s_i] + v_i
                    else:
                        o_2 = self._last_pass[0] + v_i
                    curr_pass[c] = max([o_1, o_2])
            self._last_pass = curr_pass

    def reconstruct(self):
        pass

    def get_total_value_fast(self):
        return self._last_pass[-1]
    def get_total_value(self):
        if len(self._to_fill) == 0:
            raise RuntimeError

        return self._to_fill[len(self.items)][self.size]

file = '/home/apuzyk/Documents/algorithms_coursera/knapsack1.txt'
with open(file) as f:
    o = f.readlines()

#problem 1
o = [list(map(int, i.rstrip().split(' '))) for i in o]
size = o.pop(0)[0]
kf = KnapsackFiller(size=size, items=o)
kf.fill_knapsack()

print(f"answer to problem 1 is: {kf.get_total_value()}")
kf.forward_pass_noreconstruction()
print(f"answer to problem 1 is: {kf.get_total_value_fast()}")

#problem 2
file = '/home/apuzyk/Documents/algorithms_coursera/knapsack_big.txt'
with open(file) as f:
    o = f.readlines()

o = [list(map(int, i.rstrip().split(' '))) for i in o]
size = o.pop(0)[0]
items = o

kf_big = KnapsackFiller(size=size, items=items)

kf_big.forward_pass_noreconstruction()
print(f"answer to problem 2: {kf_big.get_total_value_fast()}")