"""
https://leetcode.com/problems/count-special-quadruplets
"""


def count_quadruplets(nums: list[int]) -> int:
    """"""

    # Similar to https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/020.1%29%204Sum%20II.py.

    # 0) Brute-force (4 Loops): TC = O(n^4); SC = O(1)
    # N is very small, how can we use that? Can we check every possible quadruplet?

    """
    n = len(nums)
    count = 0
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                for d in range(c+1, n):
                    if nums[a]+nums[b]+nums[c] == nums[d]:
                        count += 1
    return count
    """

    # The order is important here, therefore we cannot use the two pointers approach (which requires sorting).

    # 1) Better (HashMap): TC = O(n^3); SC = O(n)
    # This o(3) version does essentially the same thing as the first solution, keeping track of a, b, and c.
    # However, by going backwards, we do not need and additional for loop to keep track of d.
    # Instead, each time we see a new number, we increment that number's count in our hashmap.
    # By going backwards, we guarantee that d comes after a, b, and c, and for each combination of a, b, and c,
    # we simply check the dictionary to see if we have already seen their sum before.
    # https://leetcode.com/problems/count-special-quadruplets/discuss/1456709/Python-99-Clean-Code-Walkthrough-From-O(4)-greater-O(3)-greater-O(2)
    # https://leetcode.com/problems/count-special-quadruplets/discuss/1452628/O(n4)-200-ms-vs.-O(n3)-16-ms

    from collections import Counter

    n = len(nums)
    hashmap = Counter()  # collections.Counter for easy working
    count = 0
    for c in range((n-1)-1, -1, -1):  # reverse traverse
        hashmap[nums[c+1]] += 1  # c+1 = d
        for b in range(c-1, -1, -1):
            for a in range(b-1, -1, -1):
                count += hashmap[nums[c]+nums[b]+nums[a]]
    return count

    # (DIDN'T UNDERSTAND):
    # 2) Optimal (HashMap): TC = O(n^2); SC = O(n^2)
    # Divide in two groups, i.e. nums[a]+nums[b]+nums[c] == nums[d] -> nums[a]+nums[b] == -nums[c]+nums[d]
    # https://leetcode.com/problems/count-special-quadruplets/discuss/1456709/Python-99-Clean-Code-Walkthrough-From-O(4)-greater-O(3)-greater-O(2)
    # https://leetcode.com/problems/count-special-quadruplets/discuss/1446988/JavaC++Python3-Real-O(n2)-solution
    # https://leetcode.com/problems/count-special-quadruplets/discuss/1451080/JavaPython-O(n2)-solution-with-explanation

    # Step-by-step algorithm building:
    # i) Can we write an algo which can find all the possible pairs of len 2?
    """
    n = len(nums)
    for a in range(n):
        for b in range(a+1, n):
            print(nums[a], nums[b])
    """
    # ii) Can we write algos which can find all the possible pairs of group 1 and group 2?
    """
    n = len(nums)
    print('G1')
    for a in range(0, n-3):  # last a can be at (n-4)-th index
        for b in range(a+1, n-2):  # last b can be at (n-3)-th index
            print(nums[a], nums[b])
    print('G2')
    for c in range(2, n-1):  # first c can be at 2nd index
        for d in range(c+1, n):  # first d can be at 3rd index
            print(nums[c], nums[d])
    """
    # iii) Can we write a merged algo (in order to make sure `a < b < c < d`) which can find all the possible pairs of
    # both groups?
    """
    pass
    """
    # iv) Can we do the same thing in reverse?
    # Why reverse? Now we have two groups so why can't we do it without reversing? 😶
    """
    pass
    """
    # v) That's it! Now just integrate hashmap in the algo to search required pair from other group in O(1) time!
    """
    pass
    """


# For debugging `2) Optimal`:
# print(), count_quadruplets([1, 2, 3, 4])
# print(), count_quadruplets([1, 2, 3, 4, 5])
# print(), count_quadruplets([1, 1, 1, 3, 5])
