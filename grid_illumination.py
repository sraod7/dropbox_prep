import collections
from typing import List

NBRS = [[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]


class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        # making it a tuple set to make lookup and removal easy
        lamps_on = set()

        # hashmaps to store the count of lamps of rows, cols, diagonal and anti-diagonal
        rows = collections.defaultdict(int)
        cols = collections.defaultdict(int)
        diag = collections.defaultdict(int)
        anti_diag = collections.defaultdict(int)

        # get the count of lamps on rows, cols, diagonal and anti-diagonal
        for i, j in lamps:
            lamps_on.add((i, j))
            rows[i] += 1
            cols[j] += 1
            diag[j - i] += 1
            anti_diag[j + i - N] += 1

        result = []

        for i, j in queries:
            # if row, col, diag or anti-diagonal has a lamp, then the query location is lit
            result.append(1 if rows[i] or cols[j] or diag[j - i] or anti_diag[j + i - N] else 0)

            # turn off the lamp if it's one step away from the query location.
            for x, y in NBRS:
                i_ = i + x
                j_ = j + y

                if (i_, j_) in lamps_on:
                    rows[i_] -= 1
                    cols[j_] -= 1
                    diag[j_ - i_] -= 1
                    anti_diag[j_ + i_ - N] -= 1
                    lamps_on.remove((i_, j_))

        return result