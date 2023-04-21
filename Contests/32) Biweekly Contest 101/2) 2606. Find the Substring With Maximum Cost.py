"""
https://leetcode.com/problems/find-the-substring-with-maximum-cost
"""


def maximum_cost_substring(s: str, chars: str, vals: list[int]) -> int:
    """"""

    # Create a new integer array where arr[i] denotes the value of character s[i].
    # We can use Kadane’s maximum subarray sum algorithm to find the maximum cost.

    # 1) Optimal (HashMap + Kadane's Algo): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/find-the-substring-with-maximum-cost/solutions/3366705/java-c-python-kadane

    # Convert to dict for O(1) access: TC = SC = O(1) because "lowercase English letters"
    # hm = {char: val for char, val in zip(chars, vals)}
    hm = dict(zip(chars, vals))

    # Now, `004) Maximum Subarray.py` style: TC = O(n); SC = O(1)
    curr = mx = 0
    for char in s:
        curr = max(curr+hm.get(char, ord(char)-96), 0)  # add to current or reset
        mx = max(mx, curr)  # update ans
    return mx
