"""
https://leetcode.com/problems/minimum-time-to-break-locks-i
"""


def find_minimum_time(strength: list[int], k: int) -> int:
    """"""

    # Hint: Try all n! permutation ways of breaking the locks.

    # 1) Optimal (Permute & Calc. using Division): TC = O(n! * n) = O(n!); SC = O(n)
    # We can't apply greedy here (break the lock in increasing order of strength). See example test case 1.
    # Since `1 <= n <= 8`, this hints that we can just try all the permutations to get the optimal lock breaking order.
    # We just need to make sure that we calculate the time required for a permutation efficiently not by using a for
    # loop and passing the minutes one by one, but directly using maths (division).

    from itertools import permutations
    from math import ceil

    ans = float('inf')

    for perm in permutations(strength):  # TC = O(n!); SC = O(n)
        t = 0  # time in minutes
        x = 1  # "The initial factor `X` by which the energy of the sword increases is 1."
        for s in perm:  # TC = O(n); SC = O(1)
            t += ceil(s/x)  # "Every minute, the energy of the sword increases by the current factor `X`."
            # "After breaking a lock, the energy of the sword resets to 0, and the factor `X` increases by a given value
            # `K`.":
            # (Note that since the energy resets to 0 everytime we break lock, we don't need to track it.)
            x += k
        ans = min(ans, t)

    return ans
