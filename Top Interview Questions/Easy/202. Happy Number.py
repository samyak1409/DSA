"""
https://leetcode.com/problems/happy-number/
"""


def isHappy(n: int) -> bool:

    def next_(num: int) -> int:  # TC = O(log n); because the number of digits in a number is given by log n; Here's why: https://math.stackexchange.com/a/231745
        """Helper Function"""
        return sum([int(x)**2 for x in str(num)])  # https://stackoverflow.com/questions/1247486/list-comprehension-vs-map

    # Approach 1 (Using Hash Set): TC = O(log n); SC = O(log n); why? read on solution page 💯

    """
    occurred = {n}  # SET OVER LIST because https://www.geeksforgeeks.org/internal-working-of-set-in-python

    while n != 1:

        n = next_(n)

        if n in occurred:  # O(1) op. on an avg.
            return False  # loop formed => isHappy = False
        else:
            occurred.add(n)

    return True
    """

    # Approach 2 (Floyd's Cycle-Finding Algorithm; https://leetcode.com/problems/linked-list-cycle): TC = O(log n); SC = O(1)

    slow = n
    fast = next_(next_(n))

    while fast != 1 and slow != 1:  # loop while 1 not comes

        if slow == fast:  # slow=fast at any point => cycle is there, so stop
            return False

        slow = next_(slow)  # +1
        fast = next_(next_(fast))  # +2

    return True


# MUST READ: https://leetcode.com/problems/happy-number/solution

"""
for i in range(1, 9+1):
    n = 10**i-1
    print(n)
    print(isHappy(n))
    print()
"""
