
class ItemList:

    def __init__(self):
        self.items = []
        
    def addItem(self, item):
        self.items.append(item)
        
    def removeItem(self, item):
        self.items.remove(item)
        
    def items(self):
        return self.items
        