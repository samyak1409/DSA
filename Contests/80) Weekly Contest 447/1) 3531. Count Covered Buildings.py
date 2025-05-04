"""
https://leetcode.com/problems/count-covered-buildings
"""


def count_covered_buildings(n: int, buildings: list[list[int]]) -> int:
    """"""

    # First of all, the question was badly written:
    # "A building is covered if there is at least one building in all four directions: left, right, above, and below."
    # This basically means if a b2 is above a b1 (not necessarily in the same line).
    # However, the question actually wanted to be meant in the same line.
    # https://leetcode.com/problems/count-covered-buildings/description/comments/2966058

    # 1) Suboptimal (HashMap, Sort, HashSet: Group buildings): TC = O(n*log2(n)); SC = O(n)
    # Algo:
    # - Group buildings on the basis of vertical and horizontal lines (using two hashmaps).
    # - Sort each group, or maybe keep them sorted while inserting only.
    # - Now, all the buildings in each of the groups except the buildings on both ends are "covered" (vertically &
    # horizontally separately).
    # - Now, just find the intersection using HashSet to find buildings which are `covered` both vertically &
    # horizontally.

    # To keep the groups sorted:
    # `bisect.insert()` (only builtin option) -> actually takes O(n) not O(log2(n))
    # `sortedcontainers.SortedList().add()` (pip, but widely used) -> O(log2(n))

    """
    from collections import defaultdict
    from sortedcontainers import SortedList

    # For checking vertically & horizontally covered respectively:
    hm1, hm2 = defaultdict(SortedList), defaultdict(SortedList)
    # (Using `SortedList` directly instead of `list` so that we don't have to loop again for sorting each of the
    # groups.)
    # Group the buildings:
    for i, (x, y) in enumerate(buildings):  # (`i` to uniquely identify)
        hm1[x].add((y, i)), hm2[y].add((x, i))  # (imp. to add actual co-ordinate first so that sorting occurs using
        # that first)

    # Add vertically covered buildings to hashset:
    hs1 = set()
    for arr in hm1.values():
        hs1.update(i for _, i in arr[1:-1])

    # Add horizontally covered buildings to hashset:
    hs2 = set()
    for arr in hm2.values():
        hs2.update(i for _, i in arr[1:-1])

    # Return their intersection:
    return len(hs1.intersection(hs2))
    """

    # 2) Optimal (HashMap: Group only min and max): TC = O(n); SC = O(n)
    # https://leetcode.com/problems/count-covered-buildings/description/comments/2966134
    # Main idea: Instead of keeping the whole group sorted, just keep the min & max building in each of the groups.

    from collections import defaultdict

    # For checking vertically & horizontally covered respectively:
    hm1, hm2 = defaultdict(lambda: [float('inf'), float('-inf')]), defaultdict(lambda: [float('inf'), float('-inf')])
    # Save min, max:
    for x, y in buildings:
        hm1[x] = [min(hm1[x][0], y), max(hm1[x][1], y)]
        hm2[y] = [min(hm2[y][0], x), max(hm2[y][1], x)]

    # Count common buildings (buildings which are covered both vertically & horizontally):
    # cnt = 0
    # for x, y in buildings:
    #     if hm1[x][0] < y < hm1[x][1] and hm2[y][0] < x < hm2[y][1]:
    #         cnt += 1
    # return cnt
    # Or just:
    return sum(hm1[x][0] < y < hm1[x][1] and hm2[y][0] < x < hm2[y][1] for x, y in buildings)
