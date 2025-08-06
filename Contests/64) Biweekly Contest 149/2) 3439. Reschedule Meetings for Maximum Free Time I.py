"""
https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i
"""


def max_free_time(mx: int, k: int, st: list[int], et: list[int]) -> int:
    """"""

    # 1) Optimal (Sliding Window): TC = O(n); SC = O(n)
    # Felt hard to come up with, but easy after knowing the solution.
    # Good article:
    # https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/solutions/6357735/merge-k-1-gaps
    # Good video explanation: https://youtu.be/Nn_LU8ir5wY
    # To understand the easy solution, watch from (timed link): https://youtu.be/Nn_LU8ir5wY?t=258

    # First, make an array of all the gaps from 0 to `eventTime` (`mx`): TC = SC = O(n)
    gaps = [st[0]]
    for i in range(1, len(st)):
        gaps.append(st[i]-et[i-1])
    gaps.append(mx-et[-1])
    # print(gaps)  # debug

    # Then, just keep a sliding window of fixed length k+1 (since if we're allowed to shift k meetings, we can sum up
    # k+1 gaps): TC = O(n)
    window = sum(gaps[:k+1])
    ans = window
    for i in range(k+1, len(gaps)):
        # Extend and shrink the window by 1 keeping the size same k+1:
        window += gaps[i] - gaps[i-(k+1)]
        ans = max(ans, window)
    return ans
