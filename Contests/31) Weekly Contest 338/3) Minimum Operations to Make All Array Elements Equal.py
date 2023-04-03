"""
https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal
"""


def min_operations(nums: list[int], queries: list[int]) -> list[int]:
    """"""

    # Remark: It's a really good question for learning. 2-3 good algorithms/techniques are used to get the optimal time
    #         complexity.

    # For each query, you should decrease all elements greater than queries[i] and increase all elements less than
    # queries[i].
    # The answer is the sum of absolute differences between queries[i] and every element of the array. How do you
    # calculate that optimally?

    # 0) [TLE] Brute-force (Calc. the diff for each query using loop): TC = O(q*n); SC = O(1)

    """
    for q in queries:  # O(q * n)
        min_ops = 0
        for num in nums:  # O(n)
            min_ops += abs(num-q)
        yield min_ops
    """
    # One-liner:
    """
    yield from (sum(abs(num-q) for num in nums) for q in queries)
    """

    # 1) Optimal (Maths + Prefix Sum + Binary Search): TC = O((n+q) * log(n)); SC = O(n)
    # Main Technique: Calc. for smaller elements and larger elements separately!
    # https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/solutions/3341928/c-java-python3-prefix-sums-binary-search

    from itertools import accumulate
    from bisect import bisect_right

    # Sort Arr:
    nums = sorted(nums)  # TC = O(n*log(n)); SC = O(n)

    n = len(nums)

    # Build Prefix Sum Arr:
    '''
    ps = [0]
    for i in range(n):  # TC = O(n); SC = O(n)
        ps.append(ps[-1]+nums[i])
    '''
    # One-liner using `itertools.accumulate`:
    ps = list(accumulate(iterable=nums, initial=0))

    # Calc Ans:
    for q in queries:  # O(q * log(n))
        i = bisect_right(nums, q)  # O(log(n))
        # (q*i - (ps[i]-ps[0])) + (ps[n]-ps[i] - q*(n-i))
        # = (q*i - ps[i]) + (ps[n]-ps[i] - q*(n-i))
        # = (q * (2*i - n)) + (ps[n] - 2*ps[i])
        yield (q * (2*i - n)) + (ps[n] - 2*ps[i])
