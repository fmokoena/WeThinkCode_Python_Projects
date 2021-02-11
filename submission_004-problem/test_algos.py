import unittest
import super_algos

class MyTestCase(unittest.TestCase):
    def test_find_min_empty(self):
        """ tests that the find_min function returns a -1 if an empty list is declared as a parameter"""
        result = super_algos.find_min([])
        self.assertEqual(-1, result)

    def test_find_min_non_int(self):
        """ tests that the find_min function returns a -1 if a list with characters that arent integers is declared as a parameter"""
        result = super_algos.find_min([1,"a",2,"b"])
        self.assertEqual(-1, result)

    def test_find_min_works(self):
        """ tests that the find_min function works as intended and finds the minimum value in a list of integers"""
        result = super_algos.find_min([44,11,33,50])
        self.assertEqual(11, result)

    def test_sum_all_empty(self):
        """ tests that the sum_all function returns a -1 if an empty list is declared as a parameter"""
        result = super_algos.sum_all([])
        self.assertEqual(-1, result)

    def test_sum_all_non_int(self):
        """ tests that the sum_all function returns a -1 if a list with characters that arent integers is declared as a parameter"""
        result = super_algos.sum_all([1,"a",2,"b"])
        self.assertEqual(-1, result)

    def test_sum_all_works(self):
        """ tests that the sum_all function works as intended and adds all the value in a list of integers and returns the total"""
        result = super_algos.sum_all([44,11,33,50])
        self.assertEqual(138, result)

    def test_find_possible_strings_empty(self):
        """ tests that the find_possible_strings function returns an empty list if an empty list is declared as a parameter"""
        result = super_algos.find_possible_strings([],3)
        self.assertEqual([], result)

    def test_find_possible_strings_not_int(self):
        """ tests that the find_possible_strings function returns an empty list if integers are declared as an argument for the set"""
        result = super_algos.find_possible_strings([1,2,3] , 3)
        self.assertEqual([], result)

    def test_find_possible_strings_works(self):
        """ tests that the find_possible_strings function works as intended and returns a list of all possible string combinations for a list of characrters of a given length"""
        result = super_algos.find_possible_strings(["x","y",], 2)
        self.assertEqual(["xx","xy","yx","yy"], result)

if __name__ == "__main__":
    unittest.main()