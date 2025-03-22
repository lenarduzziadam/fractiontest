import unittest
from fraction import Fraction

class TestFractionStr(unittest.TestCase):
    """Tests for the __str__ method of Fraction class."""
    
    def setUp(self):
        """Set up common fractions for testing"""
        self.f1 = Fraction(1, 2)
        self.f2 = Fraction(3, 4)
        self.f3 = Fraction(-5, 6)
        self.f4 = Fraction(0, 7)
        self.f5 = Fraction(8)
        self.f6 = Fraction(-10)
        
    def test_str_positive_fraction(self):
        """Test string representation of a positive fraction"""
        self.assertEqual(str(self.f1), "1/2", "String of Fraction(1, 2) should be '1/2'")
        
    def test_str_another_positive_fraction(self):
        """Test string representation of another positive fraction"""
        self.assertEqual(str(self.f2), "3/4", "String of Fraction(3, 4) should be '3/4'")
        
    def test_str_negative_fraction(self):
        """Test string representation of a negative fraction"""
        self.assertEqual(str(self.f3), "-5/6", "String of Fraction(-5, 6) should be '-5/6'")
        
    def test_str_zero_fraction(self):
        """Test string representation of a zero fraction"""
        self.assertEqual(str(self.f4), "0/1", "String of Fraction(0, 7) should be '0/1'")
        
    def test_str_positive_whole_number(self):
        """Test string representation of a positive whole number as fraction"""
        self.assertEqual(str(self.f5), "8/1", "String of Fraction(8) should be '8/1'")
        
    def test_str_negative_whole_number(self):
        """Test string representation of a negative whole number as fraction"""
        self.assertEqual(str(self.f6), "-10/1", "String of Fraction(-10) should be '-10/1'")


if __name__ == '__main__':
    unittest.main()
