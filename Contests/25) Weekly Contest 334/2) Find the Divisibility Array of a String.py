"""
https://leetcode.com/problems/find-the-divisibility-array-of-a-string
"""


def divisibility_array(word: str, m: int) -> list[int]:
    """"""

    # We can check if the numeric value of the prefix of the given string is divisible by m by computing the remainder
    # of the numeric value of the prefix when divided by m.
    # The remainder of the numeric value of a prefix ending at index `i` can be computed from the remainder of the
    # prefix ending at index `i-1`.

    # 1) Optimal (One by one add new digit and keep forming the next num and use % op (in 2 ways)): TC = O(n); SC = O(1)

    # [TLE ☹️] Submission 1:
    # Take digit one by one, everytime right shift (base 10) the num by one then add digit, then check using remainder
    # op, if remainder == 0 => divisible, and then just yield.

    """
    num = 0  # init
    for d in word:  # TC = O(n)
        num = num*10 + int(d)  # form next num
        yield int(num % m == 0)  # yield 1 if divisible else 0
    """

    # Why TLE? Loop is just O(n), inside the loop, every num is O(1), then why TLE?
    # After a minute, realized, num will grow monstrously large (max(len(word)) == 1e5) 🤦
    # So, even a O(1) op will basically take a lot of time (this is not the first time faced a situation like this).
    # What a little mistake though.
    # Why this happened? Because, while coding in Python, I never worried about int overflow!!
    # If I have been coding in some other lang, for sure I had caught it!

    # Submission 2:
    # Small fix.

    """
    num = 0  # init
    for d in word:  # TC = O(n)
        num = num*10 + int(d)  # form next num
        num %= m  # keep modding the num with `m` so that it never grows large
        # modding doesn't disturb the ans because we're modding with the divisor only, so basically we're just reducing
        # the quotient, which doesn't change the ans, because we don't care what the quotient is, we just want the
        # remainder = 0
        yield int(num == 0)  # yield 1 if divisible else 0
    """
    # Short:
    num = 0  # init
    for d in word:  # TC = O(n)
        yield int((num := (num*10+int(d)) % m) == 0)  # form next num, mod, and yield 1 if divisible else 0
