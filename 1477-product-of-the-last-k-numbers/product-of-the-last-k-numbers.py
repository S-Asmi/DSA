class ProductOfNumbers:

    def __init__(self):
        self.cum_prod = []
        self.length = 0

    def add(self, num: int) -> None:
        if self.length == 0:
            if num != 0:
                self.cum_prod.append(num)
                self.length = 1
        else:
            if num == 0:
                self.cum_prod = []
                self.length = 0
            else:
                prod = self.cum_prod[-1] * num
                self.cum_prod.append(prod)
                self.length += 1

    def getProduct(self, k: int) -> int:
        if k > self.length:
            return 0

        divide = self.length - k - 1

        if divide == -1:
            return self.cum_prod[-1]

        return int(
            self.cum_prod[-1] /
            self.cum_prod[self.length - k - 1]
        )

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)