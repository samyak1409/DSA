"""
https://leetcode.com/problems/find-all-k-distant-indices-in-an-array
"""


def find_k_distant_indices(nums: list[int], key: int, k: int) -> list[int]:
    """"""

    # 1) Time-Optimal (Traverse + HashSet): TC = O(nk); SC = O(n)
    # For every occurrence of key in nums, find all indices within distance k from it.
    # Use a hash table to remove duplicate indices.

    """
    n = len(nums)
    hashset = set()  # hash table to remove duplicate indices
    for i, num in enumerate(nums):  # for every occurrence of key in nums
        if num == key:
            for j in range(max(0, i-k), min(n-1, i+k)+1):  # all indices within distance k from num
                # `max(0, i-k)` & `min(n-1, i+k)` because start can't be < 0 and end can't be > n-1
                if j not in hashset:
                    yield j
                    hashset.add(j)
    """

    # 2) Optimal (Smartly Traverse): TC = O(n); SC = O(1)
    # Better of: https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/discuss/1844332/One-Pass

    n = len(nums)
    last_j = -1  # will track the last considered index
    for i, num in enumerate(nums):  # for every occurrence of key in nums
        if num == key:
            for j in range(max(last_j+1, i-k), min(n-1, i+k)+1):  # all indices within distance k from num
                # `max(last_j+1, i-k)` & `min(n-1, i+k)` because start can't be < last_j+1 and end can't be > n-1
                yield (last_j := j)  # without these "redundant parentheses":
            #   yield last_j := j
            #                ^^
            # SyntaxError: invalid syntax
