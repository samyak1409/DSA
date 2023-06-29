"""
https://leetcode.com/problems/number-of-senior-citizens
"""


def count_seniors(details: list[str]) -> int:
    """"""

    # Convert the value at index 11 and 12 to a numerical value.
    # The age of the person at index i is equal to details[i][11]*10+details[i][12].

    # 1) Optimal (Slice, compare, and sum): TC = O(n); SC = O(1)

    return sum(d[11:13] > '60' for d in details)

    # Notice we didn't need int conversion, we directly compared the str representation of the numbers only.
    # Because it works, and you should know why.
