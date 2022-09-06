"""
https://leetcode.com/problems/two-sum
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """"""

    # 0) Brute-force (Nested Loop): TC = O(n^2); SC = O(1)

    """
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i]+nums[j] == target:
                return [i, j]
    """

    # Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?

    # 1.1) Better (Sorting & Binary Search): TC = O(n*log(n) + n*log(n)); SC = O(n) {sorting}

    """
    # Getting sorted array of tuples (index, num), saving index because we have to return indices as answer and after
    # sorting we'll lose original indices:
    sorted_nums = sorted(enumerate(nums), key=lambda tup: tup[1])

    # Taking every element one by one from the sorted array and applying binary search to the elements in the right:
    # (why only right? same reason as why we used `i+1` in brute force approach)
    for search_start_index, (index1, num1) in enumerate(sorted_nums, start=1):
        req_num2 = target - num1  # required_num2
        # Finding the required_num2 using Binary Search:
        lo, hi = search_start_index, len(nums)-1
        while lo <= hi:
            mid = (lo+hi) // 2  # mid index
            index2, num2 = sorted_nums[mid]
            if num2 == req_num2:
                return [index1, index2]
            elif num2 < req_num2:
                lo = mid + 1
            else:  # (if num2 > req_num2)
                hi = mid - 1
    """

    # 1.2) Better (Sorting & Two-Pointers): TC = O(n*log(n) + n); SC = O(n) {sorting}
    # "Solution 2: Sort then Two Pointers" in
    # https://leetcode.com/problems/two-sum/discuss/1378064/C++JavaPython-HashMap-Two-pointers-Solutions-Clean-and-Concise

    """
    # Getting sorted array of tuples (index, num), saving index because we have to return indices as answer and after
    # sorting we'll lose original indices:
    sorted_nums = sorted(enumerate(nums), key=lambda tup: tup[1])

    # Finding the 2 nums using Two-Pointers:
    lo, hi = 0, len(nums)-1  # init
    while lo < hi:
        (index1, num1), (index2, num2) = sorted_nums[lo], sorted_nums[hi]
        if num1+num2 == target:
            return [index1, index2]
        elif num1+num2 < target:  # => we want greater sum
            lo += 1  # considering next num (larger) in right
        else:  # (if num1+num2 > target) => we want lesser sum
            hi -= 1  # considering next num (smaller) in left
    """

    # 2) Optimal (HashMap): TC = O(n); SC = O(n) {hashmap}
    # https://leetcode.com/problems/two-sum/solution
    # https://youtu.be/dRUpbt8vHpo?t=150

    """
    # Storing all the nums in HashMap (for O(1) lookup) along with their indices (we need to return indices as answer):
    hashmap = {num: index for index, num in enumerate(nums)}
    # Taking every num one by one and checking for required_num2 in HashMap:
    for index1, num1 in enumerate(nums):
        index2 = hashmap.get(target-num1)  # target-num1 = required_num2
        if index2 not in (None, index1):  # `None` means num1 doesn't form target sum with any number; 
            # `index1` means num1 = num2
            return [index1, index2]
    """
    # It turns out we can do it in one-pass:
    # HashMap to store nums (for O(1) lookup) along with their indices (we need to return indices as answer):
    hashmap = {}  # num: index
    # Taking every num one by one and checking for required_num2 in HashMap:
    for index1, num1 in enumerate(nums):
        index2 = hashmap.get(target-num1)  # target-num1 = required_num2
        if index2 is not None:
            return [index1, index2]
        hashmap[num1] = index1  # storing after checking so that we do not need to care about index2 == index1

    # Did you notice?
    # In this question, we used all the searching techniques, viz. Linear Search, Binary Search, and Hashing in
    # `0)`, `1.1)` and `2)` respectively.


# Similar Questions:
# https://leetcode.com/problems/3sum
# https://leetcode.com/problems/4sum
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
# https://leetcode.com/problems/subarray-sum-equals-k
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst
# https://leetcode.com/problems/max-number-of-k-sum-pairs
# https://leetcode.com/problems/count-good-meals
# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k
# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target
# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array
# https://leetcode.com/problems/first-letter-to-appear-twice
# https://leetcode.com/problems/number-of-arithmetic-triplets
# https://leetcode.com/problems/node-with-highest-edge-score
