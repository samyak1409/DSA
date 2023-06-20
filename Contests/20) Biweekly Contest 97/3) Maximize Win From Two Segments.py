"""
https://leetcode.com/problems/maximize-win-from-two-segments
"""


def maximize_win(prize_positions: list[int], k: int) -> int:
    """"""

    # Try solving the problem for one interval.
    # Using the solution with one interval, how can you combine that with a second interval?

    # 1) Optimal: TC = O(n); SC = O(n)

    # 1.1) Sliding Window + Prefix & Suffix Array:
    # Same logic like: `023.4) Find Two Non-overlapping Sub-arrays Each With Target Sum.py`
    # (https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/023.4%29%20Find%20Two%20Non-overlapping%20Sub-arrays%20Each%20With%20Target%20Sum.py)
    # https://leetcode.com/problems/maximize-win-from-two-segments/solutions/3141910/prefix-count-o-n-sliding-window-with-image

    n = len(prize_positions)

    # Calculate Prefix Array:
    prefix = [0]
    lt = 0
    for rt in range(n):
        while prize_positions[rt]-prize_positions[lt] > k:  # while segment_length > k
            lt += 1  # shrink window
        prefix.append(max(prefix[-1], rt-lt+1))  # keep max till this index
    # print(prefix)  #debugging

    # Calculate Suffix Array:
    suffix = [0] * (n+1)
    rt = n-1
    for lt in range(n-1, -1, -1):  # (reverse traverse)
        while prize_positions[rt]-prize_positions[lt] > k:  # while segment_length > k
            rt -= 1  # shrink window
        suffix[lt] = max(suffix[lt+1], rt-lt+1)  # keep max till this index
    # print(suffix)  #debugging

    # Return max:
    return max(map(sum, zip(prefix, suffix)))

    # 1.2) Sliding Window + DP:
    # https://leetcode.com/problems/maximize-win-from-two-segments/solutions/3141449/java-c-python-dp-sliding-segment-o-n
    # https://leetcode.com/problems/maximize-win-from-two-segments/solutions/3141497/sliding-window-dp-o-n
