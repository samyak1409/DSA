"""
https://leetcode.com/problems/richest-customer-wealth
"""


def maximum_wealth(accounts: list[list[int]]) -> int:
    """"""

    # Calculate the wealth of each customer.
    # Find the maximum element in array.

    # 1) Optimal (Iterate & Calc.): TC = O(m*n); SC = O(1)

    """
    max_wealth = 0
    for amount_list in accounts:
        wealth = 0
        for amount in amount_list:
            wealth += amount
        if wealth > max_wealth:
            max_wealth = wealth
    return max_wealth
    """

    """
    max_wealth = 0
    for amount_list in accounts:
        max_wealth = max(max_wealth, sum(amount_list))
    return max_wealth
    """

    """
    return max(sum(amount_list) for amount_list in accounts)
    """

    # https://leetcode.com/problems/richest-customer-wealth/solutions/952795/java-python-solution
    return max(map(sum, accounts))
