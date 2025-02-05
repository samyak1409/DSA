"""
https://leetcode.com/problems/next-permutation
"""


def next_permutation(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # 0) [TLE] Brute-force (Generating all the permutations and then returning the "next permutation"): TC = O(n!);
    #                                                                                                   SC = O(n)
    # Not coding this approach because it's just way too inefficient to accept as an approach at the first place.

    # 1) Better (Recognize Pattern for Next Permutation, Implement the Same): TC = O(n^2); SC = O(n)
    # (I came up with this, Correct but Redundant.)

    """
    from bisect import insort  # for a (throughout) sorted array

    bucket = []
    for i in range(len(nums)-1):  # O(n^2)
        insort(bucket, nums[-i-1])  # insert the last number (next to curr) keeping the array sorted; O(n)
        # "The insort() functions are O(n) because the logarithmic search step is dominated by the linear time insertion
        # step." -https://docs.python.org/3.11/library/bisect.html#performance-notes
        curr = nums[-i-2]  # number which is in consideration currently (for this particular iteration)
        for j, x in enumerate(bucket):  # O(n)
            if curr < x:  # finding the next greater num than curr
                # converting the current permutation to it's next one:
                nums[-i-2], bucket[j] = x, curr  # 1) swapping curr and next greater num
                nums[-i-1:] = bucket  # 2) filling all the nums next to curr
                return

    # if nums did not have a lexicographically larger rearrangement (is the last permutation itself)
    nums.reverse()  # in that case, first permutation is the ans. as mentioned in the Q.
    # ("While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger
    # rearrangement.")
    """

    # 2) Optimal (First Decreasing Element): TC = O(n); SC = O(1)
    # (Mine approach is doing the same thing, but not efficiently.)
    # https://leetcode.com/problems/next-permutation/solution
    # https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

    for i in range(len(nums)-2, -1, -1):  # finding first decreasing num (iterating from right to left)
        if nums[i] < nums[i+1]:
            decreasing_num = nums[i]  # decreasing num found
            for j in range(len(nums)-1, i, -1):  # finding number just larger than decreasing num (iterating from right to left)
                if nums[j] > decreasing_num:  # since `nums[i]` was the first decreasing num, all the elements in the
                    # right are in increasing order when iterated from right to left, so first num greater would only be
                    # the "just greater" num, so no need to check through all the nums
                    just_larger = nums[j]  # just larger number found
                    nums[i], nums[j] = just_larger, decreasing_num  # swapping the two
                    nums[i+1:] = nums[i+1:][::-1]  # reversing nums in the right
                    return

    # if nums did not have a lexicographically larger rearrangement (is the last permutation itself)
    nums.reverse()  # in that case, first permutation is the ans. as mentioned in the Q.
    # ("While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger
    # rearrangement.")


# Similar Questions:
# https://leetcode.com/problems/permutations
# https://leetcode.com/problems/permutations-ii
# https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number
