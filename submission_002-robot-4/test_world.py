import unittest
from io import StringIO
import sys
# import world.obstacles as obstacles
from world import obstacles
import robot
from unittest.mock import patch

class MyTestCase(unittest.TestCase):
    @patch('sys.stdin',StringIO("Hal\nleft\nforward 2\noff"))
    def test_left(self):
        obstacles.random.randint = lambda a, b: 0
        #self.maxDiff = None
        output = StringIO()
        sys.stdout = output
        robot.robot_start()
        self.assertEqual('''What do you want to name your robot? Hal: Hello kiddo!
Hal: What must I do next?  > Hal turned left.
 > Hal now at position (0,0).
Hal: What must I do next?  > Hal moved forward by 2 steps.
 > Hal now at position (-2,0).
Hal: What must I do next? Hal: Shutting down..\n''',output.getvalue())

    @patch('sys.stdin', StringIO("Hal\nforward 10\noff\n"))
    def test_forward(self):
        self.maxDiff = None
        
        obstacles.random.randint = lambda a, b: 0
        output = StringIO()
        sys.stdout = output
        
        
        robot.robot_start()
        
        self.assertEqual('''What do you want to name your robot? Hal: Hello kiddo!
Hal: What must I do next?  > Hal moved forward by 10 steps.
 > Hal now at position (0,10).
Hal: What must I do next? Hal: Shutting down..\n''',output.getvalue())

    @patch('sys.stdin', StringIO("Hal\nBack 5\noff"))
    def test_back(self):
        self.maxDiff = None
        obstacles.random.randint = lambda a, b: 0
        output = StringIO()
        sys.stdout = output
        robot.robot_start()
        self.assertEqual('''What do you want to name your robot? Hal: Hello kiddo!
Hal: What must I do next?  > Hal moved back by 5 steps.
 > Hal now at position (0,-5).
Hal: What must I do next? Hal: Shutting down..\n''',output.getvalue())

    @patch('sys.stdin',StringIO("Hal\nright\nforward 2\noff"))
    def test_right(self):
        obstacles.random.randint = lambda a, b: 0
        #self.maxDiff = None
        output = StringIO()
        sys.stdout = output
        robot.robot_start()
        self.assertEqual('''What do you want to name your robot? Hal: Hello kiddo!
Hal: What must I do next?  > Hal turned right.
 > Hal now at position (0,0).
Hal: What must I do next?  > Hal moved forward by 2 steps.
 > Hal now at position (2,0).
Hal: What must I do next? Hal: Shutting down..\n''',output.getvalue())

if __name__ == "__main__":
    unittest.main()