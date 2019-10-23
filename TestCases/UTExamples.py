import unittest
from Examples import Math


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("First run")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Last Run")

    def setUp(self) :
        print("This is the first step for unit testing")

    def tearDown(self) -> None:
        print("This is second step for unit testing")


    def test_add(self):
        results = Math.add(self,10, 20)
        self.assertEqual(results, 30)

    def test_sub(self):
        results = Math.sub(self,50, 20)
        self.assertEqual(results, 30)


    # def test_something(self):
    #     self.assertEqual(True, False)


 # if __name__ == '__main__':
 #     unittest.main()
