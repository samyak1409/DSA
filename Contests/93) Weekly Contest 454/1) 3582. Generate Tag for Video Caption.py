"""
https://leetcode.com/problems/generate-tag-for-video-caption
"""


def generate_tag(caption: str) -> str:
    """"""

    # 1) Optimal (Loop): TC = O(n); SC = O(1)

    # 1.1) Using python functions (SC = O(n)):

    # Inspired from
    # https://leetcode.com/problems/generate-tag-for-video-caption/solutions/6845005/python3-3-lines-title-and-lower-t-s-99-97:
    """
    # `title()` capitalize (word's first letter upper, rest lower) all the words in the caption, then split words on
    # spaces, and filter the empty strings generated due to consecutive spaces:
    ans = list(filter(None, caption.title().split()))
    # If `caption` didn't have any letter:
    if not ans:
        return '#'
    # Replace the first word in the list to prefix `#` and lower-case the first letter:
    ans[0] = f'#{ans[0].lower()}'
    # Trim and return:
    return ''.join(ans)[:100]
    """

    # I did this in contest:
    """
    ans = ['#']
    # Split words on spaces, filter the empty strings generated due to consecutive spaces, and loop:
    for i, w in enumerate(filter(None, caption.split())):
        # All the words should be title (word's first letter upper, rest lower), except the first word:
        ans.extend(w.capitalize() if i else w.lower())
    # Trim and return:
    return ''.join(ans[:100])
    """

    # 1.2) Without using python functions (SC = O(1)):

    ans = ['#']  # `list` for mutability
    # Flag which tells if current letter needs to be upper-cased / capitalized:
    up = False  # `False` for first letter
    for i, c in enumerate(caption):
        # If space means we need to capitalize the next letter:
        if c == ' ':
            up = len(ans) != 1  # but if len(ans) == 1 means first letter is still not added after `#`, so `up` should
            # still be `False`
            continue
        # If current char is letter, append it with case as per `up`:
        ans.append(c.upper() if up else c.lower())
        up = False  # reset
        # We only need 100 chars at max in our tag:
        if len(ans) == 100:
            break
    return ''.join(ans)
