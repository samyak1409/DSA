"""
https://leetcode.com/problems/majority-element-ii
"""


def majority_element(nums: list[int]) -> list[int]:
    """"""

    # All the solutions are similar to the solutions of
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/015%29%20Majority%20Element.py.

    # 0.1) Brute-force (Traverse and Count): TC = O(n^2); SC = O(1)
    # "elements that appears more than ⌊ n/3 ⌋ times" => count(x) > n//3, so we can simply traverse the array to find
    # the elements.

    """
    ans = []  # SC = O(1) because at most only 2 majority elements can be there {Why? Because 1 <= n // [(n//3)+1] <= 2}
    n = len(nums)
    for num in nums:
        if num not in ans and nums.count(num) > n//3:  # `num not in ans` so that if num is a majority element, it does
            # not get added to ans everytime it appears
            ans.append(num)
            if len(ans) == 2:  # optimization: if at any point after adding a majority element to the ans, len becomes
                # 2, we can stop, because we know no. of majority elements can't be > 2
                break
    return ans
    """

    # 0.3) Brute-force (Sorting): TC = O(n*log(n)); SC = O(n)

    """
    ans = []
    nums = sorted(nums)
    n = len(nums)
    n_by_3 = n // 3
    for i in range(n-n_by_3):
        num = nums[i]
        if num not in ans and nums[i+n_by_3] == num:  # `num not in ans` so that if num is a majority element, it does
            # not get added to ans everytime it appears
            ans.append(num)
            if len(ans) == 2:  # optimization: if at any point after adding a majority element to the ans, len becomes
                # 2, we can stop, because we know no. of majority elements can't be > 2
                break
    return ans
    """
    # Little optimization: use while loop:
    # If a majority element is found, then directly jump `i` to `i + n_by_3 + 1` instead of just `i+1`.
    """
    ans = []
    nums = sorted(nums)
    n = len(nums)
    n_by_3 = n // 3
    i = 0
    while i+n_by_3 < n:
        num = nums[i]
        if num not in ans and nums[i+n_by_3] == num:  # `num not in ans` so that if num is a majority element, it does
            # not get added to ans everytime it appears
            ans.append(num)
            if len(ans) == 2:  # optimization: if at any point after adding a majority element to the ans, len becomes
                # 2, we can stop, because we know no. of majority elements can't be > 2
                break
            i += n_by_3  # main reason to use `while` loop over `for` loop
        i += 1
    return ans
    """

    # 0.2) Brute-force (HashMap): TC = O(n); SC = O(n)
    # Optimization of `0.1)` with the help of HashMap.

    """
    from collections import Counter
    count = Counter()
    ans = []
    n = len(nums)
    for num in nums:
        count[num] += 1
        if num not in ans and count[num] > n//3:  # `num not in ans` so that if num is a majority element, it does not
            # get added to ans everytime it appears
            ans.append(num)
            if len(ans) == 2:  # optimization: if at any point after adding a majority element to the ans, len becomes
                # 2, we can stop, because we know no. of majority elements can't be > 2
                break
    return ans
    """

    # 1) [WA] Better (Randomization): TC = Worst: O(inf); Average/Best: O(n); SC = O(1)
    # Probability(choosing the majority element) >= ~1/3
    # Same logic as described in https://leetcode.com/problems/majority-element/solution/#approach-4-randomization
    # Won't work because we don't know how many majority elements will be there in the array (0/1/2)?
    # So the loop will run infinitely, we don't know when to stop.
    # Would have worked perfectly if the exact no. of majority elements there was given in the Q. or as a parameter.

    """
    from random import choice

    ans = []
    n = len(nums)
    while True:
        rand_num = choice(seq=nums)  # choose a random element from the array
        # check if the chosen element is the majority element or not:
        if rand_num not in ans and nums.count(rand_num) > n//3:  # `rand_num not in ans` so that if rand_num is a
            # majority element, it does not get added to ans everytime chose
            ans.append(rand_num)
            if len(ans) == 2:  # optimization: if at any point after adding a majority element to the ans, len becomes
                # 2, we can stop, because we know no. of majority elements can't be > 2
                break
    return ans
    """

    # Follow up: Could you solve the problem in linear time and in O(1) space?

    # 2) Optimal (Extended "Boyer-Moore Majority Voting Algorithm"): TC = O(n); SC = O(1)
    # Check "Boyer-Moore Majority Voting Algorithm" at:
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/015%29%20Majority%20Element.py
    # Explanation of Extended "Boyer-Moore Majority Voting Algorithm": https://youtu.be/yDbkQd9t2ig?t=182
    # More Explanations:
    # https://leetcode.com/problems/majority-element-ii/discuss/63520/Boyer-Moore-Majority-Vote-algorithm-and-my-elaboration/112881
    # https://assets.leetcode.com/users/andriy111/image_1584562040.png (From
    # https://leetcode.com/problems/majority-element-ii/discuss/543672/BoyerMoore-majority-vote-algorithm-EXPLAINED)

    # [WA] Following implementation has a problem, dry run on the small test case [2,2] to know.
    """
    # Init:
    m1, m2, v1, v2 = None, None, 0, 0
    # Loop:
    for num in nums:
        # If votes are 0, assign major:
        if v1 == 0:
            m1 = num
        elif v2 == 0:
            m2 = num
        # If num is major, ++votes:
        if num == m1:
            v1 += 1
        elif num == m2:
            v2 += 1
        # If num is none of the two, -- the relative votes of each:
        else:
            v1 -= 1
            v2 -= 1
    # Verify the majors, and return:
    return [m for m in (m1, m2) if nums.count(m) > len(nums)//3]
    """

    # However, since the problem is very specific, we can actually try to add a check for exactly that, and it works!:
    """
    # Init:
    m1, m2, v1, v2 = None, None, 0, 0
    # Loop:
    for num in nums:
        # If votes are 0 and `num` is not a current major, assign major:
        if v1 == 0 and num != m2:
            m1 = num
        elif v2 == 0 and num != m1:
            m2 = num
        # If num is major, ++votes:
        if num == m1:
            v1 += 1
        elif num == m2:
            v2 += 1
        # If num is none of the two, -- the relative votes of each:
        else:
            v1 -= 1
            v2 -= 1
    # Verify the majors, and return:
    return [m for m in (m1, m2) if nums.count(m) > len(nums)//3]
    """

    # Or we can also solve it like following:
    m1, m2, v1, v2 = None, None, 0, 0  # init
    # taking two vars only because at most only 2 majority elements can be there
    # {Why? Because 1 <= n // [(n//3)+1] <= 2}
    # 1st Pass (Extended "Boyer-Moore Majority Voting Algorithm"):
    for num in nums:  # O(n)
        if num == m1:
            v1 += 1
        elif num == m2:
            v2 += 1
        elif v1 == 0:  # change m1
            m1, v1 = num, 1
        elif v2 == 0:  # change m2
            m2, v2 = num, 1
        else:  # if (num not in (m1, m2)) and (v1 >= 1 and v2 >= 1)
            v1, v2 = v1-1, v2-1  # relative_votes--
    # 2nd Pass (When the array will contain no majority elements, then `m1` & `m2` will contain false
    # positives which will be filtered out next):
    # return list(filter(lambda major: nums.count(major) > len(nums)//3, (m1, m2)))  # O(n)
    return [m for m in (m1, m2) if nums.count(m) > len(nums)//3]  # O(n)

    # Give this a read too:
    # https://leetcode.com/problems/majority-element-ii/discuss/63502/6-lines-general-case-O(N)-time-and-O(k)-space


# Similar Questions:
# https://leetcode.com/problems/majority-element
# https://leetcode.com/problems/most-frequent-even-element
