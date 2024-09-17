"""
https://leetcode.com/problems/climbing-stairs
"""


def climb_stairs(n: int) -> int:
    """"""

    # Hint: To reach nth step, what could have been your previous steps? (Think about the step sizes)

    # 0) Brute-force (Recursion): TC = O(2^n); SC = O(n)
    # Trying all possible ways using recursion.

    """
    ways = [0]  # list instead of int for mutability

    # Recursive Function: TC = O(2^n); SC = O(n)
    def recurse(stairs_left: int) -> None:
        if stairs_left == 0:  # base case: reached at the top
            ways[0] += 1
            return  # recurse out
        recurse(stairs_left-1)  # move one step and recurse in
        if stairs_left > 1:
            recurse(stairs_left-2)  # move two steps and recurse in

    recurse(stairs_left=n)
    return ways[0]
    """

    # 1) Time-Optimal (Recursion+Memoization): TC = O(n); SC = O(n)
    # Just adding memoization to the above approach.

    """
    ways = [0]  # list instead of int for mutability
    memo = [0] * (n+1)  # using list as a hash-map, indices act like keys; `n+1` as indices start from 0; SC = O(n)

    # Recursive Function: TC = SC = O(n)
    def recurse(stairs_left: int) -> None:
        if stairs_left == 0:  # base case: reached at the top
            ways[0] += 1
            return  # recurse out
        if mem := memo[stairs_left-1]:  # first check if we already have the ans.
            ways[0] += mem  # just add to the ans. if we've
        else:  # if this is the first time `recurse()` is called with `n`
            recurse(stairs_left-1)  # move one step and recurse in
        if stairs_left > 1:
            # similar as above:
            if mem := memo[stairs_left-2]:
                ways[0] += mem
            else:
                recurse(stairs_left-2)
        memo[stairs_left] = ways[0]  # finally save the ans. for current `n` so that it's never calc. again

    recurse(stairs_left=n)
    return ways[0]
    """

    # 2) Optimal (Fibonacci): TC = O(n); SC = O(1)
    # Proof:
    # Basically, if we're on n-th stair, we only had two options from which we could've come here, either from (n-1)-th
    # stair (by jumping one step) or from (n-2)-th stair (by jumping two steps).
    # So, this also mean that if we've already calc. ans. at (n-1)-th & (n-2)-th stair, we can just append 1s to all the
    # ways of (n-1)-th stair, and 2s to all the ways of (n-2)-th stair. And that would give us the ans. for current i.e.
    # n-th stair. Try below:
    # `0` ->
    # `1` -> 1
    # `2` -> 11, 2
    # `3` -> 111, 12, 21 (append 1s to ans. of stair (n-1) = (3-1) = `2` and 2s to ans. of stair (n-2) = (3-2) = `1`)
    # `4` -> 1111, 112, 121, 211, 22
    # And, in this question we just need to ans. the no. of ways not the actual ways, so we do not need to actually
    # append, but just count, and so ans(n) = ans(n-1) + ans(n-2). And that turns out to be the fibonacci sequence!
    # 1 -> 1
    # 2 -> 2
    # 3 -> 3
    # 4 -> 5
    # Want to read more? ->
    # https://leetcode.com/problems/climbing-stairs/solutions/3708750/4-method-s-beat-s-100-c-java-python-beginner-friendly
    # https://leetcode.com/problems/climbing-stairs/solutions/25299/basically-it-s-a-fibonacci

    n1, n2 = 0, 1
    for _ in range(n):
        n1, n2 = n2, n1+n2
    return n2
    # (https://leetcode.com/problems/climbing-stairs/solutions/25296/3-4-short-lines-in-every-language)

    # Interesting Fact: Fibonacci can also be formed using the golden ratio (1.618):
    # init             = 1
    # round(1 * 1.618) = 2
    # round(2 * 1.618) = 3
    # round(3 * 1.618) = 5
    # round(5 * 1.618) = 8
    # ...
    # Few interesting videos about Fibonacci: https://www.youtube.com/results?search_query=Fibonacci&sp=CAM%253D


# Similar Questions:
# https://leetcode.com/problems/fibonacci-number
