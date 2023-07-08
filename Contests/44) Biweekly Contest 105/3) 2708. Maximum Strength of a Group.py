"""
https://leetcode.com/problems/maximum-strength-of-a-group
"""


def max_strength(nums: list[int]) -> int:
    """"""

    # Try to generate all pairs of subsets and check which group provides maximal strength.

    # 0) Brute-force (Generate all subsets using Bit Manipulation): TC = O(2^n * n); SC = O(n)
    # {It's not TLE because max(n) = 13 => 2^n * n = 8192 * 13 = 106496 ~= 1e5;
    # Turns out this is the reason max(n) = 13 in the first place!}
    # Generating all subsets using "Approach 3: Lexicographic (Binary Sorted) Subsets" in
    # https://leetcode.com/problems/subsets/editorial.

    """
    from functools import reduce
    from operator import mul

    ans = float('-inf')
    # No. of subsets = 2^n (Proper = 2^n - 1):
    for i in range(1, 2**(n := len(nums))):  # O(2^n * n)
        bits = bin(i)[2:].zfill(n)  # TC = SC = O(n)
        # 0 will mean not pick, 1 will mean pick.
        ans = max(ans, reduce(mul, (nums[j] for j in range(n) if int(bits[j]))))  # TC = SC = O(n)
        # `(nums[j] for j in range(n) if int(bits[j]))`: subset
    return ans
    """

    # It can also be solved in O(NlogN) by sorting the array and using all positive integers.
    # Use negative integers only in pairs such that their product becomes positive.

    # 1) Sub-Optimal (Sort + Greedy): TC = O(n*log(n)); SC = O(n)
    # Sort and Greedily pick.
    # Intuition: It's clear that picking all the positives will always be beneficial. Next, we can also notice that
    # picking negatives in the pairs of two would make the result +ve too. Next, we just need to think of some edge
    # cases.
    # Some possible inputs (sorted so that it's easy to work):
    # [-3, -2, -1, 0, 1, 2]
    # [-1, 0, 1, 2]
    # [-1, 0]
    # [-1]
    # Algo formation after seeing the inputs:
    # First, multiply all the +ves.
    # Then, all the -ves from left to right in the pairs of two.
    # Lastly, if no multiplications done till now, return max(nums).

    # For simplicity:
    nums = sorted(nums)
    # print(nums)  #debugging

    # Init some vars:
    n = len(nums)
    ans = 1
    mul_done = False

    # Pick all the positives:
    for i in range(n-1, -1, -1):  # loop from right to left
        if (num := nums[i]) <= 0:  # stop as soon as we reach 0 or a -ve
            break
        ans *= num  # pick
        mul_done = True  # update the tracker

    # Pick all the negatives in pairs of two:
    for i in range(0, n-1, 2):  # loop from left to right; imp: `n-1` instead of `n` else we'll hit IndexError
        if (num1 := nums[i]) >= 0 or (num2 := nums[i+1]) >= 0:  # stop as soon as we reach 0 or a +ve
            break
        ans *= num1 * num2  # pick (two)
        mul_done = True  # update the tracker

    # Return ans. if multiplication was done else max(nums) which handles the edge cases ([0], [-1, 0]):
    return ans if mul_done else max(nums)

    # 2) Optimal (Greedy): TC = O(n); SC = O(1)
    # Above approach would work w/o sorting too but would stick to above only due to small Time & Space complexity
    # difference and for simpler code.
