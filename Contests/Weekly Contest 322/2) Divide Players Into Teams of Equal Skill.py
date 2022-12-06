"""
https://leetcode.com/problems/divide-players-into-teams-of-equal-skill
"""


def divide_players(skill: list[int]) -> int:
    """"""

    # 1) Sub-Optimal (Sort & then Choose first and last and so on): TC = O(n*log(n)); SC = O(n)
    # Try sorting the skill array.
    # It is always optimal to pair the weakest available player with the strongest available player.

    """
    skill = sorted(skill)  # new local var
    team_skill = skill[0] + skill[-1]  # init with first and last
    chemistry = 0
    for i in range(len(skill)//2):
        if skill[i]+skill[~i] != team_skill:
            return -1
        chemistry += skill[i] * skill[~i]
    return chemistry
    """

    # 2) Optimal (HashMap to count occurrences): TC = O(n); SC = O(n)
    # https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/solutions/2875011/PythonC++-O(N)-counting-and-pair-matching-(explained)

    from collections import Counter

    skill_count = Counter(skill)
    team_skill = sum(skill) // (len(skill)//2)  # required team skill in order to make skill of each team equal
    chemistry = 0
    for s1, count in skill_count.items():
        if skill_count[s2 := team_skill-s1] != count:  # if there are diff. no. of players with required skill
            return -1                                  # in order to make skill of each team equal
        chemistry += s1 * s2 * count
    return chemistry // 2  # because we ran the loop all over the `skill`, so pairs are considered twice
