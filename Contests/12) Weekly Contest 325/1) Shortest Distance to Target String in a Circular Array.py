"""
https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array
"""


def closet_target(words: list[str], target: str, start_index: int) -> int:
    """"""

    # 1) Optimal: TC = O(n); SC = O(1)

    # 1.1) Linearly traverse the array from start to end, and whenever the word == target, update the ans if required
    # with the min from either left moves or right moves:
    # https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/solutions/2947991/c-explanation-4-line-of-code
    # https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/solutions/2951631/one-pass

    """
    ans = float('inf')
    n = len(words)

    for i, word in enumerate(words):
        if word == target:
            # ans = min(ans, abs(i-start_index), n-abs(i-start_index))
            ans = min(ans, x := abs(i-start_index), n-x)

    return ans if ans != float('inf') else -1
    """

    # 1.2) From the `start_index` move left and right using Two Pointers linearly, as soon as the target is found, it
    # would be the ans as greedy approach works here:
    # You have two options, either move straight to the left or move straight to the right.
    # Find the first target word and record the distance.
    # Choose the one with the minimum distance.

    n = len(words)
    ans = float('inf')

    for i in range(n//2 + 1):
        if target in (words[start_index-i], words[(start_index+i) % n]):
            ans = min(ans, i)

    return ans if ans != float('inf') else -1
