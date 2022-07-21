"""
https://leetcode.com/problems/majority-element-ii
"""


def majorityElement(nums: list[int]) -> list[int]:
    """"""

    # 0.1) Brute-force (Traverse and Count): TC = O(n^2); SC = O(1)
    # "elements that appears more than ⌊ n/3 ⌋ times" => count(x) > n//3, so we can simply traverse the array to find the elements.

    """
    ans = []  # SC = O(1) because at most only 2 majority elements can be there {Why? Because 1 <= n // [(n//3)+1] <= 2}
    n = len(nums)
    for num in nums:
        if num not in ans and nums.count(num) > n//3:  # "num not in ans" so that if num is a majority element, it does not get added to ans everytime it appears
            ans.append(num)
            if len(ans) == 2:  # if at any point after adding a majority element to the ans, len becomes 2, we can simply break, because we know no. of majority elements can't be > 2
                break
    return ans
    """

    # 0.2) Brute-force (HashMap): TC = O(n); SC = O(n)
    # Optimization of "0.1)" with the help of HashMap.

    """
    from collections import Counter
    count = Counter()
    ans = []
    n = len(nums)
    for num in nums:
        count[num] += 1
        if num not in ans and count[num] > n//3:  # "num not in ans" so that if num is a majority element, it does not get added to ans everytime it appears after appearing (n//3 + 1) times ✔
            ans.append(num)
            if len(ans) == 2:  # if at any point after adding a majority element to the ans, len becomes 2, we can simply break, because we know no. of majority elements can't be > 2
                break
    return ans
    """

    # 1) (TLE (due to wrong logic)) Tried Randomization but Won't Work: TC = Worst: O(inf); Average/Best: O(n); SC = O(1)
    # Probability(choosing the majority element) > ~1/3
    # Same logic as described in https://leetcode.com/problems/majority-element/solution
    # Not working because we don't know how many majority elements will be there in the array (0/1/2)
    # So the loop will run infinitely, we don't know when to stop.

    from random import choice

    ans = []
    n = len(nums)
    while True:
        rand_num = choice(seq=nums)  # choose a random element from the array
        # check if the chosen element is the majority element or not:
        if rand_num not in ans and nums.count(rand_num) > n//3:  # "rand_num not in ans" so that if rand_num is a majority element, it does not get added to ans everytime chose
            ans.append(rand_num)
            if len(ans) == 2:  # if at any point after adding a majority element to the ans, len becomes 2, we can simply break, because we know no. of majority elements can't be > 2
                break
    return ans
