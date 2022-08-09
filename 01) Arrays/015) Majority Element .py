"""
https://leetcode.com/problems/majority-element
"""


def majority_element(nums: list[int]) -> int:
    """"""

    # 0.1) [TLE] Brute-force (Traverse and Count): TC = O(n^2); SC = O(1)
    # "element appears more than ⌊n / 2⌋ times" => count(x) > n//2, so we can simply traverse the array to find the
    # element.

    """
    n = len(nums)
    for num in nums:
        if nums.count(num) > n//2:
            return num
    """

    # 0.3) Brute-force (Sorting): TC = O(n*log(n)); SC = O(n)
    # Intuition: If an element x appears more than ⌊n / 2⌋ times (i.e. n >= count(x) > floor(n/2)),
    # then in sorted(nums), it'll be always present at position = n//2 + 1, i.e. index = n//2

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
    """
    count = {}
    n = len(nums)
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] > n//2:
            return num
    """
    # Better:
    """
    from collections import Counter
    count = Counter()
    n = len(nums)
    for num in nums:
        count[num] += 1
        if count[num] > n//2:
            return num
    """

    # 1) Better (Randomization): TC = Worst: O(inf); Average/Best: O(n); SC = O(1)
    # Probability(choosing the majority element) >= ~1/2
    # https://leetcode.com/problems/majority-element/solution/#approach-4-randomization

    """
    from random import choice

    n = len(nums)
    while True:
        rand_num = choice(seq=nums)  # choose a random element from the array
        if nums.count(rand_num) > n//2:  # check if the chosen element is the majority element or not
            return rand_num
    """

    # 2) Optimal (Boyer-Moore Majority Voting Algorithm 💘): TC = O(n); SC = O(1)
    # https://www.cs.utexas.edu/~moore/best-ideas/mjrty
    # https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
    # Intuition: If we had some way of counting instances of the majority element as +1 and instances of any other
    # element as −1, summing them would make it obvious that the majority element is indeed the majority element.

    # `016) Majority Element II.py` Style:
    """
    major, relative_votes = None, 0  # init
    for num in nums:  # traverse
        if num == major:
            relative_votes += 1
        elif relative_votes == 0:  # change major
            major, relative_votes = num, 1
        else:  # (num != major and relative_votes >= 1)
            relative_votes -= 1
    return major  # ans.
    """
    # Easier for current one:
    """
    major, relative_votes = None, 0  # init
    for num in nums:  # traverse
        if relative_votes == 0:  # change major
            major, relative_votes = num, 1
        else:  # current major's relative votes ++ or --
            relative_votes += 1 if (num == major) else -1
    return major  # ans.
    """
    # Or:
    major, relative_votes = None, 0  # init
    for num in nums:  # traverse
        if relative_votes == 0:  # change major
            major = num
        relative_votes += 1 if (num == major) else -1  # current major's relative votes ++ or --
    return major  # ans.
