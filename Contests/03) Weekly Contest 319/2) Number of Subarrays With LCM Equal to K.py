"""
https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k
"""


def subarray_lcm(nums: list[int], k: int) -> int:
    """"""

    # 1) Optimized Brute-force / Sub-Optimal (Check every Subarray but use running LCM): TC = O(n^2 * log(n)); SC = O(1)
    # The constraints on nums.length are small. It is possible to check every subarray.
    # To calculate LCM, you can use a built-in function or the formula lcm(a, b) = a * b / gcd(a, b).
    # As you calculate the LCM of more numbers, it can only become greater. Once it becomes greater than k,
    # you know that any larger subarrays containing all the current elements will not work.

    from math import lcm
    # Definition: https://github.com/samyak1409/python-lab-assignments/blob/main/9/b.py

    n = len(nums)
    count = 0
    for i in range(n):
        lcm_ = 1  # neutral init
        for j in range(i, n):
            if (num := nums[j]) > k:  # optimization: if num is > required lcm (k), then lcm of any subsequent subarray
                # can't be = k (would be > k)
                break
            if (lcm_ := lcm(lcm_, num)) == k:  # imp part: finding next lcm using current lcm
                # TC = O(log(min(a, b))) = O(log(n))
                # https://www.geeksforgeeks.org/time-complexity-of-euclidean-algorithm
                # https://www.baeldung.com/cs/euclid-time-complexity
                count += 1
    return count

    # 2) Optimal (?): TC = O(?); SC = O(?)
    # https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/solutions/2808843/o-n-d-k-log-k
