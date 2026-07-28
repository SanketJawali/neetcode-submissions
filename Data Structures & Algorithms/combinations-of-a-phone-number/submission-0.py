class Solution:
    # initiate map
    def __init__(self):
        self.pad = {
            2: {'a', 'b', 'c'},
            3: {'d', 'e', 'f'},
            4: {'g', 'h', 'i'},
            5: {'j', 'k', 'l'},
            6: {'m', 'n', 'o'},
            7: {'p', 'q', 'r', 's'},
            8: {'t', 'u', 'v'},
            9: {'w', 'x', 'y', 'z'},
        }


    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1:
            return []

        res = []

        curr = []
        def backtrack(s: str):
            if len(s) < 1:
                op = "".join(curr)
                res.append(op)
                return
            
            n = int(s[0])
            sub_s = s[1:] if len(s) > 1 else ""

            if n in self.pad:
                for c in self.pad[n]:
                    curr.append(c)
                    backtrack(sub_s)
                    curr.pop()
        
        backtrack(digits)

        return res