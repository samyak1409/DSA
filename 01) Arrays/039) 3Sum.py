"""
https://leetcode.com/problems/3sum
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    """"""

    # 0) [TLE] Brute-force (Nested Loops & HashMap): TC = O(n^3); SC = O(n)

    # Core Logic: TC = O(n^3); SC = O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    yield [nums[i], nums[j], nums[k]]
    """
    # But as the solution set must not contain duplicate triplets, see Example 1:
    #     Input: nums = [-1, 0, 1, 2, -1, -4]
    #     Output: [[-1, 0, 1], [-1, -1, 2]]
    #     Explanation:
    #     nums[0] + nums[1] + nums[2] = (-1) + 0 +   1  = 0.
    #     nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    #     nums[1] + nums[2] + nums[4] =   0  + 1 + (-1) = 0.
    #     THE DISTINCT TRIPLETS ARE [-1, 0, 1] AND [-1, -1, 2].
    #     Notice that the order of the output and the order of the triplets does not matter.
    # We will keep track of the triplets already added to the answer set and will not consider any triplet again:
    # TC = O(n^3 * 3*log(3)); SC = O(n)
    """
    # from collections import Counter

    n = len(nums)
    triplet_set = set()  # for checking triplet's presence in O(1) time
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = [nums[i], nums[j], nums[k]]
                    # For checking triplet's presence in O(1) time IRRESPECTIVE OF THE ORDER OF THE NUMS IN TRIPLETS:
                    '''
                    triplet_counter = Counter(triplet)  # tracking triplet's nums and their counts
                    # can't use set because it will destroy the triplet itself, consider triplet = [-1, 2, -1]
                    # set(triplet) = {-1, 2} ❌ whereas Counter(triplet) = {-1: 2, 2: 1} ✔
                    if triplet_counter not in triplet_set:  # raise TypeError: unhashable type: Counter
                        # because MUTABLE DATATYPES ARE UNHASHABLE
                        yield triplet
                        triplet_set.add(triplet_counter)
                    '''
                    # It's the problem, instead, we can sort the triplet (time will be O(1) only because len(triplet) is
                    # 3), and since the triplets will be ordered now, we can use tuples (i.e. ordered and immutable):
                    sorted_triplet_tuple = tuple(sorted(triplet))
                    if sorted_triplet_tuple not in triplet_set:
                        yield triplet
                        triplet_set.add(sorted_triplet_tuple)
    """
    # Turns out that we can also just sort the input array and apply the above logic (without needing to sort the
    # triplets): TC = O(n*log(n) + n^3); SC = O(n+n)
    # "Brute Force Solution" in
    # https://leetcode.com/problems/3sum/discuss/1363302/C++-or-Brute-Force-or-Optimal(Two-Pointer-Method)-or-Commented-or-Time-O(N2)-or-Auxiliary-Space-O(1)
    """
    nums = sorted(nums)  # (not modifying the input array but making a new variable (local))
    n = len(nums)
    triplet_set = set()  # for checking triplet's presence in O(1) time
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = [nums[i], nums[j], nums[k]]
                    triplet_tuple = tuple(triplet)
                    if triplet_tuple not in triplet_set:
                        yield triplet
                        triplet_set.add(triplet_tuple)
    """
    # Why does this work?
    # Because if the input array is sorted, triplets will not form like [-1, 0, 1] & [0, 1, -1],
    # but like [-1, 0, 1] & [-1, 0, 1], i.e. by default sorted (i.e. in order)
    # Since this sorting beforehand technique is more efficient than the previous one, will use this only in next
    # approaches.

    # NOTE:
    # 3Sum -> num1 + num2 + num3 = 0
    #         => num2 + num3 = -num1
    #         Let -num1 = target
    #         => num2 + num3 = target -> Two Sum

    # 1) [TLE] Better (Sorting + Binary Search): TC = O(n*log(n) + (n^2)*log(n)); SC = O(n+n)

    """
    nums = sorted(nums)  # (not modifying the input array but making a new variable (local))

    n = len(nums)
    triplet_set = set()  # for checking triplet's presence in O(1) time
    for i in range(n):
        num1 = nums[i]
        for j in range(i+1, n):
            num2 = nums[j]
            required_num3 = -num1 + -num2  # target
            # Now, finding num3 using Binary Search:
            # https://github.com/samyak1409/DSA/blob/7cbe5e00f474eb6a0aee5e0b58d66296a59604c3/01%29%20Arrays/019%29%20Two%20Sum.py#L19
            low, high = j+1, n-1
            while low <= high:
                mid = (low+high) // 2
                num3 = nums[mid]
                if num3 == required_num3:  # => triplet found
                    triplet = [num1, num2, num3]
                    triplet_tuple = tuple(triplet)
                    if triplet_tuple not in triplet_set:
                        yield triplet
                        triplet_set.add(triplet_tuple)
                    break  # imp to break out once we get our num3 otherwise it will be an inf loop
                elif num3 < required_num3:
                    high = mid - 1
                else:  # (if num3 > required_num3)
                    low = mid + 1
    """

    # 2.1) Optimal (HashMap): TC = O(n*log(n) + n^2); SC = O(n+n+n)

    """
    nums = sorted(nums)  # (not modifying the input array but making a new variable (local))
    n = len(nums)
    triplet_set = set()  # for checking triplet's presence in O(1) time
    for i in range(n):  # (for target in targets:)
        num1 = nums[i]
        if num1 > 0:  # optimization
            break
        target = -num1
        # Now, finding the 2 nums using HashMap:
        # https://github.com/samyak1409/DSA/blob/7cbe5e00f474eb6a0aee5e0b58d66296a59604c3/01%29%20Arrays/019%29%20Two%20Sum.py#L67
        hashset = set()  # for checking presence of required num in O(1) time
        for j in range(i+1, n):  # starting from i+1 because we have nums[i] to be num1 already
            num3 = nums[j]
            num2 = target - num3  # num2 -> number added in hashset in previous iterations
            if num2 in hashset:
                triplet = [num1, num2, num3]
                triplet_tuple = tuple(triplet)
                if triplet_tuple not in triplet_set:
                    yield triplet
                    triplet_set.add(triplet_tuple)
            hashset.add(num3)
    """

    # 2.2) Optimal (Sorting & Two-Pointers): TC = O(n*log(n) + n^2); SC = O(n+n)
    # https://leetcode.com/problems/3sum/discuss/143636

    nums = sorted(nums)  # (not modifying the input array but making a new variable (local))

    n = len(nums)
    triplet_set = set()  # for checking triplet's presence in O(1) time
    for i in range(n):  # (for target in targets:)
        num1 = nums[i]
        if num1 > 0:  # optimization
            break
        target = -num1
        # Now, finding the 2 nums using Two-Pointers:
        # https://github.com/samyak1409/DSA/blob/7cbe5e00f474eb6a0aee5e0b58d66296a59604c3/01%29%20Arrays/019%29%20Two%20Sum.py#L47
        low, high = i+1, n-1  # starting from i+1 because we have nums[i] to be num1 already
        while low < high:
            num2, num3 = nums[low], nums[high]
            if num2 + num3 == target:
                triplet = [num1, num2, num3]
                triplet_tuple = tuple(triplet)
                if triplet_tuple not in triplet_set:
                    yield triplet
                    triplet_set.add(triplet_tuple)
                # not stopping but continuing with:
                low += 1
                high -= 1
                # because consider input: nums = [-2, 0, 1, 1, 2]
                # output would be: [[-2, 0, 2], [-2, 1, 1]] and not [[-2, 0, 2]]
            elif num2 + num3 < target:
                low += 1
            else:  # (if num2 + num3 > target)
                high -= 1

    # Also, checkout this DIFFERENT solution:
    # https://leetcode.com/problems/3sum/discuss/725950/Python-5-Easy-Steps-Beats-97.4-Annotated


# Similar Questions:
# https://leetcode.com/problems/two-sum
# https://leetcode.com/problems/3sum-closest
# https://leetcode.com/problems/4sum
# https://leetcode.com/problems/number-of-arithmetic-triplets
