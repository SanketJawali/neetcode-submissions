class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)  # According to PS, n = len(edges) = no. of nodes

        # Convert edges to hashmap for fast access
        hashmap = {i: [] for i in range(1, n + 1)}
        for a, b in edges:
            hashmap[a].append(b)
            hashmap[b].append(a)
        
        def dfs(i, previous, visited, path):
            # Check for cycle
            if i in visited:
                # Append current node again to know where cycle starts
                path.append(i)
                return path
            
            for p in hashmap[i]:
                if p == previous: continue

                visited.add(i)
                path.append(i)
                if dfs(p, i, visited, path) is not None:
                    return path
                visited.remove(i)
                path.pop()
            
            return

        # Start DFS from node 1
        cycle = dfs(1, None, set(), [])
        print(cycle)
        start = cycle.pop()
        cycle = set(cycle[cycle.index(start):])
        
        # Starting from the last edge in 'edges', find the redundant edge
        for a, b in reversed(edges):
            if a in cycle and b in cycle:
                return [a, b]