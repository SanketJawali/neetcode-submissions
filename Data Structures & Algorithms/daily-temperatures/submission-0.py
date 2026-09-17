class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temp)

        for i in range(len(temp)):
            if len(stack) == 0 or stack[-1][1] >= temp[i]:
                stack.append((i, temp[i]))
                continue
            while stack and stack[-1][1] < temp[i]:
                idx, _ = stack.pop()
                res[idx] = i - idx
            stack.append((i, temp[i]))
        
        return res