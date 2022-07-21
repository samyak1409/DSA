"""
https://leetcode.com/problems/majority-element
"""


def majorityElement(nums: list[int]) -> int:
    """"""

    # 0.1) Brute-force (Traverse and Count): TC = O(n^2); SC = O(1)
    # "element appears more than ⌊n / 2⌋ times" => count(x) > floor(n/2), so we can simply traverse the array to find the element.

    """
    n = len(nums)
    for num in nums:
        if nums.count(num) > n//2:
            return num
    """

    # 0.3) Brute-force (Sorting): TC = O(n*log(n)); SC = O(n)
    # Intuition: If an element x appears more than ⌊n / 2⌋ times (i.e. n >= count(x) > floor(n/2)),
    # then in sorted(nums), it'll be always present at position = floor(n/2)+1, i.e. index = floor(n/2)

    """
    return sorted(nums)[len(nums)//2]
    """

    # 0.2) Brute-force (HashMap): TC = O(n); SC = O(n)
    # Optimization of "0.1)" with the help of HashMap.

    """
    from collections import Counter
    count = Counter(nums)
    return max(count.keys(), key=count.get)  # max(count.keys(), key=lambda num: count[num])
    """
    # Better:
    count = {}
    n = len(nums)
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] > n//2:
            return num
