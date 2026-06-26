class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashset = {}
        count = 0
        for c in s1:
            if c in hashset:
                hashset[c] += 1
            else:
                hashset[c] = 1
            count += 1      
        print(hashset, count)
        if len(s2) < len(s1):
            return False
        
        l, r = 0, (count - 1)

        while r < len(s2):
            if l == 0:
                for char in s2[l:r + 1]:
                    if char in hashset:
                        print(f"Found {char}, {hashset}, {count}")
                        count -= 1 if hashset[char] > 0 else 0
                        hashset[char] -= 1
            else:
                if s2[r] in hashset:
                    print(f"found {s2[r]}, {hashset}, {count}")
                    count -= 1 if hashset[s2[r]] > 0 else 0
                    hashset[s2[r]] -= 1
                
            print(f"set: {hashset}, count: {count}, c: {s2[r]}")
            if count == 0:
                return True
            else:
                if s2[l] in hashset:
                    count += 1 if hashset[s2[l]] >= 0 else 0
                    hashset[s2[l]] += 1
                l += 1
                r += 1
        return True if count == 0 else False