"""
https://leetcode.com/problems/maximum-sum-with-exactly-k-elements
"""


def maximize_sum(nums: list[int], k: int) -> int:
    """"""

    # Translation:
    # Just find the max element, and add it to the ans, then ++ it (the max element), repeat this k times.

    # 1) Brute-force (Loop): TC = O(n+k); SC = O(1)

    """
    mx = max(nums)  # O(n)
    ans = 0
    for _ in range(k):  # O(k)
        ans += mx
        mx += 1
    return ans
    """

    # 2) Optimal (Maths): TC = O(1); SC = O(1)
    # https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/solutions/3466678/max-element-formula
    # Let's assume nums = [1, 3, 2]; k = 5
    # mx = 3
    # ans = mx + mx+1 + mx+2 + mx+3 + mx+4
    # => ans = mx*k + (k-1)*((k-1)+1)//2
    # (using sum of n terms formula)
    # => ans = mx*k + (k-1)*k//2

    return max(nums)*k + (k-1)*k//2
