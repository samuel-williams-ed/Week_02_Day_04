import unittest

from src.compound_interest import CompoundInterest

class CompoundInterestTest(unittest.TestCase):
    pass
    # Tests

    # Should return 732.81 given 100 principal, 10 percent, 20 years
    def test_one(self):
        self.test_one_object = CompoundInterest(100, 0.10)
        self.assertEqual(732.81, self.test_one_object.calculate_amount(20))
    

    # Should return 181.94 given 100 principal, 6 percent, 10 years
    def test_two(self):
        self.test_two_object = CompoundInterest(100, 0.06)
        self.assertEqual(181.94, self.test_two_object.calculate_amount(10))

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years
    def test_three(self):
        self.test_three_object = CompoundInterest(100000, 0.05)
        self.assertEqual(149058.55, self.test_three_object.calculate_amount(8))

    # Should return 0.00 given 0 principal, 10 percent, 1 year
    def test_fout(self):
        self.test_fout_object = CompoundInterest(0, 0.1)
        self.assertEqual(0.00, self.test_fout_object.calculate_amount(1))

    # Should return 100.00 given 100 principal, 0 percent, 10 years
    

    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month

