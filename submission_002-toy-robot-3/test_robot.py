import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import robot
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    def test_step1_then_off(self):

        with captured_io(StringIO('HAL\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Shutting down..""", output)

    @patch('sys.stdin', StringIO('HAL\nhelp\noff\n'))
    def test_help(self):
        self.maxDiff = None
        output = StringIO()
        sys.stdout = output

        robot.robot_start()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all commands entered
REPLAY SILENT - replays all commands entered silently
REPLAY REVERSED - replays all commands entered in reverse
REPLAY REVERSED SILENT - replays all commands entered in reverse silently
HAL: What must I do next? HAL: Shutting down..\n""", output.getvalue())


    @patch('sys.stdin', StringIO('HAL\nforward 10\noff\n'))
    def test_forward(self):
        
        output = StringIO()
        sys.stdout = output

        robot.robot_start()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Shutting down..\n""", output.getvalue())

    @patch('sys.stdin', StringIO('HAL\nFORWARD 10\noff\n'))
    def test_uppercase(self):
        
        output = StringIO()
        sys.stdout = output

        robot.robot_start()
    
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Shutting down..\n""", output.getvalue())

    @patch('sys.stdin', StringIO('HAL\nback 10\noff\n'))
    def test_uppercase(self):
        # self.maxDiff = None
        
        output = StringIO()
        sys.stdout = output

        robot.robot_start()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (0,-10).
HAL: What must I do next? HAL: Shutting down..\n""", output.getvalue())

    @patch('sys.stdin', StringIO('HAL\nright\noff\n'))
    def test_turn_right(self):
        
        output = StringIO()
        sys.stdout = output

        robot.robot_start()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..\n""", output.getvalue())

    @patch('sys.stdin', StringIO('HAL\nleft\noff\n'))
    def test_turn_left(self):
        
        output = StringIO()
        sys.stdout = output

        robot.robot_start()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..\n""", output.getvalue())

    @patch('sys.stdin', StringIO('HAL\nforward 201\nforward 10\noff\n'))
    def test_turn_left(self):
        
        output = StringIO()
        sys.stdout = output

        robot.robot_start()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Sorry, I cannot go outside my safe zone.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Shutting down..\n""", output.getvalue())

    @patch('sys.stdin', StringIO('HAL\nright\nforward 101\nforward 10\noff\n'))
    def test_turn_left(self):
        
        output = StringIO()
        sys.stdout = output

        robot.robot_start()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Sorry, I cannot go outside my safe zone.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (10,0).
HAL: What must I do next? HAL: Shutting down..\n""", output.getvalue())

    @patch('sys.stdin', StringIO('Hal\nforward 10\nreplay\noff\n'))
    def test_replay(self):
        
        output = StringIO()
        sys.stdout = output

        robot.robot_start()
        self.assertEqual("""What do you want to name your robot? Hal: Hello kiddo!
Hal: What must I do next?  > Hal moved forward by 10 steps.
 > Hal now at position (0,10).
Hal: What must I do next?  > Hal moved forward by 10 steps.
 > Hal now at position (0,20).
 > Hal replayed 1 commands.
 > Hal now at position (0,20).
Hal: What must I do next? Hal: Shutting down..\n""", output.getvalue())

    @patch('sys.stdin', StringIO('Hal\nforward 10\nreplay reversed\noff\n'))
    def test_replay_reverse(self):
        self.maxDiff = None
        output = StringIO()
        sys.stdout = output

        robot.robot_start()
        self.assertEqual("""What do you want to name your robot? Hal: Hello kiddo!
Hal: What must I do next?  > Hal moved forward by 10 steps.
 > Hal now at position (0,10).
Hal: What must I do next?  > Hal moved forward by 10 steps.
 > Hal now at position (0,20).
 > Hal replayed 1 commands in reverse.
 > Hal now at position (0,20).
Hal: What must I do next? Hal: Shutting down..\n""",output.getvalue())

    @patch('sys.stdin', StringIO('a\nforward 10\nforward 10\nreplay silent\noff\n'))
    def test_replay_silent(self):
        
        output = StringIO()
        sys.stdout = output

        robot.robot_start()
        self.assertEqual("""What do you want to name your robot? a: Hello kiddo!
a: What must I do next?  > a moved forward by 10 steps.
 > a now at position (0,10).
a: What must I do next?  > a moved forward by 10 steps.
 > a now at position (0,20).
a: What must I do next?  > a replayed 2 commands silently.
 > a now at position (0,40).
a: What must I do next? a: Shutting down..\n""",output.getvalue())


    @patch('sys.stdin', StringIO('a\nforward 10\nforward 10\nreplay reversed silent\noff\n'))
    def test_replay_silent_reverse(self):
        self.maxDiff = None
        output = StringIO()
        sys.stdout = output

        robot.robot_start()
        self.assertEqual("""What do you want to name your robot? a: Hello kiddo!
a: What must I do next?  > a moved forward by 10 steps.
 > a now at position (0,10).
a: What must I do next?  > a moved forward by 10 steps.
 > a now at position (0,20).
a: What must I do next?  > a replayed 2 commands in reverse silently.
 > a now at position (0,40).
a: What must I do next? a: Shutting down..\n""",output.getvalue())

if __name__ == '__main__':
    unittest.main()