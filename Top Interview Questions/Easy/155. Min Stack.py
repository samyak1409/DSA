"""
https://leetcode.com/problems/min-stack/
"""


class MinStack:

    def __init__(self):
        self.stack = list()
        self.cur_min = float('inf')  # tracking current minimum element so that getMin() in O(1)

    def push(self, val: int) -> None:
        if val < self.cur_min:
            self.cur_min = val  # new cur_min
        self.stack.append((val, self.cur_min))

    def pop(self) -> None:
        if self.stack.pop()[1] == self.cur_min:  # if popped min was cur_min
            self.cur_min = self.stack[-1][1] if self.stack else float('inf')  # updating cur_min

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> (int, float):
        return self.cur_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
