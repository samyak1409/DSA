"""
https://leetcode.com/problems/split-with-minimum-sum
"""


def split_num(num: int) -> int:
    """"""

    # 1) Optimal (Greedy: Sort & Take Alternate): TC = O(d*log(d)); SC = O(d) {where d (digits) = log10(n)}
    # Sort the digits of num in non-decreasing order.
    # Assign digits to num1 and num2 alternatively.
    # Why?:
    # https://leetcode.com/problems/split-with-minimum-sum/solutions/3256461/python-easy-two-lines
    # https://leetcode.com/problems/split-with-minimum-sum/solutions/3256119/java-python-3-greedy-sort-then-concatenate-digits-even-and-odd-indices

    """
    nums = sorted(str(num))

    n = len(nums)

    num1 = 0
    for i in range(0, n, 2):
        num1 = num1*10 + int(nums[i])

    num2 = 0
    for i in range(1, n, 2):
        num2 = num2*10 + int(nums[i])

    return num1 + num2
    """

    # Concise:

    num = ''.join(sorted(str(num)))
    return int(num[::2]) + int(num[1::2])
