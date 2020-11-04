import mastermind
import unittest
import sys 
from unittest.mock import patch
from io import StringIO
from test_base import captured_io
from contextlib import redirect_stderr, redirect_stdout

def get_answer_input():
    return input('Enter your guess: ') 

class TestCase(unittest.TestCase):
#test to check create_code
    def test_create_code(self):
        for i in range(100):
            self.assertEqual(len(mastermind.create_code()), 4)
            for r in range(4):
                self.assertGreater(mastermind.create_code()[r], 0)
                self.assertLess(mastermind.create_code()[r], 9)

    def test_check_correctness(self):
        out = StringIO()
        with redirect_stdout(out):
            self.assertEqual(mastermind.check_correctness(4, 0), True)
            self.assertEqual(mastermind.check_correctness(5, 3), False)

    # def test_get_user_input(self):
    #     self.assertEqual(len(mastermind.get_user_input()), 4)

    # @patch("sys.stdin", StringIO("123\n12345\n1234"))
    def test_compare(self):
        with captured_io(StringIO("123\n12345\n1234")):
            self.assertEqual(len(mastermind.get_user_input()), 4)
    
    def test_take_turn(self):
        code = [1, 2, 3, 4]
        out = StringIO()
        with redirect_stdout(out):
        #with  captured_io(StringIO("5678\n8765\n5687")):
            attempt = mastermind.take_turn(code, "1234")
            self.assertEqual((attempt[0], attempt[1]), (4, 0))

            attempt = mastermind.take_turn(code,"4321")
            self.assertEqual((attempt[0], attempt[1]), (0, 4))

            attempt = mastermind.take_turn(code,"1243")
            self.assertEqual((attempt[0], attempt[1]), (2, 2))

            attempt = mastermind.take_turn(code,"1423")
            self.assertEqual((attempt[0], attempt[1]), (1, 3))
    

# if __name__ == "__main__":
#     unittest.main()