"""
https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings
"""


def count_cells(grid: list[list[str]], pattern: str) -> int:
    """"""

    # 0) [TLE] Brute-force (Flatten the grid, save indices, find common using hashset): TC = O((m*n)^2); SC = O(m*n)
    # (571/573 testcases passed)

    """
    # Get complete horizontal str (flattened):
    hs = []
    for row in grid:
        hs.extend(row)
    hs = ''.join(hs)
    # print(hs)  # debug

    # Get complete vertical str (flattened):
    m, n = len(grid), len(grid[0])
    vs = []
    vi = []  # this is for keeping the indices same through horizontal and vertical strs
    for c in range(n):
        vs.extend([grid[r][c] for r in range(m)])
        vi.extend([(r*n)+c for r in range(m)])
    vs = ''.join(vs)
    # print(vs); print(vi)  # debug

    # Now, just add the indices to the hashset where pattern matches:
    # For horizontal str:
    str_len, p = m*n, len(pattern)
    i = 0
    hc = set()
    while i < str_len:
        # Try to find the pattern starting from `i`th index in our str:
        try:
            i = hs.index(pattern, i)
        # If no more matches:
        except ValueError:
            break
        # If a match is found, add the indices to the hashset:
        else:
            i_ = i
            for _ in range(p):
                hc.add(i)
                i += 1
            # Continue with next `i` (reason of TLE):
            i = i_ + 1
    # print(hc)  # debug

    # For vertical str:
    i = 0
    vc = set()
    while i < str_len:
        # Try to find the pattern starting from `i`th index in our str:
        try:
            i = vs.index(pattern, i)
        # If no more matches:
        except ValueError:
            break
        # If a match is found, add the indices to the hashset:
        else:
            i_ = i
            for _ in range(p):
                vc.add(vi[i])
                i += 1
            # Continue with next `i` (reason of TLE):
            i = i_ + 1
    # print(vc)  # debug

    # Finally, return the intersection of the two hashsets:
    return len(hc.intersection(vc))
    """

    # 1) Optimal (String Hashing or Pattern Matching Algo): TC = O(m*n); SC = O(m*n)
    # Just include KMP or Z Algo in the above solution.

    pass
