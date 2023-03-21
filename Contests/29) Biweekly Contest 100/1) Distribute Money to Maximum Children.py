"""
https://leetcode.com/problems/distribute-money-to-maximum-children
"""


def dist_money(money: int, children: int) -> int:
    """"""

    # This Q. is tricky.

    # This is an optimization (maximization) problem.

    # 1) Brute-force (Greedy)

    # 1.1) Giving dollar one by one: TC = O(min(m, 8c)); SC = O(c)

    """
    # First, handling the base edge case:    
    money -= children  # "Everyone must receive at least 1 dollar."
    if money < 0:
        return -1  # "If there is no way to distribute the money, return -1."

    ans = 0  # no. of children w/ exactly 8 dollars
    distributions, i = [1] * children, 0  # distributions[i] is money distributed to i-th child
    while money and i != children:  # while money is left and all children have not received
        money, c[i] = money-1, c[i]+1  # give a dollar
        if c[i] == 8:  # if current children have received 8 dollars
            ans += 1  # increase count
            i += 1  # move to next child

    return ans - (money != 0 or c[-1] == 4)
    # = ans - (1 if (money is left) or (last child have 4 dollars))
    # Why?
    # "All money must be distributed.", so if `money is left`, we can give the left money to one of the children.
    # "Nobody receives 4 dollars.", so if the `last child has 4 dollars`, we can make it 3 by giving the 2nd last child 
    # 1 from the last child.
    """

    # 1.2) Giving 7 dollars at a time: TC = O(min(m//7, c)); SC = O(1)

    """
    # First, handling the base edge case:
    money -= children  # "Everyone must receive at least 1 dollar."
    if money < 0:
        return -1  # "If there is no way to distribute the money, return -1."

    ans = 0  # no. of children w/ exactly 8 dollars
    while money >= 7 and ans != children:  # while money is left and all children have not received
        money -= 7  # make a child have 8 dollars
        ans += 1  # increase count

    return ans - (money != 0 and ans == children or money == 3 and ans == children-1)
    # `money != 0 and ans == children`: if money is left and all the children have exactly 8 dollars, we can give the
    # left money to one of the children. ("All money must be distributed.")
    # `money == 3 and ans == children-1`: if we're left w/ exactly 3 dollars and only one child has not 8 dollars, then
    # he/she must have 1 dollar, because that's what we gave before, so, now we can't give these 3 to the last child, we
    # have to give 1 to some other child that will make another child have 9 dollars. ("Nobody receives 4 dollars.")
    """

    # 2) Optimal (Greedy, Directly calc. using mod op): TC = O(1); SC = O(1)
    # https://leetcode.com/problems/distribute-money-to-maximum-children/solutions/3312090/ugh-o-1

    # First, handling the base edge case:
    money -= children  # "Everyone must receive at least 1 dollar."
    if money < 0:
        return -1  # "If there is no way to distribute the money, return -1."

    # Perfect Case:
    if money == children*7:
        return children

    # When n-1 children get 8 dollars, and 1 child gets 4 dollar:
    if money == (children-1)*7 + 3:
        return children-2

    # Remaining cases will be covered by this:
    # `money//7`: money is less, all the children won't get 8 dollars.
    # `children-1`: money is more, all the children got 8 dollars but as the money is left, we have to give it to one of
    #               the child.
    return min(money//7, children-1)
