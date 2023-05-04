"""
https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array
"""


def find_prefix_score(nums: list[int]) -> list[int]:
    """"""

    # Keep track of the prefix maximum of the array
    # Establish a relationship between ans[i] and ans[i-1]
    # for 0 < i < n: ans[i] = ans[i-1] + conversion[i]
    # In other words, array ans. is the prefix sum array of the conversion array.

    # 1) Optimal (Prefix Sum): TC = O(n); SC = O(1)

    mx = ans = 0
    for num in nums:
        '''
        mx = max(mx, num)
        ans += num + mx
        yield ans
        '''
        # One liner:
        yield (ans := ans + num + (mx := max(mx, num)))
        # (LeetCode gives `SyntaxError: invalid syntax` w/o these redundant parentheses.)
