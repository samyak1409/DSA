"""
https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum
"""


def num_of_subarrays(arr: list[int]) -> int:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/023%29%20Count%20Subarrays%20with%20Given%20XOR.py.

    # 1) Optimal (Prefix Sum & HashMap): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/discuss/754743/JavaC++Python-Prefix-Sum

    """
    from collections import Counter
    frequency = Counter()  # Counter for easy working with counts
    prefix_sum = 0
    frequency[prefix_sum] = 1  # init
    count = 0
    for num in arr:
        prefix_sum += num
        mod = prefix_sum % 2  # even_sum => mod = 0; odd_sum => mod = 1
        count += frequency[1-mod]  # ✅✅ if a pair is made with a prefix_sum, then it will also satisfy with any &
        # every previous occurrences of that particular prefix_sum
        frequency[mod] += 1  # add/update frequency of even/odd sum
        count %= 1_000_000_007  # "Since the answer can be very large, return it modulo 10^9 + 7."
    return count
    """
    # Notice that as the hashmap will have 0 and 1 at most as keys, we can write the algo using 2 int vars only instead 
    # of the hashmap:
    prefix_sum = 0
    even_sums, odd_sums = 1, 0  # init
    count = 0
    for num in arr:
        prefix_sum += num
        mod = prefix_sum % 2  # mod = 0 => even sum; mod = 1 => odd sum
        if mod:  # => odd_sum
            count += even_sums
            odd_sums += 1  # add/update frequency of odd sum
        else:  # => even_sum
            count += odd_sums
            even_sums += 1  # add/update frequency of even sum
        count %= 1_000_000_007  # "Since the answer can be very large, return it modulo 10^9 + 7."
    return count
