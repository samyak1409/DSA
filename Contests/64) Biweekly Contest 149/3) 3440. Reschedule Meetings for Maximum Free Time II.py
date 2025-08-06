"""
https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii
"""


def max_free_time(mx: int, st: list[int], et: list[int]) -> int:
    """"""

    # 1) Optimal (Prefix & Suffix Maxes): TC = O(n); SC = O(n)
    # Not hard to come up with, little tricky implementation.
    # Video explanation: https://youtu.be/5VioKVNRPKk

    # First, make an array of all the gaps from 0 to `eventTime` (`mx`): TC = SC = O(n)
    gaps = [st[0]]
    for i in range(1, len(st)):
        gaps.append(st[i]-et[i-1])
    gaps.append(mx-et[-1])
    # print(gaps)  # debug

    # Build prefix max: TC = SC = O(n)
    pre = [0]
    for i in range(len(gaps)-2):  # [0, len(gaps)-3]
        pre.append(max(pre[-1], gaps[i]))
    # print(pre)  # debug

    # Build suffix max: TC = SC = O(n)
    suf = [0]
    for i in range(len(gaps)-1, 1, -1):  # [len(gaps)-1, 2]
        suf.append(max(suf[-1], gaps[i]))
    suf.reverse()
    # print(suf)  # debug

    # Try moving all the meetings one by one: TC = O(n)
    ans = 0
    for i in range(len(st)):
        d = et[i] - st[i]  # meeting duration
        ans = max(ans, gaps[i] + (d if pre[i] >= d or suf[i] >= d else 0) + gaps[i+1])
        # `d if pre[i] >= d or suf[i] >= d else 0`: if some space is there for current meeting, it's duration len is
        # emptied, so add up that, else 0
    return ans
