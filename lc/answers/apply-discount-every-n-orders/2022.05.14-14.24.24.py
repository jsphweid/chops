class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.i = 0
        self.n = n
        self.discount = (100 - discount) / 100
        self.products_to_prices = {x: y for x, y in zip(products, prices)}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.i += 1
        gets_discount = self.i % self.n == 0
        total = 0
        for p, q in zip(product, amount):
            total += self.products_to_prices[p] * q
        return total * self.discount if gets_discount else total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)