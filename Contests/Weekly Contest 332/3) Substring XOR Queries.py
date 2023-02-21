"""
https://leetcode.com/problems/substring-xor-queries
"""


def substring_xor_queries(s: str, queries: list[list[int]]) -> list[list[int]]:
    """"""

    # First of all, if Z ^ X = Y => Z == X ^ Y
    # So, for each query, we basically just need to calculate the smallest substring with XOR == first ^ second.

    # Now, if there were only a single query instead of queries, it'll be the standard question "Find the
    # smallest substring with given XOR", which can be easily solved by (Prefix XOR + HashMap).
    # Here, if we do the same for each query one by one:
    # 0.1) [TLE] Brute-force (Prefix XOR + HashMap: Calc for each query one by one): TC = O(q * n); SC = O(n)

    # Then, what can we do?
    # Alternatively, we can also calc XORs of all the (n^2) substrings using Kadane's Algo, save them in a HashMap, and
    # then return the ans for each query:
    # 0.2) [TLE] Brute-force (HashMap: Calc values of all substrings using Kadane's Algo): TC = O(n^2 + q); SC = O(n^2)

    """
    # Preprocess: Calc & Save the values of all the substrings in a HashMap:
    endpoints = {}  # (val: [left, right])
    for left in range(n := len(s)):
        if s[left] != '0':  # avoid picking binary strings starting with 0 (2 is '10' not '010')
            val = 0  # decimal val (base 10) of the binary string (base 2)
            for right in range(left, n):  # start from this index and go till the end
                # Calculating the next decimal val:
                val = (val << 1) + int(s[right])
                # Save if not already there as we are asked to return most left one:
                if val not in endpoints:
                    endpoints[val] = [left, right]
        else:  # s[left] == '0'
            # Don't forget the value 0 itself:
            if 0 not in endpoints:
                endpoints[0] = [left, left]
    # print(endpoints)  #debugging

    # Yield Ans:
    yield from (endpoints.get(first ^ second, [-1, -1]) for first, second in queries)
    """

    # There doesn't look like any other way to solve the problem, then how will this be solved?
    # Yes, there is no other way to solve the problem, and, it will be solved by the above approach only!!
    # Just with a single observation and change!
    # "first, second <= 10^9" => max(len_in_binary(first or second)) = ceil(log2(10**9)) = 30
    # => WE DO NOT NEED TO CONSIDER SUBSTRINGS HAVING LENGTHS GREATER THAN 30.

    # 1) Optimal (HashMap: Calc values of all substrings with len <= 30 using Kadane's Algo):
    # TC = O(30n + q) = O(n + q); SC = O(30n) = O(n)
    # Note that this optimal solution has literally a single, that too tiny change from the above one that is
    # brute-force!!
    # https://leetcode.com/problems/substring-xor-queries/solutions/3174092/o-32-n-hash-map-solution
    # https://leetcode.com/problems/substring-xor-queries/solutions/3174169/python-hashmap
    # https://leetcode.com/problems/substring-xor-queries/solutions/3174035/hashmap-o-n-30

    # Preprocess: Calc & Save the values of the substrings with len <= 30 in a HashMap:
    endpoints = {}  # (val: [left, right])
    for left in range(n := len(s)):
        if s[left] != '0':  # avoid picking binary strings starting with 0 (2 is '10' not '010')
            val = 0  # decimal val (base 10) of the binary string (base 2)
            for right in range(left, min(left+30, n)):  # start from this index and go for 30 indices
                # Calculating the next decimal val:
                val = (val << 1) + int(s[right])
                # Save if not already there as we are asked to return most left one:
                if val not in endpoints:
                    endpoints[val] = [left, right]
        else:  # s[left] == '0'
            # Don't forget the value 0 itself:
            if 0 not in endpoints:
                endpoints[0] = [left, left]
    # print(endpoints)  #debugging

    # Yield Ans:
    yield from (endpoints.get(first ^ second, [-1, -1]) for first, second in queries)
