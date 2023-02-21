"""
https://leetcode.com/problems/maximal-score-after-applying-k-operations
"""


def max_k_elements(nums: list[int], k: int) -> int:
    """"""

    # 1) Optimal (Heap (PQ)): TC = O(n + k*log(n)); SC = O(n) {O(1) if we modify the input `nums` only}
    # It is always optimal to select the greatest element in the array.
    # Use a heap to query for the maximum in O(log n) time.
    # https://youtu.be/WxtI_i3JfaM

    from heapq import heapify, heappop, heappush

    nums = [-num for num in nums]  # convert minheap to maxheap
    heapify(nums)  # TC = O(n)

    score = 0
    for _ in range(k):  # O(k * log(n))
        min_ = heappop(nums)  # O(log(n))
        score += -min_  # -min_ == max_
        heappush(nums, min_//3)  # 10//3 == 3 but -10//3 == -4 so we achieved "ceil(nums[i] / 3)" implicitly; O(log(n))
    return score
