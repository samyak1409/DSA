"""
https://leetcode.com/problems/minimum-penalty-for-a-shop
"""


def best_closing_time(customers: str) -> int:
    """"""

    # 1) Optimal (Traverse and Count Penalties): TC = O(n); SC = O(1)
    # At any index, the penalty is the sum of prefix count of ‘N’ and suffix count of ‘Y’.
    # Enumerate all indices and find the minimum such value.

    # 1.0) Intuitive: TC = O(n); SC = O(n)

    """
    y_count = customers.count('Y')
    penalties = [y_count]  # init
    for customer in customers:
        if customer == 'Y':
            y_count -= 1
        penalties.append(y_count)

    n_count = 0
    min_penalty, ans = penalties[0], 0  # init
    for i, customer in enumerate(customers, start=1):
        if customer == 'N':
            n_count += 1
        penalties[i] += n_count
        if (penalty := penalties[i]) < min_penalty:
            min_penalty, ans = penalty, i
    return ans
    """

    # 1.1) Shortened: TC = O(n); SC = O(1)
    # https://leetcode.com/problems/minimum-penalty-for-a-shop/discuss/2851426/O(n)

    penalty = min_penalty = customers.count('Y')  # init:
    # if the shop doesn't even open, penalty will be the total no. of customers
    ans = 0  # init: 0th hour
    for hour, customer in enumerate(customers, start=1):
        penalty -= 1 if customer == 'Y' else -1
        if penalty < min_penalty:
            min_penalty, ans = penalty, hour
    return ans
