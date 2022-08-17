"""
https://leetcode.com/problems/longest-consecutive-sequence
"""


def longest_consecutive(nums: list[int]) -> int:
    """"""

    # 0.1) [TLE] Brute-force (Nested Loop & HashSet): TC = O(n^2); SC = O(n)

    """
    nums = set(nums)  # (new local var); set for O(1) lookup

    longest = 0
    for num in nums:  # O(n^2)
        current = 1
        while (num := num+1) in nums:  # https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions
            current += 1
        longest = max(longest, current)
    return longest
    """

    # 0.2) Brute-force (Sorting): TC = O(n*log(n)); SC = O(n)

    """
    if not nums:  # edge case
        return 0

    nums = sorted(nums)  # (new local var)

    current = longest = 1
    for i in range(len(nums)-1):  # O(n)
        cur, nxt = nums[i], nums[i+1]
        if nxt == cur+1:  # => next element consecutive ✔
            current += 1
            longest = max(longest, current)
        # else: => next element not consecutive
        elif nxt != cur:  # if `nxt != cur` because for input [1, 2, 0, 1]; expected output is 3
            current = 1  # reset
    return longest
    """

    # 1) [MLE] Time-Optimal (Sorting using Counting Sort): TC = O(n); SC = O(max(nums)-min(nums))
    #                                                                 {Worst Case: max(nums)-min(nums) = 10^18}

    """
    if not nums:  # edge case
        return 0

    # Counting Sort: Sorting in TC = O(n); SC = O(max(nums)-min(nums))
    counts = {num: 0 for num in range(min(nums), max(nums)+1)}  # init
    for num in nums:  # counting
        counts[num] = counts.get(num, 0) + 1
    nums = []  # (new local var)
    for num, count in counts.items():
        nums.extend([num]*count)  # https://stackoverflow.com/q/3459098/create-list-of-single-item-repeated-n-times
    # print(nums)  #debug

    current = longest = 1
    for i in range(len(nums)-1):  # O(n)
        cur, nxt = nums[i], nums[i+1]
        if nxt == cur+1:  # => next element consecutive ✔
            current += 1
            longest = max(longest, current)
        # else: => next element not consecutive
        elif nxt != cur:  # if `nxt != cur` because for input [1, 2, 0, 1]; expected output is 3
            current = 1  # reset
    return longest
    """

    # Notice the only difference in this algo from `0.2)` is Sorting using Counting Sort,
    # which leads us from Linearithmic (Linear*Logarithmic) to Linear time.

    # 2) Optimal (HashSet): TC = O(n); SC = O(n)
    # This is an Easy problem! https://youtu.be/qgizvmgeyUM
    # https://leetcode.com/problems/longest-consecutive-sequence/discuss/41057/Simple-O(n)-with-Explanation-Just-walk-each-streak

    nums = set(nums)  # (new local var); set for O(1) lookup

    longest = 0
    for num in nums:  # O(n)
        if num-1 not in nums:  # finding the smallest num of a consecutive sequence
            current = 1
            while (num := num+1) in nums:  # https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions
                current += 1
            longest = max(longest, current)
    return longest

    # Notice the only difference in this algo from `0.1)` is the line `if num-1 not in nums:` 👌,
    # which intelligently leads us from Quadratic to Linear time!


# Similar Questions:
# https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number
# https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors
