"""
https://leetcode.com/problems/happy-number
"""


def is_happy(n: int) -> bool:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/02%29%20Linked%20List/032%29%20Linked%20List%20Cycle.py

    # For (understanding the) Complexity Analysis, read https://leetcode.com/problems/happy-number/solution.

    # 1.1) Optimal (HashSet): TC = O(C*log(n)) = O(log(n)); SC = O(C) = O(1); {C for Constant}

    """
    seen = {n}
    while n != 1:  # TC = O(C) = O(1)
        n = sum(int(digit)**2 for digit in str(n))  # ++
        # https://stackoverflow.com/questions/1247486/list-comprehension-vs-map
        # TC = O(log(n)) because the no. of digits in a number is given by log(n).
        # https://math.stackexchange.com/questions/231742/proof-how-many-digits-does-a-number-have-lfloor-log-10-n-rfloor-1
        # https://stackoverflow.com/questions/50261364/explain-why-time-complexity-for-summing-digits-in-a-number-of-length-n-is-ologn
        if n in seen:
            return False  # loop formed => is_happy = False
        seen.add(n)
    return True  # n == 1 => is_happy = True
    """

    # 1.2) Optimal (Floyd's Cycle-Finding Algorithm): TC = O(C*log(n)) {C for Constant} = O(log(n)); SC = O(1)
    # https://leetcode.com/problems/happy-number/discuss/56917/My-solution-in-C(-O(1)-space-and-no-magic-math-property-involved-)

    # Helper Function:
    def get_next(num: int) -> int: return sum(int(digit)**2 for digit in str(num))
    # https://stackoverflow.com/questions/1247486/list-comprehension-vs-map
    # TC = O(log(n)) because the no. of digits in a number is given by log(n).
    # https://math.stackexchange.com/questions/231742/proof-how-many-digits-does-a-number-have-lfloor-log-10-n-rfloor-1
    # https://stackoverflow.com/questions/50261364/explain-why-time-complexity-for-summing-digits-in-a-number-of-length-n-is-ologn

    slow, fast = n, get_next(get_next(n))
    while fast != 1 and slow != 1:  # if any of them reached to 1 => is_happy = True; TC = O(C) = O(1)
        if slow == fast:  # => cycle is there
            return False  # => is_happy = False
        slow, fast = get_next(slow), get_next(get_next(fast))  # +1, +2
    return True

    # Why does these algorithms work? Because only two cases are possible here:
    # 1) n will reach to 1 => loop will obviously not be there, because if loop was there, n would haven't reached to 1
    #    at the first place.
    # 2) n will NOT reach to 1 => loop will be there, the reason why n didn't reach to 1, and so our cycle finding algo
    #    will find it!
    # 3) n will jump from one to another number infinitely? As numbers are infinite, it is possible right?
    #    NO! Why? Read here: https://leetcode.com/problems/happy-number/solution
