class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        total = n
        while True:
            tmp = 0
            for digit in str(total):
                tmp += int(digit) ** 2
            total = tmp
            if total == 1: return True
            if total in seen: return False
            seen.add(total)
            print(seen, total)
        return False