"""
https://leetcode.com/problems/find-the-punishment-number-of-an-integer
"""


def punishment_number(n: int) -> int:
    """"""

    # Can we generate all possible partitions of a number?
    # Use a recursive algorithm that splits the number into two parts, generates all possible partitions of each part
    # recursively, and then combines them in all possible ways.

    # 1) Optimal (Calc. all the partitions using Recursion): TC = O(n * 2^log10(n^2)); SC = O(log10(n^2))
    # {max(log10(n^2)) = log10(10^6) = 6 => TC = O(n * 2^6) = O(n); SC = O(6) = O(1)}
    # https://leetcode.com/problems/find-the-punishment-number-of-an-integer/solutions/3547280/0ms-tc-o-n-5-3-sc-o-log-n-most-efficient-solution-simplest-code

    # Recursive Function:
    def possible(sum_: int = 0, start: int = 0) -> bool:

        # Base Case:
        # When reached at the end of the str:
        if start == i_sq_len:
            # Return if sum == i or not:
            return sum_ == i

        # Recurse to form all the partitions:
        for j in range(i_sq_len-start):
            # As soon as any partition satisfies the condition, return True:
            if possible(sum_=sum_+int(i_sq_str[start:start+j+1]), start=start+j+1):
                return True
        # What the above indexing does is:
        # Let i_sq = 169, then it will get all the partitions like:
        # 1) 1 6 9
        # 2) 1 69
        # 3) 16 9
        # 4) 169

        # If no partition satisfies the condition:
        return False

    ans = 0
    # Find for all the numbers from 1 to n:
    for i in range(1, n+1):  # O(n * 2^log10(n^2))
        # Init some vars:
        i_sq = i * i
        i_sq_str = str(i_sq)
        i_sq_len = len(i_sq_str)
        # Check if any partition satisfies the condition using recursion:
        if possible():  # TC = O(2^log10(n^2)); SC = O(log10(n^2))
            # Add to the answer if any does:
            ans += i_sq
    return ans
