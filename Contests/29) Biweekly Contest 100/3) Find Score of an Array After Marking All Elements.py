"""
https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements
"""


def find_score(nums: list[int]) -> int:
    """"""

    # Try simulating the process of marking the elements and their adjacent.
    # If there is an element that was already marked, then you skip it.

    # 1) Optimal (Sort; HashSet/Lookup-Array): TC = O(n*log(n)); SC = O(n)
    # https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/solutions/3312034/python-simulation

    """
    score = 0
    marked = set()  # hashset for O(1) lookup
    # Loop on nums sorted in ascending order:
    # "Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest
    # index."
    # "Repeat until all the array elements are marked."
    for num, i in sorted((num, i) for i, num in enumerate(nums)):
        if i not in marked:
            score += num  # "Add the value of the chosen integer to score."
            marked.update({i-1, i, i+1})  # "Mark the chosen element and its two adjacent elements if they exist."
    return score
    """
    # Actually, we don't need HashSet, we can use just an array, as we're only storing the indices, we can achieve O(1)
    # lookup here also.
    score = 0
    marked = [0] * (len(nums)+2)  # first & last indices are just a placeholder for handling i=0 & i=n-1 respectively
    # Loop on nums sorted in ascending order:
    # "Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest
    # index."
    # "Repeat until all the array elements are marked."
    for num, i in sorted((num, i) for i, num in enumerate(nums, start=1)):  # `start=1`: because index 0 is placeholder
        if not marked[i]:
            score += num  # "Add the value of the chosen integer to score."
            marked[i-1] = marked[i] = marked[i+1] = 1  # "Mark the chosen element and its two adjacent elements if they
            # exist."
    return score
