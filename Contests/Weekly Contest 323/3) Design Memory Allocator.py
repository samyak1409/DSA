"""
https://leetcode.com/problems/design-memory-allocator
"""


class Allocator:
    """"""

    # 1) Brute-force = Sub-Optimal (Do as told. Linearly allocate and de-allocate):
    # Can you simulate the process?
    # Use brute force to find the leftmost free block and free each occupied memory unit.

    # "`Allocator(int n)` Initializes an `Allocator` object with a memory array of size `n`."
    def __init__(self, n: int):  # TC = O(n); SC = O(n)
        self.arr = [0] * n  # will store `m_id`s

    # "`int allocate(int size, int m_id)` Find the leftmost block of `size` consecutive free memory units and allocate
    # it with the id `m_id`. Return the block's first index. If such a block does not exist, return `-1`."
    def allocate(self, size: int, m_id: int) -> int:  # TC = O(n^2); SC = O(1)
        consecutive_units = 0
        for i, unit in enumerate(self.arr):
            if not unit:  # i.e. free
                consecutive_units += 1
                if consecutive_units == size:  # found
                    for j in range((first_index := i-size+1), i+1):
                        self.arr[j] = m_id  # allocate
                    return first_index
            else:
                consecutive_units = 0  # reset
        return -1  # not found

    # "`int free(int m_id)` Free all memory units with the id `m_id`. Return the number of memory units you have freed."
    def free(self, m_id: int) -> int:  # TC = O(n); SC = O(1)
        units_freed = 0
        for i, unit in enumerate(self.arr):
            if unit == m_id:
                self.arr[i] = 0  # free
                units_freed += 1
        return units_freed

    # 2) Optimal (?):
    # https://leetcode.com/problems/design-memory-allocator/solutions/2899371/c-hashmap-vector-easy-approach

    """
    # "`Allocator(int n)` Initializes an `Allocator` object with a memory array of size `n`."
    def __init__(self, n: int):  # TC = O(?); SC = O(?)
        pass

    # "`int allocate(int size, int m_id)` Find the leftmost block of `size` consecutive free memory units and allocate
    # it with the id `m_id`. Return the block's first index. If such a block does not exist, return `-1`."
    def allocate(self, size: int, m_id: int) -> int:  # TC = O(?); SC = O(?)
        pass

    # "`int free(int m_id)` Free all memory units with the id `m_id`. Return the number of memory units you have freed."
    def free(self, m_id: int) -> int:  # TC = O(?); SC = O(?)
        pass
    """


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,m_id)
# param_2 = obj.free(m_id)
