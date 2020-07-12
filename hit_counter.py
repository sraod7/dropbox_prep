TIMESTAMP_SIZE = 300


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = [[0, i + 1] for i in range(TIMESTAMP_SIZE)]

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        idx = (timestamp - 1) % TIMESTAMP_SIZE

        if self.counter[idx][1] == timestamp:
            self.counter[idx][0] += 1
        else:
            self.counter[idx] = [1, timestamp]

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        count = 0
        for i in range(TIMESTAMP_SIZE):
            if timestamp - self.counter[i][1] < 300:
                count += self.counter[i][0]

        return count
