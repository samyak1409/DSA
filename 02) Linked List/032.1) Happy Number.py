"""
https://leetcode.com/problems/happy-number
"""


def is_happy(n: int) -> bool:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/02%29%20Linked%20List/032%29%20Linked%20List%20Cycle.py

    # For (understanding the) Complexity Analysis, read https://leetcode.com/problems/happy-number/solution.

    # 1.1) Optimal (HashSet): TC = O(C*log10(n)) = O(log10(n)); SC = O(C) = O(1); {C for Constant}

    """
    seen = set()
    while n != 1:  # TC = O(C) = O(1)
        seen.add(n)
        n = sum(int(digit)**2 for digit in str(n))  # next n
        # https://stackoverflow.com/questions/1247486/list-comprehension-vs-map
        # TC = O(log10(n)) because the no. of digits in a number is given by log10(n).
        # https://math.stackexchange.com/questions/231742/proof-how-many-digits-does-a-number-have-lfloor-log-10-n-rfloor-1
        # https://stackoverflow.com/questions/50261364/explain-why-time-complexity-for-summing-digits-in-a-number-of-length-n-is-ologn
        if n in seen:
            return False  # loop formed => is_happy = False
    return True  # n == 1 => is_happy = True
    """

    # 1.2) Optimal (Floyd's Cycle-Finding Algorithm): TC = O(C*log10(n)) {C for Constant} = O(log10(n)); SC = O(1)
    # https://leetcode.com/problems/happy-number/discuss/56917/My-solution-in-C(-O(1)-space-and-no-magic-math-property-involved-)

    # Helper Function:
    def get_next(num: int) -> int: return sum(int(digit)**2 for digit in str(num))
    # https://stackoverflow.com/questions/1247486/list-comprehension-vs-map
    # TC = O(log10(n)) because the no. of digits in a number is given by log10(n).
    # https://math.stackexchange.com/questions/231742/proof-how-many-digits-does-a-number-have-lfloor-log-10-n-rfloor-1
    # https://stackoverflow.com/questions/50261364/explain-why-time-complexity-for-summing-digits-in-a-number-of-length-n-is-ologn

    slow, fast = n, get_next(get_next(n))
    while fast != 1 and slow != 1:  # TC = O(C) = O(1)
        if slow == fast:
            return False  # cycle is there => is_happy = False
        slow, fast = get_next(slow), get_next(get_next(fast))  # +1, +2
    return True  # if any of them reached to 1 => is_happy = True

    # Why does these algorithms work? Because only two cases are possible here:
    # 1) n will reach to 1 => loop was not there, and n reached to 1
    # 2) n will NOT reach to 1 => loop was there, the reason why n didn't reach to 1, and so our cycle finding algo
    #                             will find it
    # 3) n will jump from one to another number infinitely? As numbers are infinite, it is possible right?
    #    NO! Why? Read here:
    #    """For a number with 3 digits, it's impossible for it to ever go larger than 243. This means it will have to
    #    either get stuck in a cycle below 243 or go down to 1. Numbers with 4 or more digits will always lose a digit
    #    at each step until they are down to 3 digits. So we know that at worst, the algorithm might cycle around all
    #    the numbers under 243 and then go back to one it's already been to (a cycle) or go to 1. But it won't go on
    #    indefinitely, allowing us to rule out the 3rd option.
    #    Even though you don't need to handle the 3rd case in the code, you still need to understand why it can never
    #    happen, so that you can justify why you didn't handle it."""
    #    -https://leetcode.com/problems/happy-number/solution
