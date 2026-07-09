# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         # At every index, we have a choice to create a partition or not to create a partition
#         # While creating a partition, we need to keep track if the partition is a palindrome
#         # If partition we are creating is not a palindrome, we don't create it

#         # We need a way to keep track, if current substring is a palindrome
#         # At each stage we recursively choose to partition, or not to
#         # We can partition, only if current substring is palindrome
#         # Add valid leaf nodes to result

#         res = []

#         combination = []
#         def backtrack(word: str, partition: bool):
#             # word: current word
#             # partition: represents if a partition was made or not

#             if len(word) == 1:
#                 if len(combination) == 0: return
#                 combination[-1] += word[0]
#                 if self.isPalindrome(combination[-1]):
#                     res.append(combination.copy())
#                     combination.clear()
#                 return

#             # If a partition was made on last stage, create a new substring
#             if partition or len(combination) == 0:
#                 combination.append(word[0])
#                 backtrack(word[1:], False)

#             if not partition and self.isPalindrome(combination[-1]):
#                 # Make partition on current word
#                 backtrack(word, True)
#                 combination.pop()
            
#             combination[-1] += word[0]
#             backtrack(word[1:], False)


#     def isPalindrome(self, s: str) -> bool:
#         for i in range(len(s)):
#             if s[i] != s[len(s) - i - 1]:
#                 return False
#         return True

class Solution:

    def partition(self, s: str) -> List[List[str]]:
        # Initialize result and current substring list
        res, part = [], []

        def backtrack(i):
            # If we have checked all chars in s
            if i >= len(s):
                res.append(part.copy())
                return

            # From i->end
            # [...i, x, y, z, j, ...]
            # Check if string between i and j is palindrome
            # If palindrome, recursively check for the remaining string s[j:]
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i : j + 1])
                    backtrack(j + 1)
                    part.pop()

        backtrack(0)
        return res

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True