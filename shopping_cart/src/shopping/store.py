from department import Department, Entity
from item import ItemList


class Store(Entity):
    def __init__(self, name):
        Entity.__init__(self, name)
        self.departments = []
        self.totalSales = 0
        
    def getShoppingCart(self):
        return ItemList()
    
    def getWishList(self):
        return ItemList()
    
    def getDepartments(self):
        return self.departments
    
    def addDepartment(self, department):
        self.departments.append(department)
        
    def exit(self, customer):
        Entity.exit(self, customer)
        if customer.shoppingCart:
            print(f"Checking out customer {customer.name}")
            print("Items purchased:")
            total = 0
            for item in customer.shoppingCart.getItems():
                print(f"    {item.name} ${item.price}")
                total += item.price
            
            print(f"Total = {total}")
            self.totalSales += total
            
                    
        