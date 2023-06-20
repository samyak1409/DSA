"""
https://leetcode.com/problems/count-special-quadruplets
"""


def count_quadruplets(nums: list[int]) -> int:
    """"""

    # Similar to https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/020.1%29%204Sum%20II.py.

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

    # 1) Better (3 Loops & HashMap): TC = O(n^3); SC = O(n)
    # This o(3) version does essentially the same thing as the first solution, keeping track of a, b, and c.
    # However, by going backwards, we do not need and additional for loop to keep track of d.
    # Instead, each time we see a new number, we increment that number's count in our hashmap.
    # By going backwards, we guarantee that d comes after a, b, and c, and for each combination of a, b, and c,
    # we simply check the dictionary to see if we have already seen their sum before.
    # https://leetcode.com/problems/count-special-quadruplets/solutions/1446756/c-two-simple-short-explained-solutions-brute-force-improved-version
    # https://leetcode.com/problems/count-special-quadruplets/solutions/1456709/python-99-clean-code-walkthrough-from-o-4-o-3-o-2
    # https://leetcode.com/problems/count-special-quadruplets/solutions/1452628/o-n4-200-ms-vs-o-n3-16-ms

    """
    from collections import Counter

    n = len(nums)
    hashmap = Counter()  # collections.Counter for easy working
    count = 0
    for c in range((n-1)-1, -1, -1):  # reverse traverse
        d = c + 1
        hashmap[nums[d]] += 1  # hash nums[d]
        for b in range(c-1, -1, -1):
            for a in range(b-1, -1, -1):
                count += hashmap[nums[c]+nums[b]+nums[a]]  # search nums[a]+nums[b]+nums[c]
    return count
    """

    # 2) Optimal (2 Loops & HashMap): TC = O(n^2); SC = O(n^2)
    # Divide in two groups, i.e. nums[a]+nums[b]+nums[c] == nums[d] -> nums[a]+nums[b] == -nums[c]+nums[d]
    # See this visualization for easy understanding:
    # https://raw.githubusercontent.com/wf9a5m75/leetcode/f45e9b9c9fffd7956641b62b5777bcb2e76fe20c/count-special-quadruplets/whiteboard.jpg
    # https://leetcode.com/problems/count-special-quadruplets/solutions/1446988/java-c-python3-real-o-n-2-solution
    # https://leetcode.com/problems/count-special-quadruplets/solutions/1456709/python-99-clean-code-walkthrough-from-o-4-o-3-o-2

    from collections import Counter

    n = len(nums)
    hashmap = Counter()  # collections.Counter for easy working
    count = 0
    for c in range(n-2, 1, -1):  # reverse traverse
        for d in range(n-1, c, -1):
            hashmap[nums[d]-nums[c]] += 1  # hash -nums[c]+nums[d]
        b = c - 1
        for a in range(b-1, -1, -1):
            count += hashmap[nums[b]+nums[a]]  # search nums[a]+nums[b]
    return count
