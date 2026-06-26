class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        
        l = 0
        r = 0

        encountered = {}
        for r, c in enumerate(s):
            # Check if the current character is a repeatition
            if c in encountered:
                # Set l to position after the repeated character

                l = encountered[c] + 1 if encountered[c] + 1 > l else l
            
            print(encountered)
            encountered[c] = r

            # Calculate the maxlen
            currentLen = r - l + 1

            maxlen = currentLen if currentLen > maxlen else maxlen
            print(f"c: {c}, maxlen: {maxlen}, l: {l}, r: {r}")

        return maxlen
            