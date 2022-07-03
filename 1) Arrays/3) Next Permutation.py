"""
https://leetcode.com/problems/next-permutation
"""


from typing import List


def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # 0) Correct but Redundant (I came up with this): TC = O(n^2); SC = O(n)

    """
    from bisect import insort  # for a (throughout) sorted array

    bucket = []

    for i in range(len(nums)-1):
        insort(bucket, nums[-i-1])  # insert the last number (next to curr) keeping the array sorted
        curr = nums[-i-2]  # number which is in consideration currently (for this particular iteration)
        for j, x in enumerate(bucket):
            if curr < x:  # finding the next greater element than curr
                # converting the current permutation to it's next one:
                nums[-i-2], bucket[j] = x, curr  # 1) swapping curr and next greater element
                nums[-i-1:] = bucket  # 2) filling all the elements next to curr
                return

    # if nums did not have a lexicographically larger rearrangement (is the last permutation itself)
    nums.reverse()  # in that case, first permutation is the ans. as mentioned in the Q.
    # ("While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.")
    """

    # 1) Correct and Efficient (From official solution, mine approach is doing the same thing though, but not efficiently): TC = O(n); SC = O(1)
    # https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

    for i in range(len(nums)-1):  # finding first decreasing element (iterating from right to left)
        if nums[-i-2] < nums[-i-1]:
            decreasing_element = nums[-i-2]  # decreasing element found
            for j in range(i+1):  # finding number just larger than decreasing element (iterating from right to left)
                if nums[-j-1] > decreasing_element:
                    just_larger = nums[-j-1]  # just larger number found
                    nums[-i-2], nums[-j-1] = just_larger, decreasing_element  # swapping the two
                    nums[-i-1:] = nums[-i-1:][::-1]  # reversing elements in the right
                    return

    # if nums did not have a lexicographically larger rearrangement (is the last permutation itself)
    nums.reverse()  # in that case, first permutation is the ans. as mentioned in the Q.
    # ("While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.")
