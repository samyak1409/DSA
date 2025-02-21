"""
https://leetcode.com/problems/assign-elements-to-groups-with-constraints
"""


def assign_elements(groups: list[int], elements: list[int]) -> list[int]:
    """"""

    # 0) Brute-force (Nested Loop with Memo): TC = O(m*n); SC = O(m) {m = len(groups), n = len(elements)}

    """
    ans = []
    memo = {}  # little optimization over bare brute-force (nested loop), but the worst case TC stays the same (worst
    # case: all nums are unique in groups)
    for g in groups:
        # If this `g` has seen before, use memo ans:
        if j := memo.get(g):
            ans.append(j)
            continue
        # Else find ans:
        for j, el in enumerate(elements):
            if g % el == 0:
                ans.append(j)
                memo[g] = j
                break
        else:
            ans.append(-1)
            memo[g] = -1
    return ans
    """

    # 1) Optimal (Sieve of Eratosthenes): TC = O(m*log(m)); SC = O(m) {m = len(groups), n = len(elements)}
    # Observation: Since `1 <= elements[j] <= 10^5`, we can build an array as a hashmap like we do in Sieve of
    # Eratosthenes.
    # The arr indices would work as nums in `groups`, and the values at those indices would be the `j`.
    # Time complexity:
    # https://leetcode.com/problems/assign-elements-to-groups-with-constraints/solutions/6396012/python-beat-100-o-nlogn/comments/2845309

    arr = [-1] * (arr_len:=max(groups)+1)  # (`+1` due to 0-indexed)
    # Preprocessing: filling the arr:
    for j, el in enumerate(elements):  # O(m*log(m))
        # Start the filling process for this `el` only if `el` is occurring for the first time:
        if el < arr_len and arr[el] == -1:  # (one TLE due to overseeing this)
            multiple = el  # first multiple
            while multiple < arr_len:
                # Only assign `j` if `arr[multiple]` is not assigned with some previous `j` (since "assign the element
                # with the smallest index `j`"):
                if arr[multiple] == -1:
                    arr[multiple] = j
                multiple += el  # now next multiple

    # Return the ans using the pre-processed hashmap:
    return [arr[g] for g in groups]

    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Segmented_sieve
    # https://www.linkedin.com/in/mudit-singhal-msa91
