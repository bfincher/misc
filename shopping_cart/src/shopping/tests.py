import unittest
from store import Store


class storeTest(unittest.TestCase):

    def setUp(self)->None:
        self.store = Store("testStoreName")
        
    def testConstruct(self):
        self.assertEqual("testStoreName", self.store.name)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
