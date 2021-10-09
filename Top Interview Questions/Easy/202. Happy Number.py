"""
https://leetcode.com/problems/happy-number/
"""


def isHappy(n: int) -> bool:

    # Approach 1 (Straight): TC = O(?); SC = O(?)

    """
    occurred = set()  # SET OVER LIST because https://www.geeksforgeeks.org/internal-working-of-set-in-python

    while n != 1:

        n = sum(map(lambda x: int(x) ** 2, str(n)))
        print(n)  # debug

        if n in occurred:  # O(1) op. on an avg.
            return False
        else:
            occurred.add(n)

    return True
    """

    # Approach 2 (Floyd's Cycle-Finding Algorithm; https://leetcode.com/problems/linked-list-cycle): TC = O(log n); SC = O(1)

    def get_next(num: int) -> int:
        return sum(map(lambda x: int(x) ** 2, str(num)))

    slow = n
    fast = get_next(get_next(n))

    while fast != 1 and slow != 1:  # loop while 1 not comes

        if slow == fast:  # slow = fast at any point => cycle is there so stop
            return False

        slow = get_next(slow)  # +1
        fast = get_next(get_next(fast))  # +2

    return True
