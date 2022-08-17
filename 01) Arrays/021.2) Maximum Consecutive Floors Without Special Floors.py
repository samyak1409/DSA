"""
https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors
"""


def max_consecutive(bottom: int, top: int, special: list[int]) -> int:
    """"""

    # 0.1) [TLE] Brute-force (Traverse & Count + HashSet): TC = O(top-bottom+1) {10e9}; SC = O(len(special)) {10e5}

    """
    special = set(special)  # new local var; for O(1) lookup
    maxi = curr = 0
    for floor in range(bottom, top+1):
        if floor in special:
            curr = 0  # reset
        else:
            curr += 1
            maxi = max(maxi, curr)
    return maxi
    """

    # 0.2) [MLE] Brute-force (Find Longest using HashSet): TC = O(top-bottom+1) {10e9};
    #                                                      SC = O(top-bottom+1-len(special)) {10e9-10e5}

    """
    # floors = set(range(bottom, top+1)).difference(special)
    special = set(special)  # new local var; for O(1) lookup
    floors = set()
    for floor in range(bottom, top+1):
        if floor not in special:
            floors.add(floor)
        else:
            special.remove(floor)

    # https://github.com/samyak1409/DSA/blob/d81aed952797c645eedf2032ba8537fafb3412a9/01%29%20Arrays/021%29%20Longest%20Consecutive%20Sequence.py#L74
    maxi = 0
    for floor in floors:
        if floor-1 not in floors:  # finding the smallest num of a consecutive sequence
            curr = 1
            while (floor := floor+1) in floors:
                curr += 1
            maxi = max(maxi, curr)
    return maxi
    """

    # 1) Optimal (Sorting Specials then Calc. Ranges): TC = O(n*log(n)); SC = O(n); n = len(special) <= 10e5
    # https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/discuss/2040152/JavaC%2B%2BPython-Sort
    # Say we have a pair of special floors (x, y) with no other special floors in between.
    # There are x - y - 1 consecutive floors in between them without a special floor.
    # Say there are n special floors.
    # After sorting special, we have answer = max(answer, special[i] – special[i – 1] – 1) for all 0 < i ≤ n.
    # However, there are two special cases left to consider: the floors before special[0] and after special[n-1].
    # To consider these cases, we have answer = max(answer, special[0] – bottom, top – special[n-1]).

    special = sorted(special)  # new local var

    maxi = 0
    for i in range(1, len(special)):
        maxi = max(maxi, special[i]-special[i-1]-1)  # floors b/w special floors
    return max(maxi, special[0]-bottom, top-special[-1])  # floors before & after first & last special floor
    # respectively
