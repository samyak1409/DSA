"""
https://leetcode.com/problems/count-the-number-of-good-subarrays
"""


def count_good(nums: list[int], k: int) -> int:
    """"""

    # 1) Optimal (Sliding Window (till longest not-good sub_array for every i) + HashMap): TC = O(n); SC = O(n)
    # For a fixed index l, try to find the minimum value of index r, such that the subarray is not good.
    # When a number is added to a subarray, it increases the number of pairs by its previous appearances.
    # When a number is removed from the subarray, it decreases the number of pairs by its remaining appearances.
    # Maintain 2-pointers l and r such that we can keep in account the number of equal pairs.
    # https://leetcode.com/problems/count-the-number-of-good-subarrays/solutions/3052559/java-c-python-sliding-window
    # This is basically calculating opposite because it's easier. Very imp. concept!!

    from collections import Counter

    n = len(nums)
    pairs = 0
    freq = Counter()  # `Counter` for easy working with counts of nums
    rt = 0
    ans = 0

    for lt in range(n):

        try:  # EAFP
            while pairs+(new_pairs := freq[num_rt := nums[rt]]) < k:
                pairs += new_pairs  # add new pairs going to be made on coming of num_rt
                freq[num_rt] += 1  # increase its freq
                rt += 1  # move rt (expand window)
        except IndexError:  # if j move out
            break  # no more good subarrays would be there

        ans += n-rt  # rt is the first index from where all the next `rt`s will be the good subarray from lt

        # done with current num_lt, now shrink window
        freq[num_lt := nums[lt]] -= 1  # decrease its freq
        pairs -= freq[num_lt]  # subtract the pairs it was forming

    return ans
