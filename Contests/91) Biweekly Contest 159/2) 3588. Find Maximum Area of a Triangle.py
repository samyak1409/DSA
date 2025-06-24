"""
https://leetcode.com/problems/find-maximum-area-of-a-triangle
"""


def max_area(coords: list[list[int]]) -> int:
    """"""

    # 1) Optimal (Geometry, HashMap): TC = O(n); SC = O(n)
    # Observations:
    # - Area of triangle = 1/2 * base * perpendicular height (shortest dist between the point opposite to the base to
    #   the base line, consider the base line extending to the infinity)
    # - Considering the side of the triangle which we need parallel to the two axes (plural of axis) as the base line,
    #   we need to find calc two things:
    #   i) the max base line for every fix `x` for vertical line and for every fix `y` for horizontal lines
    #   ii) extreme `x_min`, `x_max`, `y_min`, `y_max` points which would be the 3rd point of the triangle, the point
    #       opposite to the base line.

    from collections import defaultdict

    # k: v = x: [y_min_on_x, y_max_on_x] OR y: [x_min_on_y, x_max_on_y]
    vert, hori = defaultdict(lambda: [float('inf'), 0]), defaultdict(lambda: [float('inf'), 0])
    # Overall min max:
    x_min, x_max, y_min, y_max = float('inf'), 0, float('inf'), 0

    # Calc min max:
    for x, y in coords:
        vert[x][:] = min(vert[x][0], y), max(vert[x][1], y)
        hori[y][:] = min(hori[y][0], x), max(hori[y][1], x)
        x_min, x_max, y_min, y_max = min(x_min, x), max(x_max, x), min(y_min, y), max(y_max, y)

    # print(vert); print(hori); print(x_min, x_max, y_min, y_max)  # debug

    ans = 0

    # Calc ans:
    for x, (y_min_on_x, y_max_on_x) in vert.items():
        ans = max(ans, (y_max_on_x-y_min_on_x) * max(x-x_min, x_max-x))  # base * height
    for y, (x_min_on_y, x_max_on_y) in hori.items():
        ans = max(ans, (x_max_on_y-x_min_on_y) * max(y-y_min, y_max-y))  # base * height

    return ans or -1  # "If no such triangle exists, return -1."
