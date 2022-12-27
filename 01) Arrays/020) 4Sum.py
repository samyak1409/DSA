"""
https://leetcode.com/problems/4sum
"""


def four_sum(nums: list[int], target: int) -> list[list[int]]:
    """"""

    # We can implement 4Sum by wrapping 3Sum in another loop.
    # But wait - there is a catch.
    # If an interviewer asks you to solve 4Sum, they can follow up with 5Sum, 6Sum, and so on.
    # What they are really expecting at this point is a k_sum solution.
    # Therefore, we will focus on a generalized implementation here.
    # https://leetcode.com/problems/4sum/solution
    # It's Easy! First of all try to convert the iterative brute-force algorithm to recursive (with a parameter k).
    # Then, add the Two-Pointers approach to find the last two numbers!

    # 0) [TLE] Brute-force (Sort & Nested Loops (4Sum)): TC = O(n*log(n) + n^4); SC = O(n) {sorting}

    # Read how we reached to the following algorithm in detail from `039 3Sum.py`'s `0) Brute-force`
    # (https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/039%29%203Sum.py).
    """
    nums = sorted(nums)  # new local variable
    n = len(nums)
    for a in range(n):
        if a == 0 or nums[a] != nums[a-1]:  # proceed if not checked already for nums[a]
            for b in range(a+1, n):
                if b == a+1 or nums[b] != nums[b-1]:  # proceed if not checked already for nums[b]
                    for c in range(b+1, n):
                        if c == b+1 or nums[c] != nums[c-1]:  # proceed if not checked already for nums[c]
                            for d in range(c+1, n):
                                if d == c+1 or nums[d] != nums[d-1]:  # proceed if not checked already for nums[d]
                                    if nums[a]+nums[b]+nums[c]+nums[d] == target:
                                        yield [nums[a], nums[b], nums[c], nums[d]]
    """

    # 1) Optimal (Sorting & Recursion (kSum) & Two-Pointers): TC = O(n*log(n) + n^(k-1)) = O(n*log(n) + n^3);
    #                                                         SC = O(n) {Sorting, HashSet, RecursionStack}
    # https://leetcode.com/problems/4sum/discuss/8545/Python-140ms-beats-100-and-works-for-N-sum-(Ngreater2)

    # Recursive Function:
    def k_sum(k: int, target_: int, start: int = 0) -> None:
        if k == 2:  # base case
            # Now, finding the 2 nums using Two-Pointers: TC = O(n); SC = O(1)
            # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/019%29%20Two%20Sum.py
            lo, hi = start, n-1
            while lo < hi:
                num1, num2 = nums[lo], nums[hi]
                if num1+num2 == target_:
                    ans.append([num1, num2])
                    # not stopping but continuing with:
                    lo, hi = lo+1, hi-1
                    # because consider input: nums = [-2, 0, 1, 1, 2]
                    # output would be: [[-2, 0, 2], [-2, 1, 1]] and not [[-2, 0, 2]]
                    # Skip Duplicates:
                    # https://leetcode.com/problems/3sum/discuss/7380/Concise-O(N2)-Java-solution/609489
                    while lo < hi and nums[lo] == num1:
                        lo += 1
                    while lo < hi and nums[hi] == num2:
                        hi -= 1
                elif num1+num2 < target_:
                    lo += 1
                else:  # (if num1+num2 > target_)
                    hi -= 1
        elif k > 2:
            for i in range(start, n):
                num = nums[i]
                if i == start or num != nums[i-1]:  # proceed if not already checked for num
                    len_before = len(ans)  # save start index of new answers
                    k_sum(k=k-1, target_=target_-num, start=i+1)  # recurse in; fill new answers
                    for x in range(len_before, len(ans)):  # insert the num with the answers it's considered with
                        # ans[x].insert(0, num)  # O(4)
                        # but as `You may return the answer in any order.`
                        ans[x].append(num)  # O(1)

    n = len(nums)
    nums = sorted(nums)
    ans = []  # global var that will be modified by the func.
    k_sum(k=4, target_=target)  # fill ans
    return ans


# Similar Questions:
# https://leetcode.com/problems/two-sum
# https://leetcode.com/problems/3sum
# https://leetcode.com/problems/4sum-ii
# https://leetcode.com/problems/count-special-quadruplets
