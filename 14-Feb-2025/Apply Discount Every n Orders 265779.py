# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products_prices_map = {}
        self.customer_counter = 0

        for i in range(len(products)):
            self.products_prices_map[products[i]] = prices[i]
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer_counter += 1
        bill = 0
        for j in range(len(product)):
            bill += amount[j] * self.products_prices_map[product[j]]
        if self.customer_counter % self.n == 0:
            bill = bill * ((100-self.discount)/100)
        return bill
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)