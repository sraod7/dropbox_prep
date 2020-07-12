class PhoneDirectory:
    def __init__(self, max_number):
        self.tree = [True] * 2 * max_number
        self.max_number = max_number

    def get(self):
        if self.tree[1] == False:
            return -1

        i = 1
        while i < len(self.tree) / 2:
            left = 2 * i
            right = 2 * i + 1
            if left < len(self.tree) and self.tree[left] == True:
                i = left
            if right < len(self.tree) and self.tree[right] == True:
                i = right

        ret = i - self.max_number

        # update the tree
        self.tree[i] = False

        i //= 2
        while i > 0:
            left = 2 * i
            right = 2 * i + 1
            self.tree[i] = self.tree[left] or self.tree[right]
            i //= 2

        return ret

    def check(self, number):
        return self.tree[number + self.max_number]

    def release(self, number):
        i = self.max_number + number
        while i > 0:
            self.tree[i] = True
            i //= 2