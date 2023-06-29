"""
https://leetcode.com/problems/maximum-or
"""


def maximum_or(nums: list[int], k: int) -> int:
    """"""

    # -1) [WA] Sub-Optimal (k times: Try multiplying each num (by 2) one by one to find the max):
    # TC = O(k * n * O(log2(m))); SC = O(O(log2(m))) {m = max(nums) = 10^9}
    # Input: nums = [41,79,82,27,71,62,57,67,34,8,71,2,12,93,52,91,86,81,1,79,64,43,32,94,42,91,9,25], k = 10
    # Output: 81023
    # Expected: 96383
    # It didn't look like this approach will fail, but somehow one index giving max OR val at one op, and then another
    # index giving max OR val at following op, leads to losing overall max OR val if all the ops were applied to one of
    # the index only. (Next Approach)

    """
    from math import log2, ceil
    
    # Form a freq arr to track bits freq in resulting OR vals:
    # Quiz: Why freq arr is required, can we not just track if bit is set or not?
    freq_arr = [0] * (ceil(log2(max(nums)+1)) + k)  # SC = O(log2(m) + k)
    # `ceil(log2(x+1))`: no. of digits that would be required to represent `x` in binary (alt: `len(bin(x))-2`)
    for num in nums:  # O(n * log2(m))
        for i, bit in enumerate(bin(num)[2:][::-1]):  # O(log2(m))
            freq_arr[~i] += int(bit)
    # print(freq_arr)  #debugging

    # Now, for k times:
    for _ in range(k):  # O(k * n * O(log2(m)))
        # print('k:', _)  #debugging

        max_or = 0
        max_i = -1
        # Now, try multiplying (by 2) each num one by one, in order to calc. multiplying which num by 2 gives the max
        # OR val:
        for i, num in enumerate(nums):  # O(n * O(log2(m)))
            # Update in a copied arr:
            freq_arr_copy = freq_arr[:]  # SC = O(log2(m))
            # Multiply by 2 = Left Shift Op:
            for j, bit in enumerate(bin(num)[2:][::-1]):  # O(log2(m))
                freq_arr_copy[~j] -= int(bit)
                freq_arr_copy[~(j + 1)] += int(bit)
            # print(num, freq_arr_copy)  #debugging
            # Get the OR val from freq arr:
            curr_or = int(''.join('1' if freq else '0' for freq in freq_arr_copy), base=2)  # O(log2(m))
            # Compare and update:
            if curr_or > max_or:
                max_or = curr_or
                max_i = i

        # Now, update the max to the main arr:
        # Multiply by 2 = Left shift op:
        for j, bit in enumerate(bin(nums[max_i])[2:][::-1]):  # O(log2(m))
            freq_arr[~j] -= int(bit)
            freq_arr[~(j + 1)] += int(bit)
        # Also update nums as op is performed:
        nums[max_i] *= 2
        # print(max_i, freq_arr, nums)  #debugging

    # Return ans.:
    return int(''.join('1' if freq else '0' for freq in freq_arr), base=2)  # O(log2(m))
    """

    # The optimal solution should apply all the k operations on a single number.

    # 0) [TLE] Brute-force (Apply all ops to each num one by one, calc. the OR after applying the op):
    # TC = O(n^2); SC = O(1)

    """
    from functools import reduce
    from operator import or_

    max_or = 0
    for i in range(len(nums)):  # O(n^2)
        # Perform all the ops on one num:
        nums[i] <<= k
        # Calc the OR and update max OR if required:
        max_or = max(max_or, reduce(or_, nums))  # O(n)
        # Revert the ops:
        nums[i] >>= k
    return max_or
    """

    # Calculate the prefix_or and the suffix_or and perform k operations over each element, and maximize the answer.

    # 1) Optimal (Prefix & Suffix Arr + Apply all ops to each num one by one, calc. the OR after applying the op (using
    # Prefix & Suffix Arr)): TC = O(n); SC = O(n)

    # Calc prefix & suffix arr:
    pre_or, suf_or = [0], [0]
    for i in range(n := len(nums)):  # O(n)
        pre_or.append(pre_or[-1] | nums[i]), suf_or.append(suf_or[-1] | nums[~i])
    suf_or.reverse()
    # Beautiful! Best way to build a prefix & suffix arr. Also, note how `~` did the magic.

    max_or = 0
    for i in range(n):  # O(n)
        # Calc the OR and update max OR if required:
        max_or = max(max_or, pre_or[i] | nums[i] << k | suf_or[i+1])
        # (Imp: To take care of the indices for prefix & suffix arr.)
    return max_or

    # Implementation of the solution was easy, hard part is its PROOF:
    #
    # "Q. Why this works?
    # Ans. When we multiply a number by 2 then this equal to shifting the values to the left by 1 place.
    # So to have the largest value we should shift a single number to the k number of times which end up with max value
    # possible."
    # -https://leetcode.com/problems/maximum-or/solutions/3520412/explained-very-simple-easy-to-understand-solution
    #
    # Read more:
    # https://leetcode.com/problems/maximum-or/solutions/3520489/o-1-space-keep-track-of-bits-super-simple-to-understand-and-detailed-explanation
