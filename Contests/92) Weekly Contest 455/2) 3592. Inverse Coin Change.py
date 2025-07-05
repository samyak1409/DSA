"""
https://leetcode.com/problems/inverse-coin-change
"""


def find_coins(num_ways: list[int]) -> list[int]:
    """"""

    # Similar logic to one of the most famous DP problems: https://leetcode.com/problems/climbing-stairs
    # https://github.com/samyak1409/DSA/blob/main/LeetCode%20List%20-%20Top%20Interview%20Questions/1%29%20Easy/70.%20Climbing%20Stairs.py

    # 1) Optimal (DP): TC = O(n^2); SC = O(n)
    # Not very intuitive but Easy after knowing the solution.
    # Approach:
    # Observe that for the smallest denomination `c`, you must have `num_ways[c] == 1`.
    # Find the smallest `c > 0` with `num_ways[c] == 1` and append `c` to your answer list.
    # "Remove" that coin’s contribution by doing, for each `i` from `c` up to `n`: `num_ways[i] -= num_ways[i-c]`
    # Repeat: pick the next smallest `c` with `num_ways[c] == 1`, remove it, and so on.
    # At the end, if `num_ways` is all zeros, your answer is valid; otherwise, return an empty array.

    deno = []

    # For first iteration of `num_ways[i] -= num_ways[i-c]` to work:
    num_ways.insert(0, 1)

    # Iterate:
    for amount, ways in enumerate(num_ways):  # O(n)

        # Early exit: If all the prev ways are 0, and this way is >= 2 instead of 1, means no such set exists:
        if ways > 1:
            return []

        # Main:
        if amount and ways == 1:
            deno.append(amount)
            # Separate array to not make the change while iterating since we need the prev values to update next values:
            new = []
            # Start with the current coin:
            for i in range(amount, len(num_ways)):  # O(n)
                # Subtract ways due to this particular coin:
                new_ways = num_ways[i] - num_ways[i-amount]
                # Early exit: If any ways cnt go below 0, means no such set exists:
                if new_ways < 0:
                    return []
                # Save:
                new.append(new_ways)
            # Now, update:
            num_ways[amount:] = new

    return deno

    # The main thing, the proof to understand this solution is why/how `num_ways[i] - num_ways[i-amount]` works.
    # Works because `num_ways[i-amount]` contains all the total combinations of coins we can get `i-amount` amount.
    # Now, we subtract `num_ways[i-amount]` from current `num_ways[i]`, because if we're at `num_ways[i-amount]`, we can
    # add `amount` amount more to all the ways `num_ways[i-amount]`, and we'll get some ways to reach `num_ways[i-]`.
    # And, the most important thing is, when we do this for all the amounts, that subtract out all the intermediate
    # `num_ways[i-amount]` from `num_ways[i]`, and makes it 0.
    # [Not very intuitive]

    # More solutions: https://leetcode.com/problems/inverse-coin-change/solutions
