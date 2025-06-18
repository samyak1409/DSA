"""
https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings
"""


def max_substrings(word: str) -> int:
    """"""

    # 1) Time-optimal (Greedy, HashMap): TC = O(n); SC = O(n)
    # [What I came up with in contest.]
    # Loop the word, keep track of the indices of every char in a hashmap, pick the earliest finishing substr of at
    # least 4 chars.

    """
    from collections import defaultdict

    hm = defaultdict(list)  # c: [indices]
    cnt = 0
    last_end = -1  # end index of last chosen substr

    # Iterate on word:
    for j, c in enumerate(word):
        
        # Reverse iterate on the prev indices of this char in order to find the smallest index `i` which makes the
        # substr >= 4:
        for i in range(len(hm[c])-1, -1, -1):
            # Get the index:
            i = hm[c][i]
            # It should be after `last_end`, else break:
            if i <= last_end:
                break
            # If this idx makes at least 4 length substr:
            if j-i+1 >= 4:
                cnt += 1
        
        # Save index for next iterations:
        hm[c].append(j)

    return cnt
    """

    # The only difference between above and below implementation is:
    # Above is keeping all the indices saved, and using `last_end` to consider only those indices which are after
    # `last_end`.
    # Below does better by emptying the `hm` as soon as a substr is formed, and only storing the smallest index after.

    # 2) Optimal (Greedy, HashMap): TC = O(n); SC = O(26)
    # https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/solutions/6781403/python3-9-lines-iteration-t-s-97-96

    hm = {}
    cnt = 0

    # Iterate on word:
    for j, c in enumerate(word):

        # If we don't have a prev index of current char, then simply save curr index `j` for future iterations:
        # (Note: We're not updating the index if it's already there so that we have the left-most index
        # (after last substr), not the right-most one.)
        if (i := hm.get(c)) is None:
            hm[c] = j

        # Else if substr >= 4 is forming:
        elif j-i+1 >= 4:
            cnt += 1
            # And clear the indices now, since we can't use them now:
            hm.clear()

    return cnt
