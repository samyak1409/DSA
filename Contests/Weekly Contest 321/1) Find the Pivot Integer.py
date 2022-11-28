"""
https://leetcode.com/problems/find-the-pivot-integer
"""


def pivot_integer(n: int) -> int:
    """"""

    # Can you use brute force to check every number from 1 to n if any of them is the pivot integer?
    # 0) Brute-force (Calc sum for every possible x): TC = O(n^2); SC = O(1)

    """
    for x in range(1, n+1):  # x -> pivot
        if sum(range(1, x+1)) == sum(range(x, n+1)):
            return x
    return -1
    """

    # If you know the sum of [1: pivot], how can you efficiently calculate the sum of the other parts?

    # 1.1) Better (Use the last sum to calc sum for every possible x): TC = O(n); SC = O(1)

    """
    sum_1_to_x, sum_x_to_n = sum(range(1, 0+1)), sum(range(0, n+1))  # init
    for x in range(1, n+1):  # x -> pivot
        if (sum_1_to_x := sum_1_to_x+x) == (sum_x_to_n := sum_x_to_n-(x-1)):
            # `+x` => include current x; `-(x-1)` => remove previous x
            return x
    return -1
    """

    # 1.2) Better (Use sum of n terms formula to calc sum for every possible x): TC = O(n); SC = O(1)

    sum_1st_n = n*(n+1)//2
    for x in range(1, n+1):  # x -> pivot
        if (sum_1st_x := x*(x+1)//2) == (sum_1st_n - sum_1st_x + x):  # `sum_1st_n - sum_1st_x + x` = sum_x_to_n
            return x
    return -1

    # 2) Optimal (?): TC = O(log(n)); SC = O(1)
    # https://leetcode.com/problems/find-the-pivot-integer/discuss
