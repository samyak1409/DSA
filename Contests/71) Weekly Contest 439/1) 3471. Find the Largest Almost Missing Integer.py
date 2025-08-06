"""
https://leetcode.com/problems/find-the-largest-almost-missing-integer
"""


def largest_integer(nums: list[int], k: int) -> int:
    """"""

    # 0.1) Brute-force (Simulate: HashSet, Loop): TC = O(n*(n-k)*k); SC = O(n+k)
    # Algo: One by one check for each num, if it "appears in exactly one subarray of size `k` within `nums`".

    """
    ans = -1
    for num in set(nums):  # TC = SC = O(n) {when worst case `nums` have all uniques}
        if sum(num in nums[i:i+k] for i in range(len(nums)-k+1)) == 1:  # TC = O((n-k)*k); SC = O(k)
            ans = max(ans, num)
    return ans
    """

    # 0.2) Brute-force (Loop, HashSet): TC = O((n-k)*(n-k)*k); SC = O(k)
    # Algo: One by one for each subarray of len `k`, subtract (remove) the nums from all the other sub-arrays.

    """
    ans = -1
    for i in range((n:=len(nums))-k+1):  # TC = O(n-k)
        hs = set(nums[i:i+k])  # TC = SC = O(k)
        for j in range(n-k+1):  # TC = O(n-k)
            if i != j:
                hs -= set(nums[j:j+k])  # TC = SC = O(k)
        if hs:
            ans = max(ans, max(hs))  # TC = O(k)
    return ans
    """

    # 1) Sub-optimal (HashMap, Loop): TC = O(); SC = O()
    # What we're doing here better than previous algos is we're not going through all the sub-arrays for all the nums
    # (`0.1`) or all the sub-arrays (`0.2`), but only once, and storing the data in a hashmap.
    # Algo: Loop on all the sub-arrays, and ++`freq[num]` everytime a num appears. That way if a num is present in only
    # one sub-array, it'd be 1, but if a num is there in two sub-arrays, then it'd be counted 2. Clever.
    # https://leetcode.com/problems/find-the-largest-almost-missing-integer/solutions/6485946/hash-table-python-c-java-js-c

    """
    from collections import Counter

    freq = Counter()  # SC = O(n)
    # Looping on all the sub-arrays one by one, so that if a num is there in multiple sub-arrays, it'd be counted
    # multiple times:
    for i in range(len(nums)-k+1):  # TC = O(n-k)
        for num in set(nums[i:i+k]):  # TC = SC = O(k)
            freq[num] += 1

    ans = -1
    # Then, just return the max num with freq = 1:
    for num, cnt in freq.items():  # TC = O(n)
        if cnt == 1:
            ans = max(ans, num)
    return ans
    """

    # 2) Optimal (HashMap, Loop): TC = O(n); SC = O(n)
    # Optimal complexity (O(n)) only possible by dividing & solving the problem separately for three different cases.
    # Hints:
    # 1. Solve the problem for three different cases: k = 1, k = n, and 1 < k < n.
    # 2. If k = 1, return the largest element that occurs exactly once in nums.
    # 3. If k = n, return the largest element in nums.
    # 4. If 1 < k < n, all elements different from nums[0] and nums[n-1] will occur in more than one subarray of size k.
    # Hence, the answer is the largest of nums[0] and nums[n-1] if they both occur exactly once in the array.
    # If one of them occurs more than once, return the other. If both of them occur more than once, return -1.

    from collections import Counter

    if k == 1:  # TC = SC = O(n)
        # Since k == 1, we don't need approach `1)` pre-process part, basically that part just boils down to:
        # Return max num with freq = 1:
        return max((num for num, cnt in Counter(nums).items() if cnt == 1), default=-1)
    if k == len(nums):  # TC = O(n)
        # Return max num:
        return max(nums)
    else:  # (if 1 < k < n); TC = SC = O(n)
        # Other than `nums[0], nums[1]`, all the `nums[i]` would surely have freq across all sub-arrays > 1 if `k > 1`
        # and `k != n`. Only possible candidates: `nums[0], nums[1]`:
        freq = Counter(nums)
        return max((num for num in (nums[0], nums[-1]) if freq[num] == 1), default=-1)
