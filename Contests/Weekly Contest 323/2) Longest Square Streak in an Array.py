"""
https://leetcode.com/problems/longest-square-streak-in-an-array
"""


def longest_square_streak(nums: list[int]) -> int:
    """"""

    # 1) Sub-Optimal (Sort; HashMap to store (num, streak) pairs): TC = O(n*log(n)); SC = O(n)
    # I came up with this.
    # Similar to:
    # https://leetcode.com/problems/longest-square-streak-in-an-array/solutions/2899678/short-dp-c-java-lis-type

    """
    streak = {}  # num: streak
    max_streak = 0
    for num in sorted(set(nums)):  # set to remove duplicates, otherwise those will interfere
        # For every num, try to del and get the streak for sqrt(num):
        try:  # EAFP
            continued_streak = streak.pop(num**.5) + 1  # prev_streak + 1
        except KeyError:  # => sqrt(num) was not there, so begin a new seq
            streak[num] = 1
        else:  # else, update (popped the previous, now add new) the num & streak
            streak[num] = continued_streak
            max_streak = max(max_streak, continued_streak)  # and update the ans.
    # print(streak)  #debugging
    return max_streak or -1  # "called a square streak if: The length is at least 2"
    """

    # 2) Optimal (Use HashSet & Calc streak with every num): TC = O(n); SC = O(n)
    # With the constraints, the length of the longest square streak possible is 5.
    # Store the elements of nums in a set to quickly check if it exists.

    nums = set(nums)
    max_streak = 0
    for num in nums:  # O(n)
        # For every num, Calc streak:
        streak = 1
        while (num := num**2) in nums:  # O(5)
            streak += 1
        max_streak = max(max_streak, streak)  # update ans.
    return max_streak if max_streak > 1 else -1  # "called a square streak if: The length is at least 2"

    # Mind-blowing to realize how one small observation can make the Brute-force turn into Optimal Solution!
