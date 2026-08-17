class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []    # Contain the order of completion of courses

        # Convert input to hashmap, populate hashmap
        hashmap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            hashmap[course].append(pre)

        # Completed list, track completed courses
        # 0: incomplete course, 1: completed course
        completed = [0] * numCourses

        def dfs(i, visited = set()):
            # Check for loop in graph
            if i in visited:
                return False
            
            # Check if course already completed
            if completed[i] == 1:
                return True

            # Complete courses with no prerequisite
            if len(hashmap[i]) == 0:
                completed[i] = 1
                res.append(i)
                return True
            
            # Recursively complete all prerequisites for current course
            for pre in hashmap[i]:
                if completed[pre] == 0:
                    visited.add(i)
                    if not dfs(pre, visited):
                        return False
                    visited.remove(i)
            hashmap[i] = []
            completed[i] = 1
            res.append(i)

            return True

        # Complete all courses
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res