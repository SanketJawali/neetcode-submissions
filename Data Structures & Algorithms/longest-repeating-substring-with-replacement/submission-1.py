class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        l, r = 0, 0

        freq = {}
        by = ""
        for r, c in enumerate(s):
            if r == 0:
                by = c
                maxLen += 1

            if c in freq:
                freq[c] += 1
                print(f"freq: {freq}, c: {c}")
                if freq[by] < freq[c]:
                    by = c
            else:
                freq[c] = 1
            
            # If num of replacables > k, move left
            if (r - l + 1) - freq[str(by)] > k:
                freq[s[l]] -= 1
                # if freq[s[l]] == 0:
                #     freq.pop(s[l])
                l += 1

            maxLen = (r - l + 1) if (r - l + 1) > maxLen else maxLen
        
        return maxLen