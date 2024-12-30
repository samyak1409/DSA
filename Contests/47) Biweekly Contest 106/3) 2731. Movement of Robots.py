"""
https://leetcode.com/problems/movement-of-robots
"""


def sum_distance(nums: list[int], s: str, d: int) -> int:
    """"""

    # 1) Optimal (Brainteaser, Sort): TC = O(n*log(n)); SC = O(n)
    # -> Very good question!
    # (Came up with myself.)
    # Observation 1:
    # "If two robots collide, they will start moving in opposite directions." is exactly same as robots passing each
    # other through. And so we don't need to worry about changing their directions etc. Turns out this was to trick us.
    # Observation 2:
    # Now, we just need "sum of distances between all the pairs of robots". If we do brute-force here, it'd be O(n^2).
    # But we can optimize it:
    # First, we need to sort the nums, so that we do not need to worry about `abs` distance, we can directly subtract
    # nums on the left from nums on the right, as nums on the right > nums on left, hence, their difference > 0.
    # Next, we see that every num occurs a fixed num of times. Observe via following example:
    # A B C D E (sorted in ascending order)
    # sum = E-D
    #     + E-C
    #     + E-B
    #     + E-A
    #
    #     + D-C
    #     + D-B
    #     + D-A
    #
    #     + C-B
    #     + C-A
    #
    #     + B-A
    # sum = 4E + 2D + 0C + (-2)B + (-4)A
    # Looks like we need to start from `len(nums)-1`, go descending order, and `-2` on each iteration.
    # (Reached to above conclusion by studying few more examples: ABCD, ABC)

    # Apply the movements:
    for i in range(n := len(nums)):  # O(n)
        nums[i] += (1 if s[i] == 'R' else -1) * d

    # Get the sum:
    ans = 0
    x = n - 1
    for num in sorted(nums, reverse=True):  # TC = O(n*log(n)); SC = O(n)
        ans = (ans + x*num) % (10**9 + 7)
        x -= 2
    return ans

    # "This is a variation of a very classic problem:
    # https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank"
    # -https://leetcode.com/problems/movement-of-robots/solutions/3622265/a-classic-problem-ants-on-a-plank-prefix-sum-o-n-log-n
