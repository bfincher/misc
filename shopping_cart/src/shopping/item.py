class Item:
    def __init__(self, name, itemId, deparment, price):
        self.name = name
        self.itemId = itemId
        self.department = deparment
        self.price = price
        
    def changePrice(self, newPrice):
        self.price = newPrice
        self.department.priceChangeNotification(self)
        
class ItemList:
    def __init__(self):
        self.items = []
        
    def addItem(self, item):
        self.items.append(item)
        
    def removeItem(self, item):
        self.items.remove(item)
        
    def getItems(self):
        return self.items
    
    def clearItems(self):
        self.items = []
        