"""
https://leetcode.com/problems/minimum-index-sum-of-two-lists
"""


def find_restaurant(list1: list[str], list2: list[str]) -> list[str]:
    """"""

    # 1) Optimal (HashMap): TC = O(n1+n2); SC = O(n1*x) {x: average string length}
    # https://leetcode.com/problems/minimum-index-sum-of-two-lists/solution

    index = {x: i for i, x in enumerate(list1)}  # hashmap for O(1) lookup; `restaurant: index` pair

    min_index_sum = float('inf')
    common = []
    for j, y in enumerate(list2):
        if (i := index.get(y)) is not None:  # => common interest found; `is not None` required because index can be = 0
            if (index_sum := i+j) < min_index_sum:  # => new best
                # common = [y]  # better ->
                common.clear(), common.append(y)
                min_index_sum = index_sum
            elif index_sum == min_index_sum:  # => tie
                common.append(y)
    return common
