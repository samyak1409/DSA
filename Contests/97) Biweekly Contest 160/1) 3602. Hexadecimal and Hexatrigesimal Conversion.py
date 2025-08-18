"""
https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion
"""


def concat_hex_36(n: int) -> str:
    """"""

    # 1) Optimal (Procedural conversion using % op and while loop): TC = O(log16(n^3)+log36(n^3)); SC = O(log16(n^3))
    # Very easy!
    # Just dry run converting a number e.g. 169 to base 10, and notice the steps. (Yes, base 10 to base 10, just for getting the pattern.)

    # Helper func:
    def get_converted(n: int, base: int) -> str:
        x = []
        while n:
            d = n % base
            x.append(str(d) if d < 10 else chr(ord("A")+d-10))
            n //= base
        return ''.join(reversed(x))

    return get_converted(n=(n2:=n*n), base=16) + get_converted(n=n2*n, base=36)
