class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            sign = tuple(count)
            if sign in res:
                res[sign].append(s)
            else:
                res[sign] = [s]
        return list(res.values())