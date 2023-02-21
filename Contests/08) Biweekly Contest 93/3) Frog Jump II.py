"""
https://leetcode.com/problems/frog-jump-ii
"""


def max_jump(stones: list[int]) -> int:
    """"""

    # One of the optimal strategies will be to jump to every stone.
    # Skipping just one stone in every forward jump and jumping to those skipped stones in backward jump can minimize
    # the maximum jump.

    # 1) Optimal (Calc the diff b/w every i-th and (i+2)-th stone): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/frog-jump-ii/solutions/2897948/java-c-python-max-a-i-a-i-2
    # So, at first, this question will sound like you have to calc for all the possible paths using DP, i.e. a medium to
    # hard Q., but, if we brainstorm for few minutes, we will realize that:
    # i)  Skipping any stone will not result in optimal answer, i.e. result in less cost by any way.
    #     Why? Because as "`stones` is sorted in a strictly increasing order", skipping any stone will only increase the
    #     cost! Let stones = [a, b, c, d] so a-d will always be > a-c > a-b.
    # ii) Now, one thing is clear that we will not skip any stones on the way. Now, second thing is how to choose stones
    #     optimally in order to minimize the cost i.e. = max jump, let's take [a, b, c, d] again and assume frog is on
    #     `a` initially, so the frog will have two options to travel:
    #     1st) a->c, c->d, d->b, b->a
    #     or
    #     2nd) a->b, b->d, d->c, c->a
    #     Now, something can be noticed, that from
    #     1st) the max jump will be either a->c or d->b
    #     (because c->d & b->a will always be < than d->b & a->c respectively)
    #     and
    #     2nd) the max jump will be either b->d or c->a
    #     (because a->b & d->c will always be < than c->a & b->d respectively)
    #     Note that: dist(a->b) == dist(b->a)
    #     => If we notice very carefully, both are giving the same answer, i.e. max(a->c, b->d)
    #     That is indeed correct if you think logically now!
    # So, turns out that we just need to calc the diff b/w all the `i`s and `i+2`s!

    """
    if len(stones) == 2:  # edge case
        return stones[1]-stones[0]
    ans = 0
    for i in range(len(stones)-2):
        ans = max(ans, stones[i+2]-stones[i])
    return ans
    """
    # Shortened:
    ans = 0
    for i in range(len(stones)-2):
        ans = max(ans, stones[i+2]-stones[i])
    return ans or stones[1]-stones[0]  # `or stones[1]-stones[0]` will handle the edge case `len(stones) == 2`
