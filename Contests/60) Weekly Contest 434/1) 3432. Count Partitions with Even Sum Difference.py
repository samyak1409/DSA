"""
https://leetcode.com/contest/weekly-contest-434/problems/count-partitions-with-even-sum-difference
"""


def count_partitions(nums: list[int]) -> int:
    """"""

    # 1) Brute-force (One by one calc sum for every partition separately): TC = O(n^2); SC = O(n)

    """
    ans = 0
    for i in range((n:=len(nums))-1):
        ans += (sum(nums[0:i+1])-sum(nums[i+1:n])) % 2 == 0
    return ans
    """

    # 1.1) TC = O(n^2); SC = O(1)

    """
    ans = 0
    for i in range((n:=len(nums))-1):
        ans += (sum(nums[j] for j in range(i+1))-sum(nums[j] for j in range(i+1, n))) % 2 == 0
    return ans
    """

    # 2) Optimal (Use two vars to store lt, rt sum, and update while traversing the arr): TC = O(n); SC = O(1)

    """
    lt, rt = 0, sum(nums)
    ans = 0
    for i in range(len(nums)-1):
        num = nums[i]
        lt += num
        rt -= num
        ans += (lt-rt) % 2 == 0
    return ans
    """

    # 3) Optimal (Maths): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/count-partitions-with-even-sum-difference/solutions/6329925/python-in-really-easy-way-check-total-is-even-or-not
    # Proof: Figure out yourself. (Easy)

    return 0 if sum(nums) % 2 else len(nums)-1
