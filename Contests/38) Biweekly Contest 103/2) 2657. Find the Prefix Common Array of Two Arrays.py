"""
https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays
"""


def find_the_prefix_common_array(a: list[int], b: list[int]) -> list[int]:
    """"""

    # Consider keeping a frequency array that stores the count of occurrences of each number till index i.
    # If a number occurred two times, it means it occurred in both A and B since they’re both permutations so add one to
    # the answer.

    # 0) Brute-force (HashSet): TC = O(n^2); SC = O(n)

    """
    hs = set()  # SC = O(n)
    for i in range(len(a)):  # O(n*n)
        hs.add(a[i])
        '''
        common = 0
        for j in range(i+1):  # O(n)
            if b[j] in hs:
                common += 1
        yield common
        '''
        # One liner:
        yield sum(b[j] in hs for j in range(i+1))  # O(n)
    """

    # 1.1) Optimal (Frequency Array): TC = O(n); SC = O(n)
    # We can use a HM, but as we need to track from 1 to n, Frequency Array is better.

    """
    freq = [0] * (n := len(a))  # init; SC = O(n)
    common = 0
    for i in range(n):  # O(n)
        for num in (a[i], b[i]):  # O(1)
            freq[num-1] += 1  # (`-1` coz indices)
            common += freq[num-1] == 2  # ++ if freq == 2
        yield common
    """

    # 1.2) Optimal (HashSet): TC = O(n); SC = O(n)
    # We can also do it in O(n) w/ a HashSet, as the most the no. will occur is 2,
    # When occurring 1st time, it won't be in the HS, so not common yet, add in the HS.
    # When occurring the 2nd (last) time, it'd be in the HS, so it's common now! (Adding in the HS would've no effect.)

    hs = set()  # SC = O(n)
    common = 0
    for i in range(len(a)):  # O(n)
        for num in (a[i], b[i]):  # O(1)
            common += num in hs  # check if already added
            hs.add(num)  # then add
        yield common
