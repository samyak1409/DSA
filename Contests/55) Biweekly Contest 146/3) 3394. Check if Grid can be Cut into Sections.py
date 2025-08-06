"""
https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections
"""


def check_valid_cuts(n: int, rectangles: list[list[int]]) -> bool:
    """"""

    # 1) Optimal (Greedy: Sort by start): TC = O(r*log(r)); SC = O(r) {r: len(rectangles)}
    # Sort the rectangles for horizontally and check if at least two valid cuts can be made. Do the same for vertically.

    # "rectangles[i] is in the form [start_x, start_y, end_x, end_y]"

    # 1.1):
    """
    # For horizontal: sort by start height:
    cuts = 0
    sorted_rects = sorted(rectangles, key=lambda rect: rect[1])
    curr_max_end = sorted_rects[0][3]
    for i in range(1, len(sorted_rects)):
        rect = sorted_rects[i]
        # If the next rectangle start is >= current max end among all the previous rectangles, means we can make a cut:
        # (valid cut condition: "Every rectangle belongs to exactly one section.")
        if rect[1] >= curr_max_end:
            cuts += 1
            if cuts == 2:
                return True
        # Tracking the max end of currently seen rectangles:
        curr_max_end = max(curr_max_end, rect[3])

    # For vertical: sort by start width:
    cuts = 0
    sorted_rects = sorted(rectangles, key=lambda rect: rect[0])
    curr_max_end = sorted_rects[0][2]
    # If the next rectangle start is >= current max end among all the previous rectangles, means we can make a cut:
    # (valid cut condition: "Every rectangle belongs to exactly one section.")
    for i in range(1, len(sorted_rects)):
        rect = sorted_rects[i]
        if rect[0] >= curr_max_end:
            cuts += 1
            if cuts == 2:
                return True
        # Tracking the max end of currently seen rectangles:
        curr_max_end = max(curr_max_end, rect[2])

    # If valid cuts can't be made:
    return False
    """

    # 1.2) We can also have the first rect in the `for` loop as well by initializing `curr_max_end` with `0`
    # ("0 <= rectangles[i][0] < rectangles[i][2] <= n; 0 <= rectangles[i][1] < rectangles[i][3] <= n"):

    """
    # For horizontal: sort by start height:
    cuts = -1
    sorted_rects = sorted(rectangles, key=lambda rect: rect[1])
    curr_max_end = 0
    for i in range(len(sorted_rects)):
        rect = sorted_rects[i]
        # If the next rectangle start is >= current max end among all the previous rectangles, means we can make a cut:
        # (valid cut condition: "Every rectangle belongs to exactly one section.")
        if rect[1] >= curr_max_end:
            cuts += 1
            if cuts == 2:
                return True
        # Tracking the max end of currently seen rectangles:
        curr_max_end = max(curr_max_end, rect[3])

    # For vertical: sort by start width:
    cuts = -1
    sorted_rects = sorted(rectangles, key=lambda rect: rect[0])
    curr_max_end = 0
    # If the next rectangle start is >= current max end among all the previous rectangles, means we can make a cut:
    # (valid cut condition: "Every rectangle belongs to exactly one section.")
    for i in range(len(sorted_rects)):
        rect = sorted_rects[i]
        if rect[0] >= curr_max_end:
            cuts += 1
            if cuts == 2:
                return True
        # Tracking the max end of currently seen rectangles:
        curr_max_end = max(curr_max_end, rect[2])

    # If valid cuts can't be made:
    return False
    """

    # 1.3) Using function:

    # Helper function:
    def check(st: int, end: int) -> bool:
        # For horizontal: sort by start height / For vertical: sort by start width:
        cuts = 0
        sorted_rects = sorted(rectangles, key=lambda r: r[st])
        curr_max_end = sorted_rects[0][end]
        for i in range(1, len(sorted_rects)):
            rect = sorted_rects[i]
            # If the next rectangle start is >= current max end among all the previous rectangles, means we can make a
            # cut:
            # (valid cut condition: "Every rectangle belongs to exactly one section.")
            if rect[st] >= curr_max_end:
                cuts += 1
                if cuts == 2:
                    return True
            # Tracking the max end of currently seen rectangles:
            curr_max_end = max(curr_max_end, rect[end])
        # If valid cuts can't be made:
        return False

    return check(1, 3) or check(0, 2)
