"""
https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array
"""


def closet_target(words: list[str], target: str, start_index: int) -> int:
    """"""

    """
    n = len(words)
    ans = float('inf')
    
    for i in range(start_index, start_index+n):
        if words[(i + 1) % n] == target:
            ans = min(ans, abs(start_index-((i + 1) % n)))
        if words[(i - 1 + n) % n] == target:
            ans = min(ans, abs(start_index-((i - 1 + n) % n)))
        
    return ans
    """

    n = len(words)
    ans = float('inf')

    for i, word in enumerate(words):
        if word == target:
            ans = min(ans, abs(start_index-i), n-abs(start_index-i))

    return ans if ans != float('inf') else -1
