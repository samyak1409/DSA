"""
https://leetcode.com/problems/continuous-subarray-sum
"""


def check_subarray_sum(nums: list[int], k: int) -> bool:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/022%29%20Longest%20Subarray%20with%200%20Sum.py.

    # 0) [TLE] Brute-force (Nested Loop): TC = O(n^2); SC = O(1)

    """
    n = len(nums)
    for i in range(n):  # for every num in nums:
        subarray_sum = nums[i]  # subarray_sum = num1 +
        for j in range(i+1, n):
            subarray_sum += nums[j]  # one by one all the nums ahead (increasing the len of the subarray)
            # print(nums[i:j+1], subarray_sum)  #debugging
            if subarray_sum % k == 0:  # if at any point sum = multiple(k):
                return True
    """

    # 1) Optimal (Prefix Sum & HashMap): TC = O(n); SC = O(n)
    # "This is one of those magics of remainder theorem :) -> `(a+(n*x)) % x` is same as `a % x`
    # e.g. in case of the array [23,2,6,4,7] the running sum is [23,25,31,35,42] and the remainders are [5,1,1,5,0].
    # We got remainder 5 at index 0 and at index 3. That means, in between these two indexes we must have added a number
    # which is multiple of the k. Hope this clarifies your doubt :)"
    # -https://leetcode.com/problems/continuous-subarray-sum/discuss/99499/Java-O(n)-time-O(k)-space/103585

    prefix_sum = 0
    leftmost_index = {prefix_sum: -1}  # hashmap for O(1) lookup; initializing with `prefix_sum: -1` because:
    # dry run the algo with input (nums=[3,4], k=7), you'll get the answer.
    for index in range(len(nums)):
        prefix_sum += nums[index]
        remainder = prefix_sum % k
        if (leftmost := leftmost_index.get(remainder)) is not None:  # we have got same remainder before too
            # that means in b/w the two indices must lie a subarray with sum divisible by k!
            if index-leftmost > 1:  # `index-leftmost` = length of subarray whose sum = multiple(k)
                return True  # subarray of len > 1 found
        else:  # only adding not updating as we're interested in keeping the subarray as long as possible because
            # "return true if nums has a continuous subarray of size at least two"
            leftmost_index[remainder] = index
