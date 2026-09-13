class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # l[-10, -5, 0, l3, r6, 10]    k = 3     x = 4       [0, 3, 6]
        l, r = -1, 0
        
        # Find the position of x in array
        while r < len(arr) and not x < arr[r]:
            l += 1
            r += 1

        # Find K elements
        while k > 0:
            if l == -1:
                r += k
                break
            elif r == len(arr):
                l -= k
                break
            else:
                # Compare elements at l and r
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    l -= 1
                else:
                    r += 1
            k -= 1
        
        # Return array between l and r
        return arr[l + 1:r]