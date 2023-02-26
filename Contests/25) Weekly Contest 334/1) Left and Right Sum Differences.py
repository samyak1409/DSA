"""
https://leetcode.com/problems/left-and-right-sum-differences
"""


def left_right_difference(nums: list[int]) -> list[int]:
    """"""

    # For each index i, maintain two variables leftSum and rightSum.
    # Iterate on the range j: [0 … i - 1] and add nums[j] to the leftSum and similarly iterate on the range j:
    # [i + 1 … nums.length - 1] and add nums[j] to the rightSum.
    # 1) Time-Optimal (Make Prefix & Suffix Arr, Return the Diff): TC = O(n); SC = O(n)

    """
    p_arr = [0]
    for num in nums[:-1]:
        p_arr.append(p_arr[-1]+num)

    s_arr = [0]
    for num in nums[::-1][:-1]:
        s_arr.append(s_arr[-1]+num)
    s_arr.reverse()

    return [abs(x-y) for x, y in zip(p_arr, s_arr)]
    """
    # Better:
    """
    n = len(nums)
    p_arr, s_arr = [0]*n, [0]*n
    for i in range(n-1):
        # p_arr[i+1], s_arr[-i-2] = p_arr[i]+nums[i], s_arr[-i-1]+nums[-i-1]  # using -ve indexing (python thing)
        p_arr[i+1], s_arr[~(i+1)] = p_arr[i]+nums[i], s_arr[~i]+nums[~i]  # using bitwise NOT (bit magic)

    return [abs(x-y) for x, y in zip(p_arr, s_arr)]
    """

    # 2) Optimal (Use Prefix & Suffix Sum Values instead of Whole Arrays): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/left-and-right-sum-differences/solutions/3231177/simple-total-sum-partial-sum-o-n-time-o-1-space

    p_sum, s_sum = 0, sum(nums)
    for num in nums:
        s_sum -= num
        yield abs(p_sum-s_sum)
        p_sum += num

    # Random:
    # "You're creating an entirely new array ans. which is of equal size to the input array nums, surely that's O(n)
    # space, not O(1)? An actual constant space solution would look something like this (Java):"
    # -https://leetcode.com/problems/left-and-right-sum-differences/solutions/3231177/simple-total-sum-partial-sum-o-n-time-o-1-space/comments/1815527
    # My Reply:
    # "Few things to remember:
    # 1) The space required for returning the ans, is not counted in the space complexity of the solution.
    # Why? Take the example of the current solution only, here's my python code with exactly the same algorithm with
    # O(1) space:
    # p_sum, s_sum = 0, sum(nums)
    # for num in nums:
    #     s_sum -= num
    #     yield abs(p_sum-s_sum)
    #     p_sum += num
    # Proves kreakEmp's algo is O(1) space.
    # 2) It's always a good practice to not modify the input array, unless we're asked to.
    # Why? Because, in real world, maybe the input array needs to be used somewhere else after it's passed into your
    # function, so, we don't want it to be changed.
    #
    # I hope it helped. 😊
    #
    # EDIT: Just saw you're way more experienced than me, I wonder why did you write that, please correct me if I'm
    # wrong instead."
    # -https://leetcode.com/problems/left-and-right-sum-differences/solutions/3231177/simple-total-sum-partial-sum-o-n-time-o-1-space/comments/1815576
