"""
https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum
"""


def min_sum_of_lengths(arr: list[int], target: int) -> int:
    """"""

    # Advanced version of:
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/022%29%20Longest%20Subarray%20with%200%20Sum.py

    # -1) [WA] Optimal (Prefix Sum + HashMap): TC = O(n); SC = O(n)
    # Find first array, then find second array in the 2 arrays got by removing the first array from the main array.

    """
    # Helper Function:
    def get_min_subarray(m: int = 0, n: int = len(arr), k: int = target) -> tuple[int, int, int]:
        prefix_sum = 0
        last_index = {prefix_sum: -1}  # for O(1) lookup
        min_len, i, j = float('inf'), None, None
        for index in range(m, n):
            prefix_sum += arr[index]
            if (last := last_index.get(prefix_sum-k)) is not None:  # => this prefix_sum has occurred before
                if (sub_arr_len := index-last) < min_len:  # `index-last` = length of subarray with required sum
                    min_len, i, j = sub_arr_len, last+1, index  # saving the [i, j] of the sub-array
            last_index[prefix_sum] = index  # add/update `prefix_sum: index`
        return min_len, i, j

    # Step 1) Find len of smallest sub-array with required sum using Prefix Sum Algo:
    #         Also, save start and end index of the subarray.
    min_len1, start, end = get_min_subarray()
    if min_len1 == float('inf'):  # no subarrays with required sum exist
        return -1

    # Step 2) Partition the input array into two arrays and find len of smallest sub-array again:
    min_len2 = min(get_min_subarray(n=start)[0], get_min_subarray(m=end+1)[0])
    if min_len2 == float('inf'):  # only 1 subarray with required sum exists
        return -1

    return min_len1 + min_len2
    """

    # Why is it wrong? Because it may be possible that while choosing the first minimum array, we destroy the chance
    # of getting two (let's say) minimum+1 len of arrays that indeed would have been the optimal answer.
    # Understood? If not, think about it.

    # 1) Optimal (Find all the sub-arrays with sum target, choose optimal ans. from them): TC = O(n); SC = O(n)
    # Let's create two arrays prefix and suffix where prefix[i] is the minimum length of sub-array ends before i and has
    # sum = k, suffix[i] is the minimum length of sub-array starting at or after i and has sum = k.
    # The answer we are searching for is min(prefix[i] + suffix[i]) for all values of i from 0 to n-1 where
    # n == arr.length.
    # If you are still stuck with how to build prefix and suffix, you can store for each index i the length of the
    # sub-array starts at i and has sum = k or infinity otherwise, and you can use it to build both prefix and suffix.

    # 0.1) Using Prefix Sum + HashMap:
    # Finding all the subarrays and Creating Prefix Array and Saving Data for Suffix Array:
    """
    n = len(arr)
    ps = 0
    hm = {0: -1}
    prefix = [float('inf')] * (n+1)  # init
    lengths = [float('inf')] * n  # for suffix array
    for j, x in enumerate(arr):
        ps += x
        if (i := hm.get(ps-target)) is not None:
            i += 1  # start index of subarray with target sum
            # print(i, j)  #debugging
            prefix[j+1] = min(prefix[j], (len_ := j-i+1))  # prefix[i] is the min subarray ends before i and has sum = k
            lengths[i] = len_  # store for each index i the length of the subarray starts at i and has sum = k or
            # infinity otherwise, and you can use it to build suffix
        else:
            prefix[j+1] = prefix[j]  # same as previous
        hm[ps] = j  # add or update
    # print(prefix, lengths)  #debugging
    # Creating Suffix Array:
    suffix = [float('inf')] * (n+1)  # init
    for i in range(-1, -n-1, -1):  # reverse traverse
        suffix[i-1] = min(suffix[i], lengths[i])  # suffix[i] is the min subarray starting at or after i and has sum = k
    # print(suffix)  #debugging
    # Finding `min(prefix[i] + suffix[i])`:
    ans = float('inf')
    for i in range(n):
        ans = min(ans, prefix[i]+suffix[i])
    return ans if ans != float('inf') else -1
    """
    # 0.2) Using Sliding Window:
    # As the input doesn't contain negative numbers, we don't necessarily need HashMap, Sliding Window will also work!
    # Benefit? -> Constant Space!
    # But as we need to use Prefix and Suffix Arrays anyway, the final SC of this solution will be O(n) only.
    i, j = 0, -1
    n = len(arr)
    curr = 0
    prefix = [float('inf')] * (n+1)  # init
    lengths = [float('inf')] * n  # for suffix array
    while i != n:
        if curr < target:
            prefix[j+1] = prefix[j]  # same as previous
            j += 1
            try:
                curr += arr[j]
            except IndexError:  # j == n
                break
        elif curr == target:
            # print(i, j)  #debugging
            prefix[j+1] = min(prefix[j], (len_ := j-i+1))  # prefix[i] is the min subarray ends before i and has sum = k
            lengths[i] = len_  # store for each index i the length of the subarray starts at i and has sum = k or
            # infinity otherwise, and you can use it to build suffix
            j += 1
            try:
                curr += arr[j]-arr[i]
            except IndexError:  # j == n
                break
            i += 1
        else:  # (if curr > target)
            curr -= arr[i]
            i += 1
    # print(prefix, lengths)  #debugging
    # Creating Suffix Array:
    suffix = [float('inf')] * (n+1)  # init
    for i in range(-1, -n-1, -1):  # reverse traverse
        suffix[i-1] = min(suffix[i], lengths[i])  # suffix[i] is the min subarray starting at or after i and has sum = k
    # print(suffix)  #debugging
    # Finding `min(prefix[i] + suffix[i])`:
    ans = float('inf')
    for i in range(n):
        ans = min(ans, prefix[i]+suffix[i])
    return ans if ans != float('inf') else -1

    # See: https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/solutions
