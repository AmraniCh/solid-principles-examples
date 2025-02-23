
from abc import ABC, abstractmethod

class Shipping(ABC):
    @abstractmethod
    def getCost() -> int:
        pass

class GroundShipping(Shipping):

    def getCost(order) -> int:
        if order.getTotal() > 100:
            return 0
        return order.getTotalWeight() * 10

    def getDate():
        pass

class AirShipping(Shipping):

    def getCost(order) -> int:
        return order.getTotalWeight() * 3

    def getDate():
        pass



class Order:

    def __init__(self, totalWeight: int) -> None:
        self.lineItems = []
        self.shipping = ''
        self.totalWeight = totalWeight

    def setShipping(self, shipping: Shipping):
        self.shipping = shipping

    def getShippingCost(self):
        return self.shipping.getCost(self)

    def getTotal(self) -> int:
        return 80 # 80 dollars order

    def getTotalWeight(self) -> int:
        return self.totalWeight

# Usage
order1 = Order(20)

order1.setShipping(GroundShipping)
print(order1.getShippingCost())

order1.setShipping(AirShipping)
print(order1.getShippingCost())