class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n=n
        self.disc=discount
        self.customer=0
        self.d={}
        for i in range(len(products)):
            self.d[products[i]]=prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer+=1
        ans=0
        for i in range(len(product)):
            ans+=amount[i]*(self.d[product[i]])
        if self.customer%self.n==0:
            return ans*((100-self.disc)/100)
        return ans


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)