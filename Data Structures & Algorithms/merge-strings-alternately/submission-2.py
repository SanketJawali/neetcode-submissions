class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        a, b = 0, 0

        while a < len(word1) or b < len(word2):
            if a < len(word1): res.append(word1[a])
            if b < len(word2): res.append(word2[b])
            a += 1
            b += 1
        return "".join(res)