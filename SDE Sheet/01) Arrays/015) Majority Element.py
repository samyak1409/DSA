"""
https://leetcode.com/problems/majority-element
"""


def majority_element(nums: list[int]) -> int:
    """"""

    # 0.1) [TLE] Brute-force (Count occurrence of each element one by one): TC = O(n^2); SC = O(1)
    # "element appears more than ⌊n / 2⌋ times" => count(x) > n//2

    """
    n = len(nums)
    for num in nums:  # O(n)
        if nums.count(num) > n//2:  # O(n)
            return num
    """

    # 0.3) Brute-force (Sorting): TC = O(n*log(n)); SC = O(n)
    # Intuition: If an element x appears more than ⌊n / 2⌋ times (i.e. n >= count(x) > floor(n/2)),
    # then in sorted(nums), it'll be always present at position = n//2 + 1, i.e. index = n//2.

    """
    return sorted(nums)[len(nums)//2]
    """

    # 0.2) Time-optimal (HashMap): TC = O(n); SC = O(n)
    # Optimization of `0.1)` with the help of HashMap.

    """
    from collections import Counter

    count = Counter(nums)  # O(n)
    # return max(count.keys(), key=lambda num: count[num])  # O(n)
    # return max(count.keys(), key=count.get)  # O(n)
    return count.most_common(n=1)[0][0]
    """
    # Better: Don't build the complete histogram, stop as soon as the ans is found:
    """
    count = {}
    n = len(nums)
    for num in nums:  # O(n)
        count[num] = count.get(num, 0) + 1
        if count[num] > n//2:  # O(1)
            return num
    """
    # Better: Use `Counter` for an added bit of simplicity:
    """
    from collections import Counter

    count = Counter()
    n = len(nums)
    for num in nums:  # O(n)
        count[num] += 1
        if count[num] > n//2:  # O(1)
            return num
    """

    # 1) Better (Randomization): TC = Worst: O(inf); Average: O(2n) = O(n); SC = O(1)
    # Probability(choosing the majority element) >= ~1/2
    # https://leetcode.com/problems/majority-element/editorial/#approach-4-randomization
    # https://leetcode.com/problems/majority-element/solutions/51612/c-6-solutions/#:~:text=Randomization

    """
    from random import choice

    n = len(nums)
    while True:  # TC Range = [O(1), O(inf)]
        rand_num = choice(seq=nums)  # choose a random element from the array; O(1)
        if nums.count(rand_num) > n//2:  # check if the chosen element is the majority element or not; O(n)
            return rand_num
    """

    # Follow-up: Could you solve the problem in linear time and in O(1) space?

    # 2) Optimal (Boyer-Moore Majority Voting Algorithm <3): TC = O(n); SC = O(1)
    # https://www.cs.utexas.edu/~moore/best-ideas/mjrty
    # https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
    # Intuition: If we had some way of counting instances of the majority element as +1 and instances of any other
    # element as −1, summing them would make it obvious that the majority element is indeed the majority element.

    # Intuitive:
    """
    # At starting, `major` doesn't exist, and `relative_votes` is set to 1 instead of 0 so that first element is
    # assigned correctly in the algo (dry run to understand).
    major, relative_votes = None, 1

    # Traverse nums:
    for num in nums:
        # If major element is repeated, ++vote:
        if num == major:
            relative_votes += 1
        # Else:
        else:
            # --vote:
            relative_votes -= 1
            # And if votes become 0, means we need to replace the major:
            if relative_votes == 0:
                major = num
                relative_votes = 1

    return major
    """

    # Original implementation (as per
    # https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm#Description:~:text=pseudocode):
    """
    major, relative_votes = None, 0  # init
    
    for num in nums:  # traverse
        if relative_votes == 0:  # change major
            major, relative_votes = num, 1
        else:  # current major's relative votes ++ or --
            relative_votes += 1 if (num == major) else -1
    
    return major  # ans.
    """

    # Shortened of above:
    major, relative_votes = None, 0  # init

    for num in nums:  # traverse
        if relative_votes == 0:  # change major
            major = num
        relative_votes += 1 if (num == major) else -1  # current major's relative votes ++ or --

    return major  # ans.


# `016 Majority Element II.py` Style:
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


# Similar Questions:
# https://leetcode.com/problems/majority-element-ii
# https://leetcode.com/problems/most-frequent-even-element
