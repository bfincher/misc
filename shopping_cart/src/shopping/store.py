from department import Entity
from item_list import ItemList

class Store(Entity):
    def __init__(self, name):
        Entity.__init__(self, name)
        self.departments = []
        
    def getShoppingCart(self):
        return ItemList()
    
    def getWishList(self):
        return ItemList()
    
    def departments(self):
        return self.departments
    
    def addDepartment(self, department):
        self.departments.append(department)
