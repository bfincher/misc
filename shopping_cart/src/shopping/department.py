class Entity:
    def __init__(self, name):
        self.name = name
        self.customers = []
        
    def enter(self, customer):
        self.customers.append(customer);
        
    def exit(self, customer):
        self.customers.remove(customer)
    
    def customers(self):
        return self.customers

class Department(Entity):
    def __init__(self, name, departmentId):
        Entity.__init__(self, name)
        self.departmentId = departmentId
        self.items = []
        self.observers = []
        
    def items(self):
        return self.items
    
    def observers(self):
        return self.observers
    
    def addObserver(self, observer):
        self.observers.append(observer)


        