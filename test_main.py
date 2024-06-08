import unittest
from main import add, subtrack
class TestMain(unittest.TestCase):
    def test_add(self):
        selfassertEqual(add(2,3),5)
        selfassertEqual(add(-1,1),0)

        def test_subtrack(self):
            selfasserEqual(subtrack(5,3),2)
            selfassertEqual(subtrack(2,4),-2)

            if_name=='_main_':
            unittest.main()