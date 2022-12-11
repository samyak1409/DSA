"""
https://leetcode.com/problems/design-memory-allocator
"""


class Allocator:

    def __init__(self, n: int):
        self.arr = [None] * n  # store mID
        
    def allocate(self, size: int, mID: int) -> int:
        size_so_far = 0
        for i, unit in enumerate(self.arr):
            if unit is None:
                size_so_far += 1
                if size_so_far == size:
                    self.arr[(first_index:=i-size+1):i+1] = [mID] * size  # allocate
                    return first_index
            else:
                size_so_far = 0  # reset
        return -1  # can not find any free block with `size` consecutive free memory units

    def free(self, mID: int) -> int:
        units_freed = 0
        for i, unit in enumerate(self.arr):
            if unit == mID:
                self.arr[i] = None  # free
                units_freed += 1
        return units_freed


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
