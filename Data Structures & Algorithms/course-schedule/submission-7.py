class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a hashmap {Course -> Prerequisite}
        # Populate the hashmap with empty values, helps handles the no prerequisite case
        hashmap = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            hashmap[c].append(p)
        print(hashmap)

        def dfs(i, visit):
            if i in visit:
                return False
            if hashmap[i] == []:
                return True
            
            visit.add(i)
            # Recursively check all prerequisites of course i
            for p in hashmap[i]:
                if not dfs(p, visit):
                    # Return immediately if a loop is found
                    return False
            # Update the prerequisites to empty for current course
            # avoid redoing the dfs for same course
            hashmap[i] = []
            visit.remove(i)
            return True
                
        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        return True