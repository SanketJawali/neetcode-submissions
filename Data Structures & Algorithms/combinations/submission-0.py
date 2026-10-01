class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []

        def dfs(i: int = 1, cc: List[int] = []):
            if len(cc) == k:
                self.res.append(cc.copy())
                return
            
            if i <= n:
                cc.append(i)
                dfs(i + 1, cc)
                cc.pop()
                dfs(i + 1, cc)
        
        dfs()
        return self.res