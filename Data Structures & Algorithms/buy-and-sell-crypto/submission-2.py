class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        while len(prices) > 1: 
            # find minimum price, find max price after min price
            # if min at end, pop it, find next min, if all prices in descending, return 0
            minIdx, maxIdx = 0, 0

            # Finding min price
            minIdx = self.findMinIdx(prices)
            # print(f"min: {minIdx}, {prices[minIdx]}")
                
            # If min price is at end, find second min
            while minIdx == len(prices) - 1 and len(prices) > 1:
                prices.pop()
                minIdx = self.findMinIdx(prices)

            # If there are less than 2 elements in the list, then there can't be a profit
            if len(prices) < 2:
                break
        
            # Finding max price after min price, start searching after minIdx
            maxIdx = self.findMaxIdx(prices, minIdx)
            # print(f"max: {maxIdx}, {prices[maxIdx]}")

            diff = prices[maxIdx] - prices[minIdx]

            # Remove the current min-max pair from prices
            prices.pop(maxIdx)
            prices.pop(minIdx)

            profit = diff if diff > profit else profit

        return profit
    
    def findMinIdx(self, prices: List[int]) -> int:
        minIdx = 0

        for i, price in enumerate(prices):
            if prices[minIdx] > price:
                minIdx = i

        return minIdx

    def findMaxIdx(self, prices: List[int], start) -> int:
        maxIdx = start

        for i in range(start, len(prices)):
            if prices[maxIdx] < prices[i]:
                maxIdx = i

        return maxIdx
            
