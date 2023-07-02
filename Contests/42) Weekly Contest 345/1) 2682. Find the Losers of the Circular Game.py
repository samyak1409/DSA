"""
https://leetcode.com/problems/find-the-losers-of-the-circular-game
"""


def circular_game_losers(n: int, k: int) -> list[int]:
    """"""

    # Simulate the whole game until a player receives the ball for the second time.

    # 1) Optimal (Simulation using Freq Arr): TC = O(n); SC = O(n)

    # Freq arr to track ball received or not in O(1):
    ball_received = [0] * n
    # Init curr pos of ball and `i` (which is the # of turn):
    curr_pos = i = 0
    # Game continues:
    while True:
        # Update next pos to be:
        curr_pos = (curr_pos + k*i) % n  # `% n`: as "friends are sitting in a circle"
        # "The game is finished when some friend receives the ball for the second time.":
        if ball_received[curr_pos]:
            # "The losers of the game are friends who did not receive the ball in the entire game.
            # Return the array answer, which contains the losers of the game in the ascending order."
            return [friend for friend, ball_received_ in enumerate(ball_received, start=1) if not ball_received_]
        # Update status:
        ball_received[curr_pos] = 1
        # Update turn #:
        i += 1
