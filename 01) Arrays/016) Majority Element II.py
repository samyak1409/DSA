"""
https://leetcode.com/problems/majority-element-ii
"""


def majority_element(nums: list[int]) -> list[int]:
    """"""

    # 0.1) Brute-force (Traverse and Count): TC = O(n^2); SC = O(1)
    # "elements that appears more than ⌊ n/3 ⌋ times" => count(x) > n//3, so we can simply traverse the array to find
    # the elements.

    """
    ans = []  # SC = O(1) because at most only 2 majority elements can be there {Why? Because 1 <= n // [(n//3)+1] <= 2}
    n = len(nums)
    for num in nums:
        if num not in ans and nums.count(num) > n//3:  # "num not in ans" so that if num is a majority element, it does
            # not get added to ans everytime it appears
            ans.append(num)
            if len(ans) == 2:  # if at any point after adding a majority element to the ans, len becomes 2, we can
                # simply break, because we know no. of majority elements can't be > 2
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
        if num not in ans and count[num] > n//3:  # "num not in ans" so that if num is a majority element, it does not
            # get added to ans everytime it appears after appearing (n//3 + 1) times ✔
            ans.append(num)
            if len(ans) == 2:  # if at any point after adding a majority element to the ans, len becomes 2, we can
                # simply break, because we know no. of majority elements can't be > 2
                break
    return ans
    """

    # 1) [WA] Better (Randomization): TC = Worst: O(inf); Average/Best: O(n); SC = O(1)
    # Probability(choosing the majority element) > ~1/3
    # Same logic as described in https://leetcode.com/problems/majority-element/solution
    # Not working because we don't know how many majority elements will be there in the array (0/1/2)
    # So the loop will run infinitely, we don't know when to stop.

    """
    from random import choice

    ans = []
    n = len(nums)
    while True:
        rand_num = choice(seq=nums)  # choose a random element from the array
        # check if the chosen element is the majority element or not:
        if rand_num not in ans and nums.count(rand_num) > n//3:  # "rand_num not in ans" so that if rand_num is a
            # majority element, it does not get added to ans everytime chose
            ans.append(rand_num)
            if len(ans) == 2:  # if at any point after adding a majority element to the ans, len becomes 2, we can
                # simply break, because we know no. of majority elements can't be > 2
                break
    return ans
    """

    # 2) Optimal (Extended "Boyer-Moore Majority Voting Algorithm"): TC = O(n); SC = O(1)
    # Check "Boyer-Moore Majority Voting Algorithm" at
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/015%29%20Majority%20Element%20.py
    # Explanation of Extended "Boyer-Moore Majority Voting Algorithm": https://youtu.be/yDbkQd9t2ig?t=182

    candidate1, candidate2, count1, count2 = None, None, 0, 0  # initialization
    # taking two candidates only because at most only 2 majority elements can be there
    # {Why? Because 1 <= n // [(n//3)+1] <= 2}
    # 1st Pass (Assigning all the majority elements (at most 2) to "candidate1" & "candidate2"):
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1, count2 = count1-1, count2-1
    # 2nd Pass (When the array will contain no majority elements, then "candidate1" & "candidate2" will contain false
    # positives which will be filtered out next):
    return list(filter(lambda candidate: nums.count(candidate) > len(nums)//3, [candidate1, candidate2]))

    # Give this a read too:
    # https://leetcode.com/problems/majority-element-ii/discuss/63502/6-lines-general-case-O(N)-time-and-O(k)-space
