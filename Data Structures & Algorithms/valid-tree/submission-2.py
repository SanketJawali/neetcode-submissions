class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # If a graph is a valid tree, there should be no cycles in it
        # Create a hashmap prepresenting edges of each node
        hashmap = {i: [] for i in range(n)}
        for a, b in edges:
            # Graph is undirectional, so we need to add edges to both node's neighbour list
            hashmap[a].append(b)
            hashmap[b].append(a)
        print(hashmap)

        # Helps in checking all nodes in a disjoint graph
        checked = 0

        def dfs(curr, prev, visited):
            print("Visiting ", curr)
            nonlocal checked
            checked += 1

            # Check if we revisited a node, indicating a cycle
            if curr in visited:
                # Return False inticating a cycle in graph
                return False
            
            # Recursively visit neighbouring nodes
            for neighbour in hashmap[curr]:
                if neighbour == prev: continue
                visited.add(curr)
                if not dfs(neighbour, curr, visited):
                    return False
                visited.remove(curr)
            
            return True

        # For each node, check if any node can be revisited
        # Use DFS, use a set to track nodes in current path, keep track of previous node
        if not dfs(0, None, set()):
            return False
        if checked < n:
            # Not all nodes were visited, the graph is disconnected, not a tree
            return False
            
        return True