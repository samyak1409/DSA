"""
https://leetcode.com/problems/minimum-time-to-repair-cars
"""


def repair_cars(ranks: list[int], cars: int) -> int:
    """"""

    # For a predefined fixed time, can all the cars be repaired?
    # Try using binary search on the answer.

    # MIN-MAX PROBLEM (Minimize the Maximum)
    # Code struct taken from
    # https://github.com/samyak1409/DSA/blob/main/Contests/21%29%20Weekly%20Contest%20331/3%29%20House%20Robber%20IV.py.

    # 1) Optimal (Binary Search): TC = O(log2(max(ranks)*cars^2) * len(ranks)); SC = O(1)
    # https://leetcode.com/problems/minimum-time-to-repair-cars/solutions

    from math import isqrt

    # Helper Function:
    def check(time: int) -> bool:  # TC = O(n)
        # Check if in this time, all the cars can be repaired or not:
        left = cars
        for r in ranks:
            # r * c^2 <= time
            '''
            c = 0
            while r * c**2 <= time:
                c += 1
            left -= c
            '''
            # One liner:
            # r * c^2 <= time => c <= sqrt(time//r); so optimal c = isqrt(time//r)
            left -= isqrt(time//r)
            if left <= 0:
                return True

    # https://en.wikipedia.org/wiki/Binary_search_algorithm#Procedure_for_finding_the_leftmost_element:
    lo, hi = 1, max(ranks) * cars**2
    while lo < hi:  # O(log2(max(ranks)*cars^2))
        guess = (lo + hi) // 2
        if check(guess):  # current guess is valid, let's see if we can get a smaller valid guess
            hi = guess
        else:  # count < k, guess was invalid, we need a larger guess
            lo = guess + 1
    return lo  # or hi

    # 2) ? (Heap): TC = O(?); SC = O(?)
    # Solution 2 in
    # https://leetcode.com/problems/minimum-time-to-repair-cars/solutions/3312003/java-c-python-binary-search-and-heap-solution
