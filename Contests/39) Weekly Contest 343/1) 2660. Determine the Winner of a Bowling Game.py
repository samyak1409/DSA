"""
https://leetcode.com/problems/determine-the-winner-of-a-bowling-game
"""


def is_winner(player1: list[int], player2: list[int]) -> int:
    """"""

    # Think about simulating the process to calculate the answer.
    # Iterate over each element and check the previous two elements. See if one of them is 10 and can affect the score.

    # 1) Optimal (Simulation: OTG checking prev two turns (if there)): TC = O(n); SC = O(1)

    """
    # Helper Function:
    def get_score(pins_list: list[int]) -> int:
        """"""
        '''
        score = 0
        for i, pins in enumerate(pins_list):
            score += pins * (2 if ((i-1 >= 0 and pins_list[i-1] == 10) or (i-2 >= 0 and pins_list[i-2] == 10)) else 1)
        return score
        '''
        # 2-liner:
        return sum(pins * (2 if ((i-1 >= 0 and pins_list[i-1] == 10) or (i-2 >= 0 and pins_list[i-2] == 10)) else 1)
                   for i, pins in enumerate(pins_list))

    # Return: 1 if the score of player 1 is more than the score of player 2,
    #         2 if the score of player 2 is more than the score of player 1, and
    #         0 in case of a draw.
    if (score_diff := get_score(player1)-get_score(player2)) > 0:
        return 1
    if score_diff < 0:
        return 2
    return 0
    """

    # 2) Optimal (Simulation: Using a var which tracks if 2x is required): TC = O(n); SC = O(1)
    # Solution `1)` is perfectly fine for current problem, but this will work for generic case where it's given like
    # "any of the previous k turns" (instead of "any of the previous two turns").

    # Helper Function:
    def get_score(pins_list: list[int]) -> int:
        score = x2_left = 0  # `x2_left`: how many times we need to 2x the pins
        for pins in pins_list:
            score += pins * (2 if x2_left else 1)
            if pins == 10:  # => next two pins would be 2x
                x2_left = 2
            elif x2_left:
                x2_left -= 1  # else --x2_left
        return score

    # Return: 1 if the score of player 1 is more than the score of player 2,
    #         2 if the score of player 2 is more than the score of player 1, and
    #         0 in case of a draw.
    if (score_diff := get_score(player1)-get_score(player2)) > 0:
        return 1
    if score_diff < 0:
        return 2
    return 0
