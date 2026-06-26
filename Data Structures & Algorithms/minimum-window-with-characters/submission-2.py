class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substr = ""
        counts = {}
        charsToFind = len(t)

        if len(t) < 1:
            return ""

        for c in t:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

        l = 0
        for r, c in enumerate(s):
            if c in counts and counts[c] > 0:
                counts[c] -= 1
                charsToFind -= 1
                print(f"found {c}, ste len: {r - l + 1}")
            elif c in counts and counts[c] <= 0:
                # while l < r:
                #     counts[c] -= 1
                #     if s[l] in counts and counts[s[l]] == 0:
                #         break
                #     l += 1

                # Check what char sits at l
                # If it is not c, check how many we can remove
                counts[c] -= 1
                for _ in range(l, r):
                    # if s[l] == c:
                    #     counts[c]  += 1
                    #     l += 1
                    if s[l] in counts and counts[s[l]] < 0:
                        counts[s[l]] += 1
                        l += 1
                    elif s[l] not in counts:
                        l += 1
            else:
                # c not in counts
                if charsToFind == len(t):
                    l += 1

            print(f"C: {c}, str: {s[l:r + 1]}, counts: {counts}")
            # Check if all chars are found, if yes then store the substring
            if charsToFind == 0:
                if substr == "":
                    substr = s[l : r + 1]
                substr = s[l : r + 1] if (r - l + 1) < len(substr) else substr

        return substr
