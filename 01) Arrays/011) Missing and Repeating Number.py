"""
https://www.codingninjas.com/codestudio/problems/873366
"""


def missing_and_repeating(arr: list[int], n: int) -> list[int]:
    """"""

    # 0.1) Brute-force (Sort): TC = O(n*log(n)); SC = O(n)

    """
    sorted_arr = sorted(arr)
    missing = 1  # starting from 1
    for i in range(n):  # finding missing number
        current = sorted_arr[i]
        if current > missing:  # if at any point, "current" exceeds "missing" => "missing" is the number which didn't
            # occur in arr
            break
        missing = current+1  # else missing = next number that should be
    repeating = None
    for i in range(n):  # finding repeating number
        current, next_ = sorted_arr[i], sorted_arr[i+1]
        if next_ == current:  # simple
            repeating = next_
            break
    return [missing, repeating]
    """

    # 0.2) Brute-force (HashSet): TC = O(n); SC = O(n)

    """
    hashset = set()  # to track existence in O(1)
    repeating = None
    for num in arr:  # finding repeating number
        if num in hashset:
            repeating = num
        hashset.add(num)
    missing = None
    for num in range(1, n+1):  # finding missing number
        if num not in hashset:
            missing = num
            break
    return [missing, repeating]
    """

    # 0.3) Brute-force (Count & Store Occurrences): TC = O(n); SC = O(n)
    # Rather than using HashMap, we can simply use Array here in which the indices will work like keys.
    # As the contents of "arr" will be in b/w 1 and n; the task can be easily performed by Array rather than HashMap.
    # Why give priority to Array over HashMap? > Less Space!

    """
    counts = [0] * n
    for num in arr:  # counting
        counts[num-1] += 1  # num-1 = index
    return [counts.index(0)+1, counts.index(2)+1]  # missing, repeating
    """

    # 1) Optimal (Negating Numbers): TC = O(n); SC = O(1)

    """
    repeating = None
    for i in range(n):  # finding repeating number
        index = abs(arr[i])-1  # index to leave mark at; abs() because arr[i] can be a negated value
        if arr[index] < 0:  # value at "index" found negated => index+1 (arr[i]) is the repeating number!
            repeating = index+1
        else:
            arr[index] *= -1  # leaving mark
    missing = None
    for i in range(n):  # finding missing number
        if arr[i] > 0:  # positive value found, it must be because of the missing number
            missing = i+1
        else:  # turning the negated values back positive
            arr[i] *= -1
    return [missing, repeating]
    """

    # 2) Optimal (Maths: Sum of n and n^2 terms): TC = O(n); SC = O(1)

    # In short:
    """
    x = n*(n+1)//2 - sum(arr)
    y = ((n*(n+1)*(2*n+1)//6)-(sum(map(lambda term: term**2, arr)))) // x
    missing = (x+y) // 2
    repeating = missing - x
    return [missing, repeating]
    """

    # With Derivation:
    # sum(arr) + missing - repeating = n*(n+1) // 2  # sum of n terms
    # => missing - repeating = n*(n+1)//2 - sum(arr)
    # Let x = missing - repeating  # ...(1)
    x = n*(n+1)//2 - sum(arr)
    # print(x)  #debugging

    # sum(map(lambda term: term**2, arr)) + missing**2 - repeating**2 = n*(n+1)*(2*n+1) // 6  # sum of n^2 terms
    # => missing**2 - repeating**2 = n*(n+1)*(2*n+1)//6 - sum(map(lambda term: term**2, arr))
    # Since a^2 - b^2 = (a+b)(a-b):
    # => (missing+repeating) * (missing-repeating) = n*(n+1)*(2*n+1)//6 - sum(map(lambda term: term**2, arr))
    # From equation (1), (missing-repeating) = x, so:
    # => (missing+repeating) * x = n*(n+1)*(2*n+1)//6 - sum(map(lambda term: term**2, arr))
    # => missing + repeating = ((n*(n+1)*(2*n+1)//6)-(sum(map(lambda term: term**2, arr)))) // x
    # Let y = missing + repeating
    y = ((n*(n+1)*(2*n+1)//6)-(sum(map(lambda term: term**2, arr)))) // x
    # print(y)  #debugging

    # x + y = (missing-repeating) + (missing+repeating)
    # => x + y = 2 * missing
    # => missing = (x+y) // 2
    missing = (x+y) // 2
    # And from equation (1), repeating = missing - x, so:
    # => repeating = (x+y)//2 - x
    repeating = missing - x
    return [missing, repeating]
