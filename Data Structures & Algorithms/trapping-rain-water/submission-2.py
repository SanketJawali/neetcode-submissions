class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
        trapped = 0
        l, r = 0, len(height) - 1

        maxL, maxR = height[l], height[r]
        # i = 0
        while l < r:
            # h = height[i]
            # currentTrapped = min(maxL, maxR) - h
            # if currentTrapped > 0:
            #     trapped += currentTrapped
            # print(maxL, maxR, currentTrapped)
            if maxL > maxR:
                r -= 1
                maxR = max(height[r], maxR)
                trapped += maxR - height[r]
            else:
                l += 1
                maxL = max(height[l], maxL)
                trapped += maxL - height[l]
            # i += 1
        return trapped
            
