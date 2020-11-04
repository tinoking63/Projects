import unittest
from io import StringIO
import sys
from world import obstacles
import robot
from unittest.mock import patch

class MyTestCase(unittest.TestCase):
    def test_obstacles(self):
        obstacles.list_co = [(4,5)]
        self.assertTrue(obstacles.is_position_blocked(8,6), True)


    def test_obstacles_fail_position(self):
        obstacles.list_co = [(4,5)]
        self.assertFalse(obstacles.is_position_blocked(34,12), True)


    def test_obstacles_fail(self):
        obstacles.list_co = [(4,5)]
        self.assertFalse(obstacles.is_path_blocked(12,65,56,67),False)


    def test_obstacles_true(self):
        obstacles.list_co = [(12,16)]
        self.assertTrue(obstacles.is_position_blocked(13,17), True)


    def test_path_blocked(self):
        obstacles.list_co = [(12,16)]
        self.assertTrue(obstacles.is_path_blocked(12,17,56,67),True)


    def test_path_blocked_fail(self):
        obstacles.list_co = [(12,70)]
        self.assertFalse(obstacles.is_path_blocked(12,17,56,67),True)

    
if __name__ == "__main__":
    unittest.main()