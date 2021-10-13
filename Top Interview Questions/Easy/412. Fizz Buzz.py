"""
https://leetcode.com/problems/fizz-buzz/
"""


from typing import List


def fizzBuzz(n: int) -> List[str]:

    # TC = O(n); SC = O(1)

    for i in range(1, n+1):
        if i % 15 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        else:
            yield str(i)
