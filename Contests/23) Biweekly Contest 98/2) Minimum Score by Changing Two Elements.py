"""
https://leetcode.com/problems/minimum-score-by-changing-two-elements
"""


def minimize_sum(nums: list[int]) -> int:
    """"""

    # 1) Sub-Optimal (Greedy: Sort, Choose from min and max): TC = O(n*log(n)); SC = O(n))
    # ALL HAND-WRITTEN EXPLANATION:
    # This is a good problem! (It'll look medium but is easy.)
    # So, first of all we realize that we may sort the array and the answer will remain the same.
    # (Why?
    # https://leetcode.com/problems/minimum-score-by-changing-two-elements/solutions/3202016/java-c-python-change-biggest-or-smallest/comments/1806119)
    # Now, the first thing that come in mind is this is a min-max problem, and we should apply Binary Search, but no, no
    # need, we can be greedy and don't need to check all possible pairs!
    # Simplifying the problem statement:
    # We just need to find the minimum(diff b/w the closest pair (by value) + diff b/w the farthest pair (by value)) by
    # changing at most 2 values!
    # So, let's try sorting the array and see what can we do:
    # 1 4 5 7 8
    # Realization: The farthest pair will always be = (nums[0], nums[n-1])
    # and the Closest pair will be any (nums[i], nums[i+1])
    # We have to minimize both.
    # If we change even a one num equal to it's neighbour, then we'll get the diff b/w the closest pair = 0.
    # Diff b/w the farthest pair (be x) is bounded by the min and max num.
    # If we change the nums[0] = nums[1], then x = nums[-1] - nums[1]
    # And for sure we'll get a better (possibly same) minimized answer as nums[1] >= nums[0] as the arr is sorted.
    # Wait, we can change two nums, so even better x = nums[-1] - nums[2]
    # And in the process, we can change nums[0], nums[1] to nums[2], by this, we'll get y = 0 as well!
    # So, finally, turns out we just need to return the diff b/w nums[-1] and nums[2].
    # *Penalized in the contest* Bro, it can be the other way around too!!!!
    # So return min(nums[-1]-nums[2], nums[-3]-nums[0])
    # *Penalized again* Bro, what about skipping both from left and right!!!!
    # Ans: return min(nums[-1]-nums[2], nums[-3]-nums[0], nums[-2]-nums[1])

    """
    nums = sorted(nums)  # (doesn't modify the input arr)
    return min(nums[-1]-nums[2], nums[-3]-nums[0], nums[-2]-nums[1])
    """

    # 1.1) Same idea, but can be the implemented without Sorting the whole arr, as we only want the 3 smallest & 3
    # largest nums: TC = O(n); SC = O(1)
    # https://leetcode.com/problems/minimum-score-by-changing-two-elements/solutions/3201904/explained-two-solutions-with-without-sorting-very-simple-easy-to-understand

    # Finding smallest 3 & largest 3 in linear time:
    s1 = s2 = s3 = float('inf')  # nums[0], nums[1], nums[2] (sorted nums)
    l1 = l2 = l3 = float('-inf')  # nums[-1], nums[-2], nums[-3] (sorted nums)
    # (s1, s2, s3, ..., l3, l2, l1)
    for n in nums:
        # Smallest:
        if s1 > n:
            s3, s2, s1 = s2, s1, n
        elif s2 > n:
            s3, s2 = s2, n
        elif s3 > n:
            s3 = n
        # Largest:
        if l1 < n:
            l3, l2, l1 = l2, l1, n
        elif l2 < n:
            l3, l2 = l2, n
        elif l3 < n:
            l3 = n

    # Main:
    return min(l1-s3, l3-s1, l2-s2)
