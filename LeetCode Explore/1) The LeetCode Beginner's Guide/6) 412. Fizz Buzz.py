"""
https://leetcode.com/problems/fizz-buzz
"""


def fizz_buzz(n: int) -> list[str]:
    """"""

    # 1) Optimal (Loop & Check Modulo): TC = O(n); SC = O(1)
    # See: https://leetcode.com/problems/fizz-buzz/solutions/173828/fizz-buzz

    """
    for dividend in range(1, n+1):
        if dividend % 15 == 0:
            yield 'FizzBuzz'
        elif dividend % 3 == 0:
            yield 'Fizz'
        elif dividend % 5 == 0:
            yield 'Buzz'
        else:
            yield f'{dividend}'
    """

    # Using String Concatenation which reduces the no. of conditions:

    """
    for dividend in range(1, n+1):
        ans = ''
        if dividend % 3 == 0:
            ans += 'Fizz'
        if dividend % 5 == 0:
            ans += 'Buzz'
        yield ans or f'{dividend}'
    """

    # Adding HashMap in order to make it scalable:

    hm = {3: 'Fizz', 5: 'Buzz'}
    for dividend in range(1, n+1):
        ans = ''
        for divisor in hm.keys():
            if dividend % divisor == 0:
                ans += hm[divisor]
        yield ans or f'{dividend}'
