"""
https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i
"""


def max_rectangle_area(points: list[list[int]]) -> int:
    """"""

    # 0) Brute-force (Trying All Permutations): TC = O(nP4 * n) {nP4 = 10P4 = 5040}; SC = O(1)
    # Since `1 <= points.length <= 10`, we can just try to calculate the area for all permutations.

    """
    from itertools import permutations

    ans = -1
    # Loop on all permutations:
    for perm in permutations(points, r=4):  # O(nP4)
        # print(perm)  # debugging
        # Now, what we'd do is, we would make sure following:
        # perm[0]: bottom-left
        # perm[1]: bottom-right
        # perm[2]: top-left
        # perm[3]: top-right
        # And discard all other permutations which doesn't satisfy this.
        if perm[0][0] <= perm[1][0] and perm[0][1] <= perm[2][1]:  # make sure perm[0] is bottom-left point
            if perm[0][1] == perm[1][1] and perm[0][0] == perm[2][0]:  # check "Has its edges parallel to the axes."
                if perm[3] == [perm[1][0], perm[2][1]]:  # make sure rectangle can be formed
                    # Check "Does not contain any other point inside or on its border.":
                    btm_lt, btm_rt, top_lt = perm[:3]
                    skip = False
                    for x, y in filter(lambda point: point not in perm, points):  # O(n)
                        if (btm_lt[0] <= x <= btm_rt[0]) and (btm_lt[1] <= y <= top_lt[1]):
                            skip = True
                    if not skip:
                        ans = max(ans, (btm_rt[0]-btm_lt[0])*(top_lt[1]-btm_lt[1]))
    return ans
    """

    # 1) Sub-optimal (Trying All Combinations): TC = O(nC4 * n) {nC4 = 10C4 = 210}; SC = O(1)
    # We can optimize `0)` as we're only considering all the permutations just because we don't know which point is
    # btm_lt, btm_rt, top_lt, top_rt. If we sort the `comb` list, we'd just get the points in following order:
    # btm_lt, top_lt, btm_rt, top_rt.
    # - Why? Because Python sort has the following functionality:
    #   "In the case of a nested list (a list of lists), the sorting will happen by comparing the first elements of each
    #   sublist. If the first elements are equal, it proceeds to the second elements, and so on, until the lists are
    #   sorted."
    # All the other implementation is same as above.

    from itertools import combinations

    ans = -1
    # Loop on all combinations:
    for comb in combinations(points, r=4):  # O(nC4)
        # print(comb)  # debugging
        # We directly get the points in order using sort:
        btm_lt, top_lt, btm_rt, top_rt = sorted(comb)
        if btm_lt[1] == btm_rt[1] and btm_lt[0] == top_lt[0]:  # check "Has its edges parallel to the axes."
            if top_rt == [btm_rt[0], top_lt[1]]:  # make sure rectangle can be formed
                # Check "Does not contain any other point inside or on its border.":
                skip = False
                for x, y in filter(lambda point: point not in comb, points):  # O(n)
                    if (btm_lt[0] <= x <= btm_rt[0]) and (btm_lt[1] <= y <= top_lt[1]):
                        skip = True
                if not skip:
                    ans = max(ans, (btm_rt[0]-btm_lt[0])*(top_lt[1]-btm_lt[1]))
    return ans

    # Other solutions:

    # Hint 1: If `(x1, y1)` and `(x2, y2)` are two opposite corners of a rectangle, then the other two would be
    # `(x1, y2)` and `(x2, y1)`.
    # Hint 2: Fix two points and find the other two using a set data structure.
    # Hint 3: After determining the rectangle, iterate through the array of points to ensure no point lies on the
    # rectangle’s border or within its interior.

    # https://leetcode.com/problems/minimum-area-rectangle
