"""
https://leetcode.com/problems/take-gifts-from-the-richest-pile
"""


def pick_gifts(gifts: list[int], k: int) -> int:
    """"""

    # How can you keep track of the largest gifts in the array?
    # What is an efficient way to find the square root of a number?
    # Can you keep adding up the values of the gifts while ensuring they are in a certain order?
    # Can we use a priority queue or heap here?

    # 1) Optimal (Max Heap): TC = O(n + k*log(n)); SC = O(n)
    # https://leetcode.com/problems/take-gifts-from-the-richest-pile/solutions/3143755/make-heap

    from heapq import heapify, heappop, heappush

    gifts = [-gift for gift in gifts]  # python heap is min-heap by default, converting to max-heap; O(n)

    heapify(gifts)  # O(n)

    for _ in range(k):  # O(k*log(n))
        # "Choose the pile with the maximum number of gifts."
        # "Leave behind the floor of the square root of the number of gifts in the pile."
        heappush(gifts, -int((-heappop(gifts))**.5))  # O(log(n))
        # Note: negating then sqrt-ing, because sqrt(-ve num) == a complex num, and so giving error on leetcode

    return -sum(gifts)  # O(n)
