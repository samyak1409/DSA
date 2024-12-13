"""
https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal
"""


def minimum_cost(s: str) -> int:
    """"""

    # 1) Optimal: TC = O(n); SC = O(1)

    # 1.1) Intuitive: Greedy: Moving outwards from mid to both ends, and calc. the cost:
    # Came up with this myself with following thinking process:
    # So, as we've to make the chars equal, and we can apply the op either from L2R or R2L.
    # 1) It'd be optimal to apply L2R for the first half, and R2L for the second half. That's straight-forward.
    # 2) When we'd need to change a char, all the chars before that (for first half, and similarly, chars after that for
    #    second half) would also be changed, hence, we'd apply the ops going outwards, starting from the mid.
    # 3) If the str has odd number of chars, then it'd be optimal to just change all the other chars in both the halves
    #    to that very middle char.
    #    If even:
    #             - If both the middle chars are equal, we'd change all the other chars to this char.
    #             - If odd, then we can change to any 0 or 1, so we'd just have a default char to which we'd change all
    #               the other chars.
    # Implementation thoughts:
    # 1) We don't actually need to change anything, but just add up the cost.
    # 2) And since after an op, all the following chars should change, but we're not actually changing, so to track
    #    that, we'd have two target variables for both the halves, as we'd be moving in both the sides inside a single
    #    for loop.

    """
    n = len(s)
    target_1 = target_2 = None
    ans = 0
    for i in range((n+1)//2):
        lt, rt = n//2 - i - (n % 2 == 0), n//2 + i
        # print(lt, rt)  # debugging
        if not target_1:  # or `not target_2`
            if s[lt] == s[rt]:
                target_1 = target_2 = s[lt]
                continue
            else:
                target_1 = target_2 = '0'  # a default pre-defined target
        if s[lt] != target_1:
            ans += lt + 1  # +1 coz `lt` is index
            # Now, as we've flipped all the following chars, but not actually flipping any of them, we'd instead flip
            # our target to get the same effect:
            target_1 = f'{1-int(target_1)}'
        if s[rt] != target_2:
            ans += n - rt
            # Same as above:
            target_2 = f'{1-int(target_2)}'
    return ans
    """

    # 1.2) Magic:
    # Even after reading many explanations, can't completely understand the proof that why does this work.
    # https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/solutions
    # But, most top solutions (https://leetcode.com/contest/weekly-contest-347/ranking) are this only. So, there must be
    # some strong and easy base, which I'm not aware of.

    ans = 0
    for i in range(1, n := len(s)):
        if s[i-1] != s[i]:
            ans += min(i, n-i)
    return ans
