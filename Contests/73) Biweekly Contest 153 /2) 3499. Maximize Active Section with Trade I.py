"""
https://leetcode.com/problems/maximize-active-section-with-trade-i
"""


def max_active_sections_after_trade(s: str) -> int:
    """"""

    # 1) Time-optimal ('0' -> -1, '1' -> 1; Prefix, Suffix Arr): TC = O(n); SC = O(n)
    # My intuitive approach:
    # If we convert `0` -> `-1` in `s`, and add up the same contiguous parts:
    # `1000100` becomes `[+1, -3, +1, -2]`
    # Next, since first we need to change contiguous 1s to 0s, in our case any +ve to -ve,
    # Loop through `[+1, -3, +1, -2]` and find the max sum we can get by changing one +ve to -ve
    # In this example, it'd be `abs(-3) + +1 + abs(-2)` = `6`, and we also need to consider remaining +ves from the arr,
    # so `6 + +1` (`+1`: arr[0]) = `7` = answer.

    """
    arr = []
    # Create the alt sign arr:
    for c in s:
        c = -1 if c == '0' else 1  # '0' -> -1; '1' -> 1
        if not arr or arr[-1]*c < 0:  # `arr[-1]*c < 0`: check if signs are different
            arr.append(c)
        else:
            arr[-1] += c
    # print(arr)  # debug

    # Build prefix & suffix arrays for +1s:
    # e.g.
    # arr =     [+1, -3, +1, -2]
    # pre = [ 0, +1, +1, +2, +2]
    # suf       [+2, +1, +1,  0,  0]
    pre = [0]
    for x in arr:
        pre.append(pre[-1] + max(x, 0))
    suf = [0]
    for x in arr[::-1]:
        suf.append(suf[-1] + max(x, 0))
    suf.reverse()
    # print(pre, suf)  # debug

    ans = 0
    # Now, calc the ans:
    for i in range(1, len(arr)-1):  # keeping the `i` in the middle
        # We only need to calc when our middle val is +ve:
        if arr[i] > 0:
            # Prefix + (`-ve val` + `+ve val` + `-ve val`) + Suffix:
            ans = max(ans, pre[i-1] + (-arr[i-1]+arr[i]-arr[i+1]) + suf[i+2])
    # Return ans:
    return ans or pre[-1]  # `or pre[-1]`: edge case: if we didn't enter the above `if` condition even once
    # `pre[-1]` = total 1s which were already there
    """

    # Penalties in contest:
    # 1 WA due to leaving the 1s which are not in the window but are already there in the arr.
    # 1 TLE due to re-looping to calc no. of 1s without using prefix, suffix.

    # 2) Optimal (Sliding Window): TC = O(n); SC = O(1)
    # Same base idea as `1)`, better implementation.
    # i. No need of '0' -> -1, '1' -> 1, we can loop on the original `s` only to calc the max window.
    # ii. No need of Prefix, Suffix Arr, we can calc the max window without the 1s in it, and then add the total 1s
    # from `s` to max window size.
    # Approach (very easy):
    # If you carefully take a look at the operations we've to perform in one trade, it's just equal to finding the max
    # window size of: 0s, 1s, 0s
    # And then we just need to add the 1s which were already there in `s`.

    prev_0s = curr_0s = total_1s = max_window = 0
    # (note: `max_window` will not count the 1s in it, only 0s from left and right)
    # Sliding window:
    for i in range(len(s)):
        # When 0 comes:
        if s[i] == '0':
            curr_0s += 1
        # When 1 comes:
        else:
            total_1s += 1
            # If 1 has come after 0s:
            if curr_0s:
                # If we've got a window of pattern: 0s, 1s, 0s
                if prev_0s:
                    # Calc. the window size (without 1s):
                    max_window = max(max_window, prev_0s+curr_0s)
                # Move curr 0s to prev:
                prev_0s, curr_0s = curr_0s, 0

    # If s[-1] == '0', we need to calc the last window of pattern: 0s, 1s, 0s:
    if curr_0s and prev_0s:
        max_window = max(max_window, prev_0s+curr_0s)

    # Add the total 1s to the max window size:
    return max_window + total_1s
