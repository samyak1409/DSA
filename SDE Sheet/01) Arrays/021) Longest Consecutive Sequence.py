"""
https://leetcode.com/problems/longest-consecutive-sequence
"""


def longest_consecutive(nums: list[int]) -> int:
    """"""

    # 0.1) [TLE] Brute-force (Nested Loop & HashSet): TC = O(n^2); SC = O(n)

    """
    hs = set(nums)  # for O(1) lookup

    longest = 0
    for num in hs:  # O(n^2)
        curr = 1
        while (num := num+1) in hs:
            curr += 1
        longest = max(longest, curr)
    return longest
    """

    # 0.2) Brute-force (Sorting): TC = O(n*log(n)); SC = O(n)

    """
    if not nums:  # edge case
        return 0

    nums = sorted(nums)  # (new local var)

    longest = curr = 1
    for i in range(len(nums)-1):  # O(n)
        cur, nxt = nums[i], nums[i+1]
        if nxt == cur+1:  # => next element consecutive
            curr += 1
            longest = max(longest, curr)
        # else: => next element not consecutive
        elif nxt != cur:  # `nxt != cur`: because we need to do nothing & continue (basically skip) and not reset if 
            # nxt == cur (e.g.: Input: [1, 2, 0, 1]; Output: 3)
            curr = 1  # reset
    return longest
    """
    # Better implementation:
    """
    curr = longest = 0
    prev = None
    for num in sorted(set(nums)):  # imp: using `set`
        if num-1 == prev:
            curr += 1
        else:
            curr = 1
        longest = max(longest, curr)
        prev = num
    return longest
    """

    # `-10^9 <= nums[i] <= 10^9`: This is also too much, else we could've used a freq arr (arr as a hashmap) to first
    # count and save the freq, then looped on it like above.
    # 1) [MLE] Time-Optimal (Sorting using Counting Sort): TC = O(n); SC = O(max(nums)-min(nums))
    #                                                                 {Worst Case: max(nums)-min(nums) = 10^18}

    # 2) Optimal (HashSet): TC = O(n); SC = O(n)
    # This is an Easy problem! https://youtu.be/qgizvmgeyUM
    # https://leetcode.com/problems/longest-consecutive-sequence/discuss/41057/Simple-O(n)-with-Explanation-Just-walk-each-streak

    hs = set(nums)  # for O(1) lookup

    longest = 0
    for num in hs:  # O(n)
        if num-1 not in hs:  # finding the smallest num of a consecutive sequence
            curr = 1
            while (num := num+1) in hs:
                curr += 1
            longest = max(longest, curr)
    return longest

    # Notice the only difference in this algo from `0.1)` is addition of the line `if num-1 not in nums:` 👌,
    # which intelligently leads us from Quadratic to Linear time!


# Similar Questions:
# https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number
# https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors
# https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring
