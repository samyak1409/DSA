"""
https://leetcode.com/problems/count-the-number-of-fair-pairs
"""


def count_fair_pairs(nums: list[int], lower: int, upper: int) -> int:
    """"""

    # 0) [TLE] Brute-force (HashMap: Check, then Update): TC = O(n * k) {max(n) == 1e5, max(k) == 2e9}; SC = O(n)
    # Used in the standard question (Two Sum) where lower == upper. But not feasible here.

    """
    from collections import Counter
    
    freq = Counter()  # `Counter` to count easily
    count = 0
    
    for num in nums:  # O(n * k)
        
        for sum_ in range(lower, upper+1):  # O(k)
            count += freq[sum_-num]  # check pair
        
        freq[num] += 1  # then update
    
    return count
    """

    # Sort the array in ascending order.
    # For each number in the array, keep track of the smallest and largest numbers in the array that can form a fair
    # pair with this number.
    # As you move to larger number, both boundaries move down.

    # 1) Optimal (Two Pointers): TC = O(n*log(n)); SC = O(n)
    # First realization: We can sort the array, result will remain the same! Can we take some advantage of array being
    # sorted?
    # We can use two pointers which will point on the smallest & largest numbers that can form a "fair pair" with the
    # current number!

    # 1.0) [WA] Dry run with (nums=[-1, -1, 0, 0], lower=1, upper=1) to know why.
    """
    count = 0

    nums = sorted(nums)  # O(n*log(n))

    largest = smallest = len(nums)-1  # (these are indices); init
    # You might have a doubt that why are we starting `smallest` from the end too, read following to know.

    for i, num in enumerate(nums):  # O(n)

        # Move `largest` to the largest possible number which can form a "fast pair" with current `num`:
        while largest >= 0 and num+nums[largest] > upper:
            largest -= 1
        
        # Move `smallest` to the smallest possible number which can form a "fast pair" with current `num`:
        while smallest-1 >= 0 and num+nums[smallest-1] >= lower:
            smallest -= 1

        count += largest-smallest+1 - (smallest <= i <= largest)
        # `largest-smallest+1`: no. of "fast pairs" which can form with `num`
        # `- (smallest <= i <= largest)`: subtract 1 if a pair formed was with itself

    return count // 2  # `// 2` because every num was considered 2 times (while main iterating & and while pair finding)
    """

    # 1.1) Fix: Point `smallest` to the number before the smallest possible number:
    count = 0

    nums = sorted(nums)  # O(n*log(n))

    largest = smallest = len(nums)-1  # (these are indices); init
    # You might have a doubt that why are we starting `smallest` from the end too, read following to know.

    for i, num in enumerate(nums):  # O(n)

        # Move `largest` to the largest possible number which can form a "fast pair" with current `num`:
        while largest >= 0 and num+nums[largest] > upper:
            largest -= 1

        # Move `smallest` to the number before the smallest possible number which can form a "fast pair" with current
        # `num`:
        while smallest >= 0 and num+nums[smallest] >= lower:
            smallest -= 1

        count += largest-smallest - (smallest < i <= largest)
        # `largest-smallest`: no. of "fast pairs" which can form with `num`
        # `- (smallest < i <= largest)`: subtract 1 if a pair formed was with itself

    return count // 2  # `// 2` because every num was considered 2 times (while main iterating & and while pair finding)

    # Another good way to solve these (related to range) kind of problems:
    # 2) Optimal (Return pair_count(sum_lt_eq=upper) - pair_count(sum_lt_eq=lower-1)): TC = O(n*log(n)); SC = O(n)
    # https://leetcode.com/problems/count-the-number-of-fair-pairs/solutions/3174181/two-pointers-2
