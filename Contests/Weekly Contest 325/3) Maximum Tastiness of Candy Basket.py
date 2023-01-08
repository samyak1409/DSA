"""
https://leetcode.com/problems/maximum-tastiness-of-candy-basket
"""


def maximum_tastiness(price: list[int], k: int) -> int:
    """"""

    # 1) Optimal ("Reverse Engineer" Finding Ans.): TC = O(log(max(price)-min(price)) * n); SC = O(1)
    # {note: max(max(price)-min(price)) == 10^9}
    # The answer is binary searchable.
    # For some x, we can use a greedy strategy to check if it is possible to pick k distinct candies with tastiness
    # being at least x.
    # Sort prices and iterate from left to right. For some price[i] check if the price difference between the last taken
    # candy and price[i] is at least x. If so, add the candy i to the basket.
    # So, a candy basket with tastiness x can be achieved if the basket size is bigger than or equal to k.
    # https://leetcode.com/problems/maximum-tastiness-of-candy-basket/solutions/2947983/c-java-python-binary-search-and-sorting
    # https://leetcode.com/problems/maximum-tastiness-of-candy-basket/solutions/2948107/binary-search
    # UNEXPECTEDLY-GOOD EXPLANATION: https://youtu.be/ob6VrRpqqHw

    price = sorted(price)
    # print(price)  #debugging

    lo, hi = 0, price[-1]-price[0]  # max diff possible
    n = len(price)
    while lo <= hi:  # O(log(max(price)-min(price)) * n)
        diff = (lo+hi) // 2  # mid

        # Check if with this particular `diff`, choosing k candies is possible or not:
        count = 1
        candy1 = price[0]  # start from the start
        for i in range(1, n):  # go till end; O(n)
            candy2 = price[i]
            if candy2-candy1 >= diff:
                count += 1  # we found 1 more candy
                candy1 = candy2  # update
                if count == k:  # if we got enough candies, stop
                    break

        if count == k:  # for this particular `diff`, it's possible, so let's try with a bigger `diff`
            lo = diff + 1
        else:
            hi = diff - 1
    return lo - 1

    # Note that we could have done the Linear Search in place of Binary Search, but that would be very slow, and since
    # the `integers` are sorted, Binary Search is the correct choice.
