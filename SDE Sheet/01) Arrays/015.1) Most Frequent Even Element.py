"""
https://leetcode.com/problems/most-frequent-even-element
"""


def most_frequent_even(nums: list[int]) -> int:
    """"""

    # 1) Optimal (Traverse the even elements, and Track Max Freq using HashMap): TC = O(n); SC = O(n)
    # Could you count the frequency of each even element in the array?
    # Would a hashmap help?
    # https://leetcode.com/problems/most-frequent-even-element/solutions/2560064/single-pass-with-comments-c-java-python

    # With Sorting: O(n*log(n))
    """
    freq = {}
    ans, max_freq = -1, 0
    for num in sorted(filter(lambda x: x % 2 == 0, nums)):  # only sorting & traversing even elements
        freq[num] = f = freq.get(num, 0) + 1
        if f > max_freq:
            ans, max_freq = num, f
    # print(freq)  #debugging
    return ans
    """

    # We can do it without Sorting, by just adding a single statement: O(n)
    freq = {}
    ans, max_freq = -1, 0
    for num in filter(lambda x: x % 2 == 0, nums):  # only traversing even elements
        freq[num] = f = freq.get(num, 0) + 1
        if f > max_freq:
            ans, max_freq = num, f
        elif f == max_freq and num < ans:  # "If there is a tie, return the smallest one"
            ans = num
    # print(freq)  #debugging
    return ans
