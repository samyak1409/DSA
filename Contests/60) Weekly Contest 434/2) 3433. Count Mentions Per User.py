"""
https://leetcode.com/problems/count-mentions-per-user
"""


def count_mentions(users: int, events: list[list[str]]) -> list[int]:
    """"""

    # 1) Optimal (Sort, Arr Indices as HashMap Keys): TC = O(e*log(e) + e*u); SC = O(e+u) {e: len(events); u: users}

    # Sort the events as they're not sorted on this basis of time:
    # And also handle the edge case there can be both message and offline event at the same timestamp:
    # Sort by timestamp, type (offline type first, message type after):
    events.sort(key=lambda e: (int(e[1]), e[0] == 'MESSAGE'))  # TC = O(e*log(e)); SC = O(e)
    # By `e[0] == 'MESSAGE'`: when e[0] = 'OFFLINE', it'd be `False`, else `True`.
    # `sorted([False, True])` = `[False, True]` because `False` evaluates to `0`, `True` to `1`.
    # print(events)  # debug

    mentions = [0] * users  # will hold the ans.
    off = [0] * users  # track offline users and for how much time, using arr indices as keys; SC = O(u)
    all_ = 0  # OPTIMIZATION: when we need to +1 all the users, don't do it again and again, do it in the end only once

    for type_, ts, msg in events:  # O(e)
        ts = int(ts)
        if type_ == 'OFFLINE':
            off[int(msg)] = ts + 60  # update state with timestamp it'd get online at
        else:  # 'MESSAGE'
            if msg == 'ALL':
                all_ += 1  # we'd ++ in the end together
            elif msg == 'HERE':
                for id_ in range(users):  # O(u)
                    if off[id_]:  # if this user is off
                        if off[id_] > ts:  # check if the online time is not crossed
                            continue  # skip the counting of this
                        else:  # if online time is crossed
                            off[id_] = 0  # reset status
                    mentions[id_] += 1  # count it
            else:
                for id_ in msg.split():
                    mentions[int(id_[2:])] += 1

    return [mention+all_ for mention in mentions]  # O(u)
