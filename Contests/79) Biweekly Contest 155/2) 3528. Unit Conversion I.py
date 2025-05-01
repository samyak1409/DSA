"""
https://leetcode.com/problems/unit-conversion-i
"""


def base_unit_conversions(cs: list[list[int]]) -> list[int]:
    """"""

    # -2) [WA] Suboptimal (Sort, For Loop): TC = O(n*log2(n)); SC = O(n)
    # Observations:
    # - For a pair [s, t, f], next ans, ans[t] = ans[s] * f
    # - Since for ans[t], we need ans[s] to be filled already, sort using (s, t).

    """
    MOD = 10**9 + 7
    # Init `ans` arr:
    ans = [0] * (len(cs)+1)
    ans[0] = 1
    # Sort by (s, t), and fill answers:
    for s, t, f in sorted(cs):
        ans[t] = (ans[s]*f) % MOD
    return ans
    """

    # WA
    # Input
    # conversions = [[0,3,4],[3,2,7],[2,1,12]]
    # Output
    # [1,0,28,4]
    # Expected
    # [1,336,28,4]
    # Reason: `s` <-> `t` linking is not done in sequential order, in the above case, `0` is linked to `3`, even when
    # `1` is there.
    # Let's try with the order as given in input.

    # -1) [WA] Optimal (Just For Loop): TC = O(n); SC = O(n)
    # Same as `-2)`, just trying without sorting.

    """
    MOD = 10**9 + 7
    # Init `ans` arr:
    ans = [0] * (len(cs)+1)
    ans[0] = 1
    # Fill answers:
    for s, t, f in cs:
        ans[t] = (ans[s]*f) % MOD
    return ans
    """

    # WA
    # Input
    # conversions = [[2,3,4],[1,2,2],[0,1,3]]
    # Output
    # [1,3,0,0]
    # Expected
    # [1,3,6,24]
    # Reason: Input is not given in sequential order such that it could be processed directly. (Neither we can sort as
    # mentioned in `-2`.)
    # Hence, we'd to put actual checks before saving a `t` that `s` is already there or not. If not, we need to recurse
    # and first process `s` first.

    # 1) Optimal (Recursion, HashMap): TC = O(n); SC = O(n)

    # Pre-process: Create a mapping for direct access using `t`, hashmap also provides O(1) time:
    hm = {t: (s, f) for s, t, f in cs}
    # (Note that array as a hashmap could've been also used here.)
    # print(hm)  # debug

    # Recursive Function:
    # This is the main part of this algorithm:
    # To save answer for `t`, `s` should already be there, if not, first recurse and save for `s` first.
    def r(t: int) -> None:
        s, f = hm[t]
        if not ans[s]:
            r(t=s)
        ans[t] = (ans[s]*f) % MOD

    MOD = 10**9 + 7
    # Init `ans` arr:
    ans = [0] * (len(cs)+1)
    ans[0] = 1
    # Iterate on `ans` arr:
    for i in range(1, len(ans)):
        # Only process an index if answer is not already saved (by recursion while saving other answers):
        if not ans[i]:
            r(t=i)
    return ans

    # This can also be solved using DFS/BFS (Graph/Tree), as mentioned in:
    # Official hints:
    # - The input is a weighted directed tree rooted at 0.
    # - Launch a BFS from node 0 and multiply the weights on the path.
    # And solutions page: https://leetcode.com/problems/unit-conversion-i/solutions
    # Check the last two prompts of this chat: https://chatgpt.com/share/6813c80d-9a94-800a-9d7f-51be1d92cfff
    # Summary:
    # Both solutions achieve the same goal with similar time and space complexities, but the key difference lies in how
    # the data is structured and how the recursion is handled:
    # Your solution uses a hashmap for direct access to conversions, whereas I used an adjacency list to represent the
    # tree structure.
    # Both approaches use recursion and memoization, but in your case, recursion is triggered within the iteration over
    # the ans array, while in my approach, recursion is triggered from a DFS call.
    # Both are valid solutions, but your approach is slightly more compact, using a single hashmap to store conversion
    # relationships, while mine uses a more explicit graph traversal structure.
