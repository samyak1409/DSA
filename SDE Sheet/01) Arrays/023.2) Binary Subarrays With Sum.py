"""
https://leetcode.com/problems/binary-subarrays-with-sum
"""


def num_subarrays_with_sum(nums: list[int], goal: int) -> int:
    """"""

    # This problem is just a sub-problem of https://leetcode.com/problems/subarray-sum-equals-k.

    # 1) Time-Optimal (Prefix Sum & HashMap): TC = O(n); SC = O(n)
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/023.1%29%20Subarray%20Sum%20Equals%20K.py

    """
    from collections import Counter
    frequency = Counter()  # Counter for easy working with counts
    prefix_sum = 0
    frequency[prefix_sum] = 1  # initializing with `prefix_sum: 1` because:
    # dry run the algo with input (nums=[6, 6], x=6), you'll get the answer.
    count = 0
    for num in nums:
        prefix_sum += num
        count += frequency[prefix_sum-goal]  # ✅✅ if a pair is made with a prefix_sum, then it will also satisfy with
        # any & every previous occurrences of that particular prefix_sum
        frequency[prefix_sum] += 1  # add/update frequency of prefix_sum
    return count
    """

    # 2) Optimal (Sliding Window): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/binary-subarrays-with-sum/discuss/186683/C++JavaPython-Sliding-Window-O(1)-Space
    # Explanation:
    # "This is my understanding of the sliding window solution. If there is anything wrong, please point it out.
    # atMost(A, S) counts the number of the subarrays of `A` the sum of which is at most (less than or equal to) `S`.
    # Therefore, we can use atMost(A, S) - atMost(A, S-1) to get the number of the subarrays the sum of which is
    # exactly `S`.
    # In the atMost function, the `i` to `j` window represents the subarrays. We use the `j` pointer to expand the
    # window, when the sum of all numbers in the window is bigger than `S`, it's time for us to move the `i` pointer to
    # shorten the window. Through this process, we can count the number of the subarrays."
    # -https://leetcode.com/problems/binary-subarrays-with-sum/solutions/186683/c-java-python-sliding-window-o-1-space/comments/950969

    # Helper Function:
    def at_most(target: int) -> int:
        """
        Sliding Window to find the total number of subarrays with at most `target` sum, in the array consisting only
        of positive integers.
        """
        if target < 0:  # we won't find any subarray with -ve `target` because our array only contains +ves
            return 0
        count, i, curr = 0, -1, 0
        for j in range(len(nums)):
            curr += nums[j]  # extend window
            while curr > target:  # while sum is > than target, shrink window
                curr -= nums[i := i+1]
            count += j-i  # imp: this looks like we're just adding the len of the subarray to the count, yes we're,
            # because we are counting the subarrays with at most `target` sum, so, total `j-i` subarrays will satisfy
            # this condition.
            # https://leetcode.com/problems/binary-subarrays-with-sum/solutions/186683/c-java-python-sliding-window-o-1-space/comments/1220229
            # you might also ask if this is the case, then shouldn't it be `n*(n+1) // 2` where n = j-i? instead of just
            # `j-i`, because the total number of subarrays in an array is `n*(n+1) // 2`, to understand this, revise
            # how for input ([0, 0, 0, 0, 0], 0), the output is 15.
            # Basically, other subarrays will be covered in other iterations, so in a single iteration, we only count
            # "len of the subarray" and not "the total number of subarrays in the subarray".
        return count

    return at_most(goal) - at_most(goal-1)

    # Note that directly finding the answer without using the `at_most` technique and by using
    # Three Pointer Sliding Window
    # (https://leetcode.com/problems/binary-subarrays-with-sum/solutions/186800/binary-subarrays-with-sum/#approach-3-three-pointer)
    # looks complicated, so didn't do it that way.
