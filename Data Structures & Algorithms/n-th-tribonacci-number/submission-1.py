class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2: return n
        if n == 2: return 1

        zero, one, two = 0, 1, 1

        for _ in range(n - 2):
            zero, one, two = one, two, zero + one + two
        
        return two