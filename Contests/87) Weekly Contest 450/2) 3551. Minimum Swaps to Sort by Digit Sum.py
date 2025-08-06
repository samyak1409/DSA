"""
https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum
"""


def min_swaps(nums: list[int]) -> int:
    """"""

    # 1) Optimal (Sort; Greedy: Iteratively move to correct position using index mapping): TC = O(n); SC = O(n)
    # I'm not sure why everyone is using cycle detection algo:
    # https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/solutions
    # I did without it just using Greedy approach, and it's straight-forward and easy!
    # Greedy logic: If we want to minimize the swaps, if we bring the correct nums directly at current indices while
    # iterating right to left, this should be optimal since we're not doing any extra work, we're only doing the minimum
    # work of bringing the correct element at each index.

    # Track the positions so that when we need to bring correct num at current position, we know where the correct num
    # is:
    hm = {num: i for i, num in enumerate(nums)}
    # print(hm)  # debug

    # Sort as per Q.:
    s_nums = sorted(nums, key=lambda num: (sum(map(int, str(num))), num))
    # print(s_nums)  # debug

    swaps = 0
    # Iterate on the array and bring the correct elements at each index right to left:
    for i in range(len(nums)):
        # Only when curr index does not have correct num:
        if nums[i] != s_nums[i]:
            # Index where the correct num is present:
            j = hm[s_nums[i]]
            # Swap to bring the correct num here, and move the current num at that index:
            nums[i], nums[j] = nums[j], nums[i]
            # Update indices as per above swap:
            hm[nums[i]], hm[nums[j]] = i, j
            swaps += 1
    return swaps
