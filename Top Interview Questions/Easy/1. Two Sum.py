"""https://leetcode.com/problems/two-sum/"""


from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:

    mapping = {}  # num: index

    for index, num in enumerate(nums):

        got = mapping.get(target-num)  # target - num = another required num

        if got is None:
            mapping[num] = index

        else:
            return [got, index]
