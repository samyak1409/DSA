"""
https://leetcode.com/problems/4sum
"""


def four_sum(nums: list[int], target: int) -> list[list[int]]:
    """"""

    # 0) [TLE] Brute-force (Nested Loops & HashMap): TC = O(n^4); SC = O(n)

    # Core Logic: TC = O(n^4); SC = O(1)
    """
    n = len(nums)
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                for d in range(c+1, n):
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        yield [nums[a], nums[b], nums[c], nums[d]]
    """
    # But as we have to return an array of all the UNIQUE quadruplets, see Example 2:
    #     Input: nums = [2,2,2,2,2], target = 8
    #     Output: [[2,2,2,2]]
    #     Explanation:
    #     The only unique quadruplet is [2,2,2,2].
    # We will keep track of the quadruplets already added to the answer set and will not consider any quadruplet again:
    # TC = O(n*log(n) + n^4); SC = O(n+n)
    # IMP: Checkout:
    # https://github.com/samyak1409/DSA/blob/7cbe5e00f474eb6a0aee5e0b58d66296a59604c3/01%29%20Arrays/019.2%29%203Sum.py#L78
    """
    nums = sorted(nums)  # (not modifying the input array but making a new variable (local))
    n = len(nums)
    quadruplet_set = set()  # for checking quadruplet's presence in O(1) time
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                for d in range(c+1, n):
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        quadruplet = [nums[a], nums[b], nums[c], nums[d]]
                        quadruplet_tuple = tuple(quadruplet)
                        if quadruplet_tuple not in quadruplet_set:
                            yield quadruplet
                            quadruplet_set.add(quadruplet_tuple)
    """

    # 1) Optimal (Sorting & Two-Pointers): TC = O(n^(k-1)) = O(n^3); SC = O(n) {Sorting, HashSet, RecursionStack}
    # We can implement 4Sum by wrapping 3Sum in another loop.
    # But wait - there is a catch.
    # If an interviewer asks you to solve 4Sum, they can follow up with 5Sum, 6Sum, and so on.
    # What they are really expecting at this point is a k_sum solution.
    # Therefore, we will focus on a generalized implementation here.
    # https://leetcode.com/problems/4sum/solution
    # https://leetcode.com/problems/4sum/discuss/8545/Python-140ms-beats-100-and-works-for-N-sum-(Ngreater2)
    # It's Easy! First of all try to convert the bruteforce algorithm (which is iterative) to recursive.
    # Then generalize it (i.e. add a parameter k).
    # Lastly, add the Two-Pointers approach to find the last two numbers!

    # Helper Function:
    def two_sum(nums__, target__):
        """
        Finding the 2 numbers using Two-Pointers: TC = O(n); SC = O(1)
        https://github.com/samyak1409/DSA/blob/7cbe5e00f474eb6a0aee5e0b58d66296a59604c3/01%29%20Arrays/019.1%29%20Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted.py#L48
        """
        two_nums_set = set()
        low, high = 0, len(nums__)-1  # init
        while low < high:
            num1, num2 = nums__[low], nums__[high]
            if num1 + num2 == target__:
                two_nums_tup = (num1, num2)
                two_nums_set.add(two_nums_tup)  # only storing unique two-nums
                # Not stopping but continuing with:
                low += 1
                high -= 1
                # because consider input: (nums=[0, 1, 1, 2], target=2)
                # output would be: [[0, 2], [1, 1]] and not [[0, 2]]
            elif num1 + num2 < target__:
                low += 1
            else:  # (if num1 + num2 > target__)
                high -= 1
        return two_nums_set

    # Recursive Function:
    def k_sum(k, nums_, target_):
        if k == 2:  # base case
            return two_sum(nums__=nums_, target__=target_)
        # (k-2) for-loops:
        sub_ans_set = set()  # new
        for i in range(len(nums_)-k+1):
            num = nums_[i]
            sub_ans_set_ = k_sum(k=k-1, nums_=nums_[i+1:], target_=target_-num)  # RECURSE; old
            # Concatenating:
            # e.g. if num = -2 & sub_ans_set_ = {(0, 2), (1, 1)}, then sub_ans_set = {(-2, 0, 2), (-2, 1, 1)}
            """
            for sub_ans_tup_ in sub_ans_set_:
                sub_ans_tup = (num, *sub_ans_tup_)
                sub_ans_set.add(sub_ans_tup)
            """
            # In short:
            sub_ans_set.update([(num, *sub_ans_tup_) for sub_ans_tup_ in sub_ans_set_])
        return sub_ans_set

    ans_set = k_sum(k=4, nums_=sorted(nums), target_=target)
    return [list(ans_tup) for ans_tup in ans_set]  # returning the answer as lists

    # 2) Optimal (HashMap): TC = O(n^(k-1)) = O(n^3); SC = O(n) {Sorting, HashSet, RecursionStack, HashMap}
    # Similarly, we can implement the same concept with the base of HashMap too (instead of Two-Pointers).


# Similar Questions:
# https://leetcode.com/problems/two-sum
# https://leetcode.com/problems/3sum
# https://leetcode.com/problems/4sum-ii
# https://leetcode.com/problems/count-special-quadruplets
