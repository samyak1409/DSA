"""
https://leetcode.com/problems/maximum-matching-of-players-with-trainers
"""


def match_players_and_trainers(players: list[int], trainers: list[int]) -> int:
    """"""

    # Same as:
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/03%29%20Greedy%20Algorithm/048%29%20Assign%20Cookies.py

    # 1) Optimal (Greedy: Sort): TC = O(m*log(m) + n*log(n)); SC = O(m+n)
    # Since we just want to take the number of children up, just give the minimum size of cookie to a children who can
    # take it.

    # Sort abilities:
    players = sorted(players)
    i = 0
    player_cnt = len(players)
    # Iterate on sorted capacities:
    for c in sorted(trainers):
        # If i-th player's ability <= this trainer's capacity `c`:
        if players[i] <= c:
            # Matching can be done, move to the next player:
            i += 1
            # Break out if we've covered all players:
            if i == player_cnt:
                break
        # Move on to the next trainer.
    # We can use the index only to return the ans:
    return i
