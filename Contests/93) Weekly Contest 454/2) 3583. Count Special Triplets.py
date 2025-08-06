"""
https://leetcode.com/problems/count-special-triplets
"""


def special_triplets(nums: list[int]) -> int:
    """"""

    # 1) Optimal (HashMap: Counting, Loop, Math): TC = O(n); SC = O(n)
    # Intuition:
    # If we fix a `nums[j]`, then we just need to find the number of `nums[i] * 2` and `nums[k] * 2`.
    # We can use hashmap to do that fast.
    # We can loop on nums and take every num one by one as `nums[j]`, and calc the num of triplets for each `nums[j]`.

    from collections import Counter

    lt, rt = Counter(), Counter(nums)
    cnt = 0

    for num in nums:
        rt[num] -= 1
        cnt += lt[num*2] * rt[num*2]
        cnt %= 10**9 + 7  # (doing mod on intermediate step so that `cnt` never goes big and slow down the algo)
        lt[num] += 1

    return cnt

    # This is a two-pass solution, for one-pass, see:
    # https://leetcode.com/problems/count-special-triplets/solutions/6844768/java-c-python-two-passes-ans-one-pass
