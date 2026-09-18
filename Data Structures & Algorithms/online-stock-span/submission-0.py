class StockSpanner:
    # [3, 8, 1, 2, 5, 9, 7]
    # [1, 2, 1, 2, 3, 6, 1]
    def __init__(self):
        self.prices = []
        self.day = 0

    def next(self, price: int) -> int:
        print(self.prices)
        self.day += 1
        if len(self.prices) == 0:
            self.prices.append((price, self.day))
            return 1

        while self.prices and self.prices[-1][0] <= price:
            self.prices.pop()
        if len(self.prices) > 0:
            _, d = self.prices[-1]
            self.prices.append((price, self.day))
            return self.day - d
        self.prices.append((price, self.day))
        return self.day

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)