class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            # print(stack, temp)
            if len(stack) == 0:
                stack.append((temp, i))
                continue
            
            if stack[-1][0] >= temp:
                stack.append((temp, i))
            else:
                while len(stack) > 0 and stack[-1][0] < temp:
                    top = stack.pop()
                    res[top[1]] = i - top[1]
                    # print(i, top[1], res)
                stack.append((temp, i))
            
        return res