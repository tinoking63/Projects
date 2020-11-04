import super_algos
import unittest
from test_base import captured_io

class Mytestcase(unittest.TestCase):
    def test_minfind_filled(self):
        check = [1, 2, 3, 4, 5]
        self.assertEqual(super_algos.find_min(check), 1)
        # self.assertEqual(super_algos.find_min(check), 0)
    def test_minfind_filled(self):
        check = []
        self.assertEqual(super_algos.find_min(check),-1)

    def test_sum_all(self):
        check = [1,2,3,4,5,6]
        self.assertEqual(super_algos.sum_all(check),21)
    def test_sum_all(self):
        check = []
        self.assertEqual(super_algos.sum_all(check),-1)

    def test_character_combo(self):
        check = ['a','b']
        self.assertEqual(super_algos.find_possible_strings(check,1),['a','b'])
        self.assertEqual(super_algos.find_possible_strings(check,2),['aa','ab','ba','bb',],)
        self.assertEqual(super_algos.find_possible_strings(check,3),['aaa','aab','aba','abb','baa','bab','bba','bbb'])
