import unittest
import sortByCalc

class TestWeek6Sort(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sortByCalc.countSort([3,8,1,10,12,4]),[1,3,4,8,10,12])

    def test_2(self):
        self.assertEqual(sortByCalc.countSort([13,11,9,7,4,1]),[1,4,7,9,11,13])

    def test_3(self):
        self.assertEqual(sortByCalc.countSort(list(map(int, '9 8 7 6 5 4 3 2 1 0'.split()))), list(map(int, '0 1 2 3 4 5 6 7 8 9'.split())))

    def test_4(self):
        self.assertEqual(sortByCalc.countSort(list(map(int, '1 2 3 4 5 6 7 8 9 10'.split()))), list(map(int, '1 2 3 4 5 6 7 8 9 10'.split())))

unittest.main()
