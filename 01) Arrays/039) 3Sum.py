"""
https://leetcode.com/problems/3sum
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    """"""

    # First of all, watch this GOLD explanation: https://youtu.be/onLoX6Nhvmg

    # 0) [TLE] Brute-force (Sort & Nested Loops): TC = O(n*log(n) + n^3); SC = O(n) {sorting}

    # 0.0) Core Logic: TC = O(n^3); SC = O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i]+nums[j]+nums[k] == 0:
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
    # 0.1) We will keep track of the triplets already added to the answer set and will not consider any triplet again:
    # TC = O(n^3 * 3*log(3)); SC = O(n) {hashset}
    """
    # from collections import Counter

    n = len(nums)
    triplet_set = set()  # for checking triplet's presence in O(1) time
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if sum(triplet := [nums[i], nums[j], nums[k]]) == 0:
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
                    # It's the problem, instead, we can sort the triplet (time will be O(3*log(3)) = O(1) only because 
                    # len(triplet) is 3), and since the triplets will be ordered now, we can use tuples (i.e. ordered 
                    # and immutable):
                    if (sorted_triplet_tuple := tuple(sorted(triplet))) not in triplet_set:
                        yield triplet
                        triplet_set.add(sorted_triplet_tuple)
    """
    # 0.2) Turns out that we can also just sort the input array and apply the above logic (without needing to sort the
    # triplets inside again and again): TC = O(n*log(n) + n^3); SC = O(n+n) {sorting, hashset}
    # "Brute Force Solution" in
    # https://leetcode.com/problems/3sum/discuss/1363302/C++-or-Brute-Force-or-Optimal(Two-Pointer-Method)-or-Commented-or-Time-O(N2)-or-Auxiliary-Space-O(1)
    """
    nums = sorted(nums)  # (not modifying the input array but making a new variable (local))
    if nums[-1] < 0:  # optimization
        return
    n = len(nums)
    triplet_set = set()  # for checking triplet's presence in O(1) time
    for i in range(n):
        if nums[i] > 0:  # optimization
            return
        for j in range(i+1, n):
            for k in range(j+1, n):
                if sum(triplet := [nums[i], nums[j], nums[k]]) == 0:
                    if (triplet_tuple := tuple(triplet)) not in triplet_set:
                        yield triplet
                        triplet_set.add(triplet_tuple)
    """
    # Why does this work?
    # Because if the input array is sorted, triplets will not form like [-1, 0, 1] & [0, 1, -1],
    # but like [-1, 0, 1] & [-1, 0, 1], i.e. by default sorted (i.e. in order)
    # Since this sorting beforehand technique is more time efficient than the previous one, will use this only in next
    # approaches.
    # 0.3) WAIT, turns out, again, that we can just use the fact that we're sorting the input array, and so we no longer
    # need HashSet to track unique triplets and save that O(n) space too!: TC = O(n*log(n) + n^3); SC = O(n) {sorting}
    """
    nums = sorted(nums)  # (not modifying the input array but making a new variable (local))
    if nums[-1] < 0:  # optimization
        return
    n = len(nums)
    for i in range(n):
        if nums[i] > 0:  # optimization
            return
        if i == 0 or nums[i] != nums[i-1]:  # proceed if not checked already for nums[i]
            for j in range(i+1, n):
                if j == i+1 or nums[j] != nums[j-1]:  # proceed if not checked already for nums[j]
                    for k in range(j+1, n):
                        if k == j+1 or nums[k] != nums[k-1]:  # proceed if not checked already for nums[k]
                            if nums[i]+nums[j]+nums[k] == 0:
                                yield [nums[i], nums[j], nums[k]]
    """
    # Since this (sorting beforehand + skipping duplicates) technique is more space efficient than the previous one,
    # will use this only in next approaches.

    # MOVING ON,
    # 3Sum -> num1 + num2 + num3 = 0
    # which can be written as num2 + num3 = -num1
    # Let -num1 = target
    # => num2 + num3 = target -> Two Sum

    # 1) Better (Sorting + Binary Search): TC = O(n*log(n) + (n^2)*log(n)); SC = O(n) {sorting}

    """
    nums = sorted(nums)  # (not modifying the input array but making a new variable (local))
    if nums[-1] < 0:  # optimization
        return
    n = len(nums)
    for i in range(n):
        if i == 0 or nums[i] != nums[i-1]:  # proceed if not checked already for nums[i]
            num1 = nums[i]
            if num1 > 0:  # optimization
                return
            for j in range(i+1, n):
                if j == i+1 or nums[j] != nums[j-1]:  # proceed if not checked already for nums[j]
                    num2 = nums[j]
                    target = -(num1+num2)  # required num3
                    # Now, finding num3 using Binary Search:
                    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/019%29%20Two%20Sum.py
                    lo, hi = j+1, n-1
                    while lo <= hi:
                        num3 = nums[(mid := (lo+hi)//2)]
                        if num3 == target:  # => triplet found
                            yield [num1, num2, num3]
                            break  # imp to break out once we get our num3 otherwise it will be an inf loop
                        elif num3 < target:
                            lo = mid + 1
                        else:  # (if num3 > target)
                            hi = mid - 1
    """

    # 2.1) Optimal (HashSet): TC = O(n*log(n) + n^2); SC = O(n+n+n) {sorting, hashset, hashset}
    # Using hashset for tracking unique triplets is easier than using skip duplicates technique for this approach.
    # Why? Try out yourself:
    # WA using skip duplicates technique:
    """
    nums = sorted(nums)  # (not modifying the input array but making a new variable (local))
    if nums[-1] < 0:  # optimization
        return
    n = len(nums)
    for i in range(n):  # (for target in targets:)
        if i == 0 or nums[i] != nums[i-1]:  # proceed if not checked already for nums[i]
            num1 = nums[i]
            if num1 > 0:  # optimization
                return
            target = -num1
            # Now, finding the 2 nums using HashSet:
            # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/019%29%20Two%20Sum.py
            hashset = set()  # for checking presence of required num in O(1) time
            for j in range(i+1, n):
                if j == i+1 or nums[j] != nums[j-1]:  # proceed if not checked already for nums[j]
                    num3 = nums[j]
                    num2 = target - num3  # num2 -> number added in hashset in previous iterations
                    if num2 in hashset:
                        yield [num1, num2, num3]
                    hashset.add(num3)
    """
    # AC using hashset to track unique triplets:
    """
    nums = sorted(nums)  # (not modifying the input array but making a new variable (local))
    if nums[-1] < 0:  # optimization
        return
    n = len(nums)
    triplet_set = set()  # for checking triplet's presence in O(1) time
    for i in range(n):  # (for target in targets:)
        num1 = nums[i]
        if num1 > 0:  # optimization
            return
        target = -num1
        # Now, finding the 2 nums using HashSet:
        # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/019%29%20Two%20Sum.py
        hashset = set()  # for checking presence of required num in O(1) time
        for j in range(i+1, n):
            num3 = nums[j]
            num2 = target - num3  # num2 -> number added in hashset in previous iterations
            if num2 in hashset:
                if (triplet_tuple := tuple(triplet := [num1, num2, num3])) not in triplet_set:
                    yield triplet
                    triplet_set.add(triplet_tuple)
            hashset.add(num3)
    """

    # 2.2) Optimal (Sorting & Two-Pointers): TC = O(n*log(n) + n^2); SC = O(n) {sorting}
    # https://en.wikipedia.org/wiki/3SUM#Quadratic_algorithm

    nums = sorted(nums)  # (not modifying the input array but making a new variable (local))
    n = len(nums)
    for i in range(n):  # (for target in targets:)
        if i == 0 or nums[i] != nums[i-1]:  # proceed if not checked already for nums[i]
            num1 = nums[i]
            target = -num1
            # Now, finding the 2 nums using Two-Pointers:
            # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/019%29%20Two%20Sum.py
            lo, hi = i+1, n-1
            while lo < hi:
                num2, num3 = nums[lo], nums[hi]
                if num2+num3 == target:
                    yield [num1, num2, num3]
                    # not stopping but continuing with:
                    lo, hi = lo+1, hi-1
                    # because consider input: nums = [-2, 0, 1, 1, 2]
                    # output would be: [[-2, 0, 2], [-2, 1, 1]] and not [[-2, 0, 2]]
                    # Skip Duplicates:
                    # https://leetcode.com/problems/3sum/discuss/7380/Concise-O(N2)-Java-solution/609489
                    while lo < hi and nums[lo] == num2:
                        lo += 1
                    while lo < hi and nums[hi] == num3:
                        hi -= 1
                elif num2+num3 < target:
                    lo += 1
                else:  # (if num2+num3 > target)
                    hi -= 1

    # Also, checkout this DIFFERENT solution:
    # https://leetcode.com/problems/3sum/discuss/725950/Python-5-Easy-Steps-Beats-97.4-Annotated


# Similar Questions:
# https://leetcode.com/problems/two-sum
# https://leetcode.com/problems/3sum-closest
# https://leetcode.com/problems/4sum
# https://leetcode.com/problems/number-of-arithmetic-triplets
