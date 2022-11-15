import unittest

from customer import Customer
from department import Department, Entity
from item_list import ItemList
from store import Store

nextDepartmentId = 1

class EntityTest(unittest.TestCase):
    
    def setUp(self):
        self.entity = self.createEntity("testEntity")
        self.cust1 = Customer("cust1")
        self.cust2 = Customer("cust2")
        
    def createEntity(self, entityName):
        return Entity(entityName)
        
    def testConstruct(self):
        self.assertEqual("testEntity", self.entity.name)
        self.assertEqual(0, len(self.entity.getCustomers()))
        
    def testCustomersEnterExit(self):
        self.entity.enter(self.cust1)
        self.assertEqual(1, len(self.entity.getCustomers()))
        self.assertTrue(self.cust1 in self.entity.getCustomers())
        
        self.entity.enter(self.cust2)
        self.assertEqual(2, len(self.entity.getCustomers()))
        self.assertTrue(self.cust1 in self.entity.getCustomers())
        self.assertTrue(self.cust2 in self.entity.getCustomers())
        
        self.entity.exit(self.cust1)
        self.assertEqual(1, len(self.entity.getCustomers()))
        self.assertFalse(self.cust1 in self.entity.getCustomers())
        self.assertTrue(self.cust2 in self.entity.getCustomers())
        
        self.entity.exit(self.cust2)
        self.assertEqual(0, len(self.entity.getCustomers()))
    	
class DepartmentTest(EntityTest):

    def createEntity(self, entityName):
        global nextDepartmentId
        dept = Department(entityName, nextDepartmentId)        
        nextDepartmentId += 1
        return dept
    
    def testCustomerEnterExit(self):
        self.assertIsNone(self.cust1.departmentId)
        self.entity.enter(self.cust1)
        self.assertEqual(self.entity.departmentId, self.cust1.departmentId)
        self.entity.exit(self.cust1)
        self.assertIsNone(self.cust1.departmentId)
    
class StoreTest(unittest.TestCase):

    def setUp(self):
        self.store = Store("testStoreName")
        
    def testConstruct(self):
        self.assertEqual("testStoreName", self.store.name)
        self.assertTrue(isinstance(self.store.getShoppingCart(), ItemList))
        self.assertTrue(isinstance(self.store.getWishList(), ItemList))
        self.assertEqual(0, len(self.store.getDepartments()))
        
    def testAddDepartment(self):
        dept1 = Department("dept1", "1")
        self.store.addDepartment(dept1)
        
        dept2 = Department("dept2", "2")
        self.store.addDepartment(dept2)
        
        departments = self.store.getDepartments()
        self.assertEqual(2, len(departments))
        self.assertTrue(dept1 in departments)
        self.assertTrue(dept2 in departments)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
