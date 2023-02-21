"""
https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up
"""


def minimum_card_pickup(cards: list[int]) -> int:

    # 0) Brute-force (Check all the Subarrays using Nested Loop): TC = O(n^2); SC = O(1)

    # 1) Optimal (HashMap): TC = O(n); SC = O(n)
    # Iterate through the cards and store the location of the last occurrence of each number.
    # What data structure could you use to get the last occurrence of a number in O(1) or O(log(n))?

    last_index = {}  # for O(1) lookup
    min_cards = float('inf')  # init
    for index, card in enumerate(cards):
        if (last := last_index.get(card)) is not None:  # => card occurred before too
            min_cards = min(min_cards, index-last+1)  # `index-last+1` = len(subarray) with at least a pair of matching
            # cards
        last_index[card] = index  # add / update
    return min_cards if (min_cards != float('inf')) else -1
