"""
https://leetcode.com/problems/4sum
"""


def four_sum(nums: list[int], target: int) -> list[list[int]]:
    """"""

    # We can implement 4Sum by wrapping 3Sum in another loop.
    # But wait - there is a catch.
    # If an interviewer asks you to solve 4Sum, they can follow up with 5Sum, 6Sum, and so on.
    # What they are really expecting at this point is a k_sum solution.
    # Therefore, we will focus on a generalized implementation here.
    # https://leetcode.com/problems/4sum/solution
    # It's Easy! First of all try to convert the iterative brute-force algorithm to recursive.
    # Then generalize it (i.e. add a parameter k).
    # Lastly, add the Two-Pointers approach to find the last two numbers!

    # 0) [TLE] Brute-force (Sort & Nested Loops): TC = O(n*log(n) + n^4); SC = O(n) {sorting}

    # Read how we reached to the following algorithm from `039 3Sum.py`'s `0) Brute-force`
    # (https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/039%29%203Sum.py).
    nums = sorted(nums)  # (not modifying the input array but making a new variable (local))
    n = len(nums)
    for a in range(n):
        if a == 0 or nums[a] != nums[a-1]:  # proceed if not checked already for nums[a]
            for b in range(a+1, n):
                if b == a+1 or nums[b] != nums[b-1]:  # proceed if not checked already for nums[b]
                    for c in range(b+1, n):
                        if c == b+1 or nums[c] != nums[c-1]:  # proceed if not checked already for nums[c]
                            for d in range(c+1, n):
                                if d == c+1 or nums[d] != nums[d-1]:  # proceed if not checked already for nums[d]
                                    if nums[a]+nums[b]+nums[c]+nums[d] == target:
                                        yield [nums[a], nums[b], nums[c], nums[d]]


# Similar Questions:
# https://leetcode.com/problems/two-sum
# https://leetcode.com/problems/3sum
# https://leetcode.com/problems/4sum-ii
# https://leetcode.com/problems/count-special-quadruplets
