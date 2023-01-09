"""
https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream
"""


class DataStream:
    """"""

    # This one is tricky, we don't need here to make and maintain any data stream, just count smartly!

    # 1) Optimal (Count Streak):
    # https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/solutions/3015022/c-o-n-to-o-1-memory-queue-count

    def __init__(self, value: int, k: int):  # TC = O(1); SC = O(1)
        self.value = value
        self.k = k
        self.streak = 0

    def consec(self, num: int) -> bool:  # TC = O(1); SC = O(1)
        if num == self.value:
            self.streak += 1
        else:
            self.streak = 0  # reset
        return self.streak >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
