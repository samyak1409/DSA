"""
https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum
"""


def min_sum_of_lengths(arr: list[int], target: int) -> int:
    """"""

    # 1) Optimal (Prefix Sum & HashMap): TC = O(n); SC = O(n)

    # 1.1) [WA] Implementation 1:
    # Run on the following test case to know why:
    # Input: [2,2,4,4,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 20
    # Output: 25
    # Expected: 23

    """
    # Helper Function:
    def get_min_subarray(nums: list[int], k: int) -> tuple[int, int, int]:
        prefix_sum = 0
        last_index = {prefix_sum: -1}  # for O(1) lookup
        min_len, i, j = float('inf'), None, None
        for index in range(len(nums)):
            prefix_sum += nums[index]
            if (last := last_index.get(prefix_sum-k)) is not None:  # => this prefix_sum has occurred before
                if (sub_arr_len := index-last) < min_len:  # `index-last` = length of subarray with required sum
                    min_len, i, j = sub_arr_len, last+1, index  # saving the [i, j] of the sub-array
            last_index[prefix_sum] = index  # add/update `prefix_sum: index`
        return min_len, i, j

    # Step 1) Find len of smallest sub-array with required sum using Prefix Sum Algo:
    #         Also, save start and end index of the subarray.
    min_len1, start, end = get_min_subarray(nums=arr, k=target)
    if min_len1 == float('inf'):  # no subarrays with required sum exist
        return -1

    # Step 2) Partition the input array into two arrays and find len of smallest sub-array again:
    min_len2 = min(get_min_subarray(nums=arr[:start], k=target)[0], get_min_subarray(nums=arr[end+1:], k=target)[0])
    if min_len2 == float('inf'):  # only 1 subarray with required sum exists
        return -1

    return min_len1 + min_len2
    """

    # 1.2) Implementation 2:
    # https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/discuss/685470/Python-One-pass-prefix-sum-O(n)

    pass

    # Though:
    # "I see, mot of the people confused this with 560. Subarray Sum Equals K off course that would give correct answer,
    # no doubt about that. But I think we can leverage the constraint here, which says a[i] >= 1 due to this constraint
    # we don't need a HashMap here. Problem can be solved by vanilla sliding window."
    # https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/discuss/686105/JAVA-or-Sliding-window-with-only-one-array-or-No-HasMap
