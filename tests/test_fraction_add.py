import unittest

from fraction import *
class TestFractionAdd(unittest.TestCase):
    """Tests for the __add__ method of Fraction class."""
    def setUp(self):
        """Set up common fractions for testing"""
        self.frac1 = Fraction(1, 2)
        self.frac2 = Fraction(1, 3)
        self.frac3 = Fraction(3, 4)
        self.frac4 = Fraction(-1, 4)
        self.frac5 = Fraction(0, 1)
        
    def test_add_same_denominator(self):
        """Test addition of fractions with the same denominator"""
        result = self.frac3 + self.frac4
        self.assertEqual(str(result), "1/2", "3/4 + (-1/4) should be 1/2")
        
    def test_add_diff_denominator(self):
        """Tests addition of fractions with different denominators"""
        result = self.frac1 + self.frac2
        self.assertEqual(str(result), "5/6", "1/2 + 1/3 should be 5/6")
        
    def test_add_negative_fractions(self):
        """Tests addition with a/an negative fraction"""
        result = self.frac2 + self.frac4
        self.assertEqual(str(result), "1/12", "1/3 + (-1/4) should be 1/12")
        
    def test_add_zero(self):
        """Tests addition with zero"""
        result = self.frac1 + self.frac5
        self.assertEqual(str(result), "1/2", "1/2 + 0 should be 1/2")
        
    def test_add_whole_number(self):
        """Test addition with a whole number"""
        result = self.frac3 + Fraction(2)
        self.assertEqual(str(result), "11/4", "3/4 + 2 should be 11/4(given 3 + 8 is 11)")
        
    def test_add_resulting_in_whole_number(self):
        """Test addition resulting in a whole number"""
        result = self.frac1 + self.frac1
        self.assertEqual(str(result), "1/1", "1/2 + 1/2 should be 1/1")