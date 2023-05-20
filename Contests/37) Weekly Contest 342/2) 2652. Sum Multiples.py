"""
https://leetcode.com/problems/sum-multiples
"""


def sum_of_multiples(n: int) -> int:
    """"""

    # 1) Brute-force (Loop): TC = O(n); SC = O(1)
    # Iterate through the range 1 to n and count numbers divisible by either 3, 5, or 7.

    """
    ans = 0
    for x in range(1, n+1):
        if x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
            ans += x
    return ans
    """

    # One-liner:
    """
    return sum(x for x in range(1, n+1) if x % 3 == 0 or x % 5 == 0 or x % 7 == 0)
    """

    # 2) Optimal (Maths: Sets + AP/Sum of n terms): TC = O(1); SC = O(1)
    # i) we'll find sum of multiples of 3, sum of multiples of 5, and sum of multiples of 7.
    # but wait, some multiples will be counted twice, e.g. 15 because it's a multiple of 3 as well as 5.
    # So there comes Sets. See how to remove duplicates:
    # https://leetcode.com/problems/sum-multiples/solutions/3445711/kotlin-o-1-with-diagram
    # ii) now to actually calc. the sum of multiples of x, we will use AP / sum of n terms, see:
    # Take n = 10, so range = [1, 10]; and x = 3
    # multiples would be = 3, 6, 9; sum = 3 + 6 + 9
    # if we take 3 common: 3 * (1 + 2 + 3)
    # = x * (sum of n_ terms where n_ = n // x)
    # https://leetcode.com/problems/sum-multiples/solutions/3446041/greedy-o-n-o-1-solution-very-simple-easy-to-understand

    # Helper functions:
    sum_of_n_terms = lambda n_: n_*(n_+1) // 2
    sum_of_multiples_ = lambda x: x * sum_of_n_terms(n_=n//x)
    # (PEP 8 recommends using def for function definitions instead of assigning lambda expressions to variables for
    # better readability and maintainability.)

    return sum_of_multiples_(3) + sum_of_multiples_(5) + sum_of_multiples_(7) \
        - sum_of_multiples_(15) - sum_of_multiples_(21) - sum_of_multiples_(35) \
        + sum_of_multiples_(105)
