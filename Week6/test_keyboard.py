import unittest
import keyboard

class TestWeek6Keyboard(unittest.TestCase):
    def test_1(self):
        self.assertEqual(keyboard.isKeyboardBroke(5, list(map(int, '1 50 3 4 3'.split())), \
                                                  16, list(map(int, '1 2 3 4 5 1 3 3 4 5 5 5 5 5 4 5'.split()))),\
                         ['YES', 'NO', 'NO', 'NO', 'YES'])

    def test_2(self):
        self.assertEqual(keyboard.isKeyboardBroke(3, list(map(int, '2 15 3'.split())), \
                                                  10, list(map(int, '1 1 1 2 3 3 3 3 3 3'.split()))), \
                         ['YES', 'NO', 'YES'])
    
unittest.main()
