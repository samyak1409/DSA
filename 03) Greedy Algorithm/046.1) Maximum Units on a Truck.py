"""
https://leetcode.com/problems/maximum-units-on-a-truck
"""


def maximum_units(box_types: list[list[int]], truck_size: int) -> int:
    """"""

    # ~ Fractional Knapsack
    # https://github.com/samyak1409/DSA/blob/main/03%29%20Greedy%20Algorithm/046%29%20Fractional%20Knapsack.py

    # 1) Optimal (Greedy: Sort by Decreasing units_per_box): TC = O(n*log(n)); SC = O(n)
    # If we have space for at least one box, it's always optimal to put the box with the most units.
    # Sort the box types with the number of units per box non-increasingly.
    # Iterate on the box types and take from each type as many as you can.
    # https://leetcode.com/problems/maximum-units-on-a-truck/solutions/999125/java-python-3-sort-by-the-units-then-apply-greedy-algorithm
    # https://leetcode.com/problems/maximum-units-on-a-truck/solutions/1272564/short-easy-solution-w-explanation-greedily-select-max-units-box-ratio
    # Also, https://leetcode.com/problems/maximum-units-on-a-truck/solutions/2221148/why-not-dp-let-s-make-it-clear

    max_total_units = 0

    # Sort by decreasing order of units_per_box:
    for boxes, units_per_box in sorted(box_types, key=lambda box_type: box_type[1], reverse=True):
        if truck_size < boxes:
            boxes = truck_size
        truck_size -= boxes
        max_total_units += boxes * units_per_box
        if truck_size == 0:
            break

    return max_total_units


# Similar Questions:
# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks
