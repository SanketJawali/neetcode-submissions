class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x

        low, high = 1, x
        n = x
        while low <= high:
            n = (low + ((high - low) // 2))
            n2 = n ** 2
            print(n)
            if n2 == x:
                return n
            elif n2 > x:
                high = n - 1
            else:
                low = n + 1
        return (low + ((high - low) // 2))