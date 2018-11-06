import unittest
import sortByCalc

class TestWeek6Sort(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sortByCalc.countSort([3,8,1,10,12,4]),[1,3,4,8,10,12])


unittest.main()
