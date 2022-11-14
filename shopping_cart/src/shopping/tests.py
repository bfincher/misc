import unittest

from department import Department
from item_list import ItemList
from store import Store


class storeTest(unittest.TestCase):

    def setUp(self)->None:
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
