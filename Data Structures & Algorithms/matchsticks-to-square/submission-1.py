class Solution:
    def makesquare(self, sticks: List[int]) -> bool:
        # Each stick can be a part of 1 of 4 edges
        # We try different combinations to find a valid combination for all sticks
        # If even one valid combination exist, we return True
        # If no combination exist, return False

        # We can also calculate the length of the edge beforehand
        # this way we know if a square is even possible with the given sticks

        perimeter = sum(sticks)
        if perimeter % 4 != 0:
            # All sticks can't form a square
            return False
        l = perimeter / 4
        if max(sticks) > l:
            # All sticks cannot be used
            return False

        def backtrack(edges: List[int], i: int):
            if max(edges) > l:
                return False
            if i == len(sticks):
                return min(edges) == max(edges) # Check all edges are equal length
            
            res = False
            for j in range(4):
                # Add sticks[i] to edge j
                edges[j] += sticks[i]
                res = res or backtrack(edges, i + 1)
                if res:
                    return res
                edges[j] -= sticks[i]
            return res
        
        return backtrack([0, 0, 0, 0], 0)