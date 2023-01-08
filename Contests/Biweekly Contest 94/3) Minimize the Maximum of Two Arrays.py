"""
https://leetcode.com/problems/minimize-the-maximum-of-two-arrays
"""


def minimize_set(d1: int, d2: int, c1: int, c2: int) -> int:
    """"""

    # Use binary search to find the smallest maximum element.
    # Add numbers divisible by x in nums2 and vice versa.

    # 1) Sub-Optimal (Binary Search + Maths): TC = O(O(log(min(d1, d2))) + log(2^31 - 1)); SC = O(1)
    # https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/solutions/2946508/python-lcm-and-binary-search-explained-bonus-one-liner
    # https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/solutions/2946511/binary-search-venn-diagram-set-diagrams-explanation-with-diagram
    # https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/solutions/2947016/binary-search-on-answer-intuition-approach-explained-c

    from math import lcm
    # Definition: https://github.com/samyak1409/python-lab-assignments/blob/main/9/b.py

    lo, hi = 2, 2147483647  # `lo = 2` since "2 <= uniqueCnt1 + uniqueCnt2"
    # `hi = 2147483647` i.e. 2^31 - 1 i.e. max int (32-bit) (https://en.wikipedia.org/wiki/2,147,483,647#In_computing)
    # Python doesn't have int limit, but other langs have, so.
    d1d2 = lcm(d1, d2)  # TC = O(log(min(d1, d2)))
    # https://www.geeksforgeeks.org/time-complexity-of-euclidean-algorithm
    # https://www.baeldung.com/cs/euclid-time-complexity

    while lo < hi:
        val = (lo+hi) // 2
        if val-(val//d1) >= c1 and val-(val//d2) >= c2 and val-(val//d1d2) >= c1+c2:  # => `val` could be the ans
            hi = val  # compressing the search range: let's see if a smaller `val` satisfies the conditions
        else:  # => we need a bigger `val` in order to fill the arrays with the required conditions
            lo = val + 1  # compressing the search range: `val` can't be the ans, so `lo = val + 1`
    return hi  # or lo

    # Explanation of `if val-(val//d1) >= c1 and val-(val//d2) >= c2 and val-(val//d1d2) >= c1+c2`:
    # `val-(val//d1)   >= c1`   : ([1, val] - multiples of d1 in               [1, val]) >= c1
    # `val-(val//d2)   >= c2`   : ([1, val] - multiples of d2 in               [1, val]) >= c2
    # `val-(val//d1d2) >= c1+c2`: ([1, val] - multiples of d1 as well as d2 in [1, val]) >= c1+c2

    # Note that we could have done the Linear Search in place of Binary Search, but that would be very slow, and since
    # the `integers` are sorted, Binary Search is the correct choice.

    # 2) Optimal (Maths): TC = O(log(min(d1, d2))); SC = O(1)
    # https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/solutions/2947014/formula
