"""
https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1
"""


def minimum_platform(n: int, arr: list[int], dep: list[int]):
    """"""

    # 1) Sub-Optimal (Sort Both Arrays Individually, then Traverse using Two Pointers): TC = O(n*log(n)); SC = O(n)
    # Why will sorting the arrays individually work?
    # Because we don't care about which train arrive or depart, we just need the maximum number of platforms occupied
    # by the trains at any particular point of time!
    # Video Explanation: https://youtu.be/dxVcMDI7vyI

    """
    # Get Sorted Arrays:
    arr, dep = sorted(arr), sorted(dep)

    # Merge Sort's Merge Part Style Traversal (using Two Pointers):
    i = j = 0
    platforms = 0
    ans = 0
    while i < n:  # `and j < n`: not required because as soon as `i` goes out of bound, it does not matter where the
        # `j` is because our answer depends on train's arrival, as at train arrival only, we may need one more platform
        if arr[i] <= dep[j]:
            platforms += 1
            ans = max(ans, platforms)
            i += 1
        else:  # (if arr[i] > dep[j])
            platforms -= 1
            j += 1

    return ans
    """

    # 1.1) Same Idea, but More-Intuitive and Easier-To-Sink-In Implementation:
    # Using only single array not two, and putting both the times in that array with attr 'a' or 'd', then sorting them,
    # and then traversing one by one.

    """
    from itertools import repeat, chain

    platforms = 0
    ans = 0
    for time, attr in sorted(chain(zip(arr, repeat('a')), zip(dep, repeat('d')))):
        if attr == 'a':  # a for arrival, at this particular time a train came, so it will use a platform
            platforms += 1
            ans = max(ans, platforms)
        else:  # (if attr == 'd', d for departure), at this particular time a train went, so it will leave a platform
            platforms -= 1

    return ans
    """

    # 2) Optimal (Range Caching!!!! (Prefix Sum)): TC = O(n); SC = O(1)
    # This solution is improved implementation of above idea!
    # Video Explanation: https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1 > Editorial > Video

    # Init arr on which we'll perform range caching:
    times = [0] * (2360+1)  # all possible times (0000 ≤ A[i] ≤ D[i] ≤ 2359)

    # Traverse train times and cache them into the arr:
    for at, dt in zip(arr, dep):  # O(n)
        times[at] += 1
        times[dt+1] -= 1

    # Prefix Sum to get the max platforms in use at a particular point of time:
    ans = 0
    for i in range(1, len(times)):  # O(1)
        times[i] += times[i-1]
        ans = max(ans, times[i])

    return ans

    # This question was dope!!
