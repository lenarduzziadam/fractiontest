import unittest

from fraction import *
class TestFractionAdd(unittest.TestCase):
    """Tests for the __add__ method of Fraction class."""
    def setUp(self):
        """Set up common fractions for testing"""
        self.f1 = Fraction(1, 2)
        self.f2 = Fraction(1, 3)
        self.f3 = Fraction(3, 4)
        self.f4 = Fraction(-1, 4)
        self.f5 = Fraction(0, 1)
        
    def test_add_same_denominator(self):
        """Test addition of fractions with the same denominator"""
        result = self.f3 + self.f4
        self.assertEqual(str(result), "1/2", "3/4 + (-1/4) should be 1/2")
        
    def test_add_different_denominator(self):
        """Test addition of fractions with different denominators"""
        result = self.f1 + self.f2
        self.assertEqual(str(result), "5/6", "1/2 + 1/3 should be 5/6")
        
    def test_add_negative_fractions(self):
        """Test addition with a negative fraction"""
        result = self.f2 + self.f4
        self.assertEqual(str(result), "1/12", "1/3 + (-1/4) should be 1/12")
        
    def test_add_zero(self):
        """Test addition with zero"""
        result = self.f1 + self.f5
        self.assertEqual(str(result), "1/2", "1/2 + 0 should be 1/2")
        
    def test_add_whole_number(self):
        """Test addition with a whole number"""
        result = self.f3 + Fraction(2)
        self.assertEqual(str(result), "11/4", "3/4 + 2 should be 11/4")
        
    def test_add_resulting_in_whole_number(self):
        """Test addition resulting in a whole number"""
        result = self.f1 + self.f1
        self.assertEqual(str(result), "1/1", "1/2 + 1/2 should be 1/1")