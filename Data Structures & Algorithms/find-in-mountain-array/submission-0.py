class Solution:
    def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
        n = arr.length()

        # find peak
        l, r = 1, n - 2
        peak = 0
        while l <= r:
            m = l + ((r - l) // 2)
            ml, mid, mr = arr.get(m - 1), arr.get(m), arr.get(m + 1)

            if ml < mid < mr:
                # Mid on left side of peak
                l = m + 1
            elif ml > mid > mr:
                # Mid on right side of peak
                r = m - 1
            else:
                # mid at peak
                peak = m
                break

        # Search target on left side
        l, r = 0, peak
        while l <= r:
            m = l + ((r - l) // 2)
            mid = arr.get(m)

            if mid == target:
                return m
            elif mid < target:
                l = m + 1
            else:
                r = m - 1

        # search target on right side
        l, r = peak, n - 1
        while l <= r:
            m = l + ((r - l) // 2)
            mid = arr.get(m)
            
            if mid == target:
                return m
            elif mid > target:
                l = m + 1
            else:
                r = m - 1
        
        return -1