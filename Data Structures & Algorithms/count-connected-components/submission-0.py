class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap = {i: [] for i in range(n)}
        for a, b in edges:
            hashmap[a].append(b)
            hashmap[b].append(a)
        
        res = 0

        # Track all the visited nodes
        visited = set()

        def dfs(i: int):
            # Don't revisit
            if i in visited:
                return
            
            # Mark node as visited
            visited.add(i)

            # Recursively visit child nodes
            for n in hashmap[i]:
                dfs(n)

        for i in range(n):
            if i in visited: continue
            dfs(i)
            res += 1
        
        return res