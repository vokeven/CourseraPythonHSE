import unittest
import maxScore

class TestMaxScore(unittest.TestCase):
    def test_1(self):
        self.assertEqual(maxScore.calcMaxScore('c:\\input1.txt'), list(map(int, '91 86 99'.split())))
    def test_2(self):
        self.assertEqual(maxScore.calcMaxScore('c:\\input2.txt'), list(map(int, '0 0 0'.split())))

unittest.main()
