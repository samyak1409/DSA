"""
https://leetcode.com/problems/min-stack/
"""


class MinStack:  # TC = O(1); SC = O(n)

    def __init__(self):
        self.stack = list()
        self.cur_min = float('inf')  # tracking current minimum element so that getMin() in O(1)

    def push(self, val: int) -> None:
        if val < self.cur_min:
            self.cur_min = val  # new cur_min
        self.stack.append((val, self.cur_min))  # smart part! (maintaining a min for every val!)

    def pop(self) -> None:
        if self.stack.pop()[1] == self.cur_min:  # if popped min was cur_min
            # EAFP https://docs.python.org/3/glossary.html#term-EAFP
            try:  # updating cur_min
                self.cur_min = self.stack[-1][1]  # (stack is (LIFO) LAST IN, so min value will be ✔)
            except IndexError:  # popped item was last item in the stack, empty stack now
                self.cur_min = float('inf')  # default

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> (int, float):
        return self.cur_min

    # Also, worth checking: https://leetcode.com/problems/min-stack/discuss/49010/Clean-6ms-Java-solution


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
