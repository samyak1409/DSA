"""
https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number
"""


def get_min_swaps(num: str, k: int) -> int:
    """"""

    # 1) Optimal ("Next Permutation" k Times + Calc. Swaps): TC = O(k*n + n^2); SC = O(n)
    # https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/discuss/1186818/C++-simple-solution-using-next_permutation

    # Helper Function: TC = O(n); SC = O(1)
    def next_permutation(nums: list[int]) -> None:
        """https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/003%29%20Next%20Permutation.py"""
        for i in range(len(nums)-1):  # finding first decreasing num (iterating from right to left)
            if nums[-i-2] < nums[-i-1]:
                decreasing_num = nums[-i-2]  # decreasing num found
                for j in range(i+1):  # finding number just larger than decreasing num (iterating from right to left)
                    if nums[-j-1] > decreasing_num:
                        just_larger = nums[-j-1]  # just larger number found
                        nums[-i-2], nums[-j-1] = just_larger, decreasing_num  # swapping the two
                        nums[-i-1:] = nums[-i-1:][::-1]  # reversing nums in the right
                        return  # stop

    # Find the next permutation of the given string k times. TC = O(k*n); SC = O(n)
    kth_perm = list(num)  # str to list because str is immutable
    for _ in range(k):
        next_permutation(kth_perm)

    # Try to move each element to its correct position and calculate the number of steps. TC = O(n^2); SC = O(n)
    num = list(num)  # str to list because str is immutable; new local var so that input array doesn't get modified
    swaps = 0
    for i in range(len(num)):  # easy, dry run to understand
        j = i
        while num[i] != kth_perm[j]:
            i += 1
        for _ in range(i-j):  # `i-j` -> distance
            num[i], num[i-1] = num[i-1], num[i]  # swapping (from right to left)
            swaps += 1
            i -= 1
    return swaps

    # Qn: WHY IS GREEDY APPROACH WORKING HERE?
    # First, we are not doing anything if the characters are at their original place.
    # Second, Since we are bringing character to its original position (if it was not), that was the minimum effort
    # (steps) we will have to put in since there is no other way of bringing it to original position with only adjacent
    # swaps.
    # And now we can apply same thing to the rest of the string. Plus we are swapping end to start, which shifts
    # characters towards the end, and ultimately close to their original position, because everything before that is
    # already in their original position.
