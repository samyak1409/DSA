"""
https://leetcode.com/problems/3sum-closest
"""


def three_sum_closest(nums: list[int], target: int) -> int:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/039%29%203Sum.py

    # 1) Optimal (Sorting & Two-Pointers): TC = O(n*log(n) + n^2); SC = O(n) {sorting}
    # https://en.wikipedia.org/wiki/3SUM#Quadratic_algorithm
    # https://leetcode.com/problems/3sum-closest/discuss/7872/Java-solution-with-O(n2)-for-reference

    """
    nums = sorted(nums)
    n = len(nums)
    dist, closest = float('inf'), 0  # `closest = 0` has no significance, it's going to change on the basis of dist
    for i in range(n):
        num1 = nums[i]
        lo, hi = i+1, n-1
        while lo < hi:
            num2, num3 = nums[lo], nums[hi]
            three_sum = num1 + num2 + num3
            if three_sum == target:
                return target
            elif three_sum < target:
                lo += 1
            else:  # (if three_sum > target)
                hi -= 1
            if (dist_ := abs(target-three_sum)) < dist:
                dist, closest = dist_, three_sum
    return closest
    """
    # Better (without using `dist`):
    nums = sorted(nums)
    n = len(nums)
    closest = sum(nums[:3])  # init with any three nums
    for i in range(n):
        num1 = nums[i]
        lo, hi = i+1, n-1
        while lo < hi:
            num2, num3 = nums[lo], nums[hi]
            three_sum = num1 + num2 + num3
            if three_sum == target:
                return target
            elif three_sum < target:
                lo += 1
            else:  # (if three_sum > target)
                hi -= 1
            if abs(target-three_sum) < abs(target-closest):
                closest = three_sum
    return closest
