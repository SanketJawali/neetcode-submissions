class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # An anagram has same number alphabets, just in different sequence
        # If we can first find all the unique alphabets and their counts
        # we can find all the words, who have same unique alphabets and their counts

        result = {}

        for s in strs:
            counts = [0] * 26

            # Count all the chars in the word
            for c in s:
                counts[ord(c) - ord('a')] += 1
            
            if str(counts) in result:
                result[str(counts)] += [s]
            else:
                result[str(counts)] = [s]
        print(list(result.values()))
        return list(result.values())
        