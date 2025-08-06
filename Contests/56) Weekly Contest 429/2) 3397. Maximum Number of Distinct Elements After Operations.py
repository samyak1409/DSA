"""
https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations
"""


def max_distinct_elements(nums: list[int], k: int) -> int:
    """"""

    # 1) Optimal (Greedy: Sort, Sweep the numbers to as left as possible): TC = O(n*log(n)); SC = O(n) {sort}
    # [Came up by myself]
    # Not hard.

    # First, sort the numbers:
    nums.sort()

    # We'd have a goal num, which is the num we want the current num to change to, in order to optimally apply the ops,
    # initializing with sweeping the first num to the max left:
    goal = nums[0] - k
    ans = 0
    # Iterate:
    for num in nums:
        # Now, we'd have three cases:
        # 1. goal < num: e.g. num = 1, k = 2, goal = -1 {see example test case 1}
        # 2. goal == num: e.g. num = 3, k = 2, goal = 3 {see example test case 1}
        # 3. goal > num: e.g. num = 4, k = 1, goal = 5 {see example test case 2}
        if (goal < num) or (goal == num) or (goal > num and goal-num <= k):
            # When goal < num, we need to handle one more thing, suppose num = 12, k = 2, goal = 8:
            if goal < num and num-goal > k:
                goal = num - k
            # * We don't actually need to change the num, but if we had to, it'd be done here. *
            # ++ the goal as we want to keep the numbers unique:
            goal += 1
            ans += 1
    return ans

    # 1.2) Another good implementation:
    # https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/solutions/6172740/c-java-greedy-approach
