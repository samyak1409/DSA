"""
https://leetcode.com/problems/longest-consecutive-sequence
"""


def longest_consecutive(nums: list[int]) -> int:
    """"""

    # 0) Brute-force (Sorting): TC = O(n*log(n)); SC = O(n)

    """
    if not nums:  # edge case
        return 0

    nums = sorted(set(nums))  # (new local var); TC = O(n + n*log(n)); SC = O(n+n)
    # set because for input [1, 2, 0, 1]; expected output is 3

    longest_length = current_length = 1
    for i in range(len(nums)-1):  # TC = O(n)
        if nums[i+1] == nums[i]+1:
            current_length += 1
        else:
            current_length = 1  # reset
        if current_length > longest_length:
            longest_length = current_length
    return longest_length
    """

    # 1) [MLE] Time-Optimal (Sorting using Counting Sort): TC = O(n); SC = O(max(nums)-min(nums))
    #                                                                 {Worst Case: max(nums)-min(nums) = 10^18}

    """
    if not nums:  # edge case
        return 0

    nums = set(nums)  # (new local var); TC = O(n); SC = O(n)
    # set because for input [1, 2, 0, 1]; expected output is 3

    # Counting Sort: Sorting in TC = O(n); SC = O(max(nums)-min(nums))
    counts = {num: 0 for num in range(min(nums), max(nums)+1)}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    nums = []
    for num, count in counts.items():
        [nums.append(num) for _ in range(count)]
    # print(nums)  #debug

    longest_length = current_length = 1
    for i in range(len(nums)-1):  # TC = O(n)
        if nums[i+1] == nums[i]+1:
            current_length += 1
        else:
            current_length = 1  # reset
        if current_length > longest_length:
            longest_length = current_length
    return longest_length
    """

    # 2) Optimal (HashSet): TC = O(n); SC = O(n)
    # This is an Easy problem! https://youtu.be/qgizvmgeyUM
    # https://leetcode.com/problems/longest-consecutive-sequence/discuss/41057/Simple-O(n)-with-Explanation-Just-walk-each-streak

    nums = set(nums)  # (new local var); set for O(1) lookup; TC = O(n); SC = O(n)

    longest_length = 0
    for num in nums:
        if num-1 not in nums:  # finding the smallest num of a consecutive sequence
            current_length = 1
            while num+1 in nums:  # next num in consecutive sequence
                current_length += 1
                num += 1
            if current_length > longest_length:
                longest_length = current_length
    return longest_length
