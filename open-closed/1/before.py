

class Order:

    def __init__(self, totalWeight) -> None:
        self.lineItems = []
        self.shipping = ''
        self.totalWeight = totalWeight

    def getTotal():
        pass

    def getTotalWeight(self):
        return self.totalWeight

    def setShippingType(self, shipping):
        self.shipping = shipping

    def getShippingCost(self):
        if self.shipping == 'ground':
            if self.getTotal() > 100:
                return 0
            return self.getTotalWeight() * 10
        
        if self.shipping == 'air':
            return self.getTotalWeight() * 3

    def getShippingDate():
        pass


order1 = Order(20)
order1.setShippingType('air')
print(order1.getShippingCost())