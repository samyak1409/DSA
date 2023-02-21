"""
https://leetcode.com/problems/set-mismatch
"""


def find_error_nums(nums: list[int]) -> list[int]:
    """"""

    # Tons of solutions to this one: https://leetcode.com/problems/set-mismatch/solution

    # 0) Brute-force (Sorting): TC = O(n*log(n)); SC = O(n)

    """
    n = len(nums)
    sorted_nums = sorted(nums)
    repeating = None
    for i in range(n):  # finding repeating number
        current, next_ = sorted_nums[i], sorted_nums[i+1]
        if next_ == current:  # simple
            repeating = next_
            break
    missing = 1  # starting from 1
    for i in range(n):  # finding missing number
        current = sorted_nums[i]
        if current > missing:  # if at any point, `current` exceeds `missing` => `missing` is the number which didn't
            # occur in nums
            break
        missing = current+1  # else missing = next number that should be
    return [repeating, missing]
    """

    # 1.1) Time-Optimal Brute-force (HashSet): TC = O(n); SC = O(n)

    """
    hashset = set()  # for O(1) lookup
    repeating = None
    for num in nums:  # finding repeating number
        if num in hashset:
            repeating = num
        hashset.add(num)
    missing = None
    for num in range(1, len(nums)+1):  # finding missing number
        if num not in hashset:
            missing = num
            break
    return [repeating, missing]
    """

    # 1.2) Time-Optimal Brute-force (Frequency Array): TC = O(n); SC = O(n)
    # When it's given like "contains all the numbers from 1 to n", use Array instead of HashSet for tracking
    # occurrences.
    # Benefit of using Array over HashSet? -> Less Space!

    """
    counts = [0] * len(nums)
    for num in nums:  # counting
        counts[num-1] += 1  # num-1 = index
    return [counts.index(2)+1, counts.index(0)+1]  # repeating, missing
    """

    # 1.3) Time-Optimal Brute-force (Compare Sums): TC = O(n); SC = O(n)
    # https://leetcode.com/problems/set-mismatch/discuss/105558/Oneliner-Python

    """
    sum_wo_repeating = sum(set(nums))  # sum without repeating (& without missing) num
    n = len(nums)
    return [sum(nums) - sum_wo_repeating, n*(n+1)//2 - sum_wo_repeating]  # repeating, missing
    # `sum(nums)`: sum with repeating (& without missing) num
    # `n*(n+1)//2`: sum without repeating & with missing num
    """

    # 2.1) Optimal (Negating Numbers): TC = O(n); SC = O(1)

    """
    n = len(nums)
    repeating = None
    for i in range(n):  # finding repeating number
        index = abs(nums[i])-1  # index to leave mark at; abs() because nums[i] can be a negated value
        if nums[index] < 0:  # value at `index` found negated => index+1 (nums[i]) is the repeating number!
            repeating = index+1
        else:
            nums[index] *= -1  # leaving mark
    missing = None
    for i in range(n):  # finding missing number
        if nums[i] > 0:  # positive value found, it must be because of the missing number
            missing = i+1
        else:  # turning the negated values back positive
            nums[i] *= -1
    return [repeating, missing]
    """

    # 2.2) Optimal (Maths: Sum of n & n^2 terms): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/set-mismatch/discuss/1089475/Python-O(n)-timeO(1)-space-math-solution-explained

    # In short:
    """
    n = len(nums)
    x = n*(n+1)//2 - sum(nums)
    y = ((n*(n+1)*(2*n+1)//6)-(sum(map(lambda term: term**2, nums)))) // x
    missing = (x+y) // 2
    repeating = missing - x
    return [repeating, missing]
    """

    # With Derivation:
    n = len(nums)
    # sum(nums) + missing - repeating = n*(n+1) // 2  # sum of n terms
    # => missing - repeating = n*(n+1)//2 - sum(nums)
    # Let x = missing - repeating  # ...(1)
    x = n*(n+1)//2 - sum(nums)
    # print(x)  #debugging

    # sum(map(lambda term: term**2, nums)) + missing**2 - repeating**2 = n*(n+1)*(2*n+1) // 6  # sum of n^2 terms
    # => missing**2 - repeating**2 = n*(n+1)*(2*n+1)//6 - sum(map(lambda term: term**2, nums))
    # Since a^2 - b^2 = (a+b)(a-b):
    # => (missing+repeating) * (missing-repeating) = n*(n+1)*(2*n+1)//6 - sum(map(lambda term: term**2, nums))
    # From equation (1), (missing-repeating) = x, so:
    # => (missing+repeating) * x = n*(n+1)*(2*n+1)//6 - sum(map(lambda term: term**2, nums))
    # => missing + repeating = ((n*(n+1)*(2*n+1)//6)-(sum(map(lambda term: term**2, nums)))) // x
    # Let y = missing + repeating
    y = ((n*(n+1)*(2*n+1)//6)-(sum(map(lambda term: term**2, nums)))) // x
    # print(y)  #debugging

    # x + y = (missing-repeating) + (missing+repeating)
    # => x + y = 2 * missing
    # => missing = (x+y) // 2
    missing = (x+y) // 2
    # And from equation (1), repeating = missing - x, so:
    repeating = missing - x
    return [repeating, missing]

    # 2.3) Optimal (Bit Manipulation: XOR): TC = O(n); SC = O(1)
    # If we do XOR of all the num in `nums`, with all the num in `range(1, n+1)`,
    # we would straight-away get XOR(repeating, missing).
    # But then how would we find repeating & missing? ->
    # https://leetcode.com/problems/set-mismatch/solution/#approach-7-using-xor


# Similar Questions:
# https://leetcode.com/problems/find-the-duplicate-number
