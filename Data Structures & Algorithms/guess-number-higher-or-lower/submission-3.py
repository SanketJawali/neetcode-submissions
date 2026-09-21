# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        currguess = n
        for i in range(n):
            currguess = ((high - low) // 2) + low
            res = guess(currguess)
            if res == 0:
                return currguess
            elif res < 0:
                high = currguess - 1
            else:
                low = currguess + 1
        return currguess