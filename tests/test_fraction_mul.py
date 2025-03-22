import unittest
from fraction import Fraction


class TestFractionMul(unittest.TestCase):
    """Tests for the __mul__ method of Fraction class."""
    
    def setUp(self):
        """Set up common fractions for testing"""
        self.f1 = Fraction(1, 2)
        self.f2 = Fraction(3, 4)
        self.f3 = Fraction(2, 3)
        self.f4 = Fraction(-3, 5)
        self.f5 = Fraction(0, 1)
        
    def test_mul_two_fractions(self):
        """Test multiplication of two fractions"""
        result = self.f1 * self.f2
        self.assertEqual(str(result), "3/8", "1/2 * 3/4 should be 3/8")
        
    def test_mul_with_negative(self):
        """Test multiplication with a negative fraction"""
        result = self.f3 * self.f4
        self.assertEqual(str(result), "-6/15", "2/3 * (-3/5) should be -6/15 or -2/5")
        
    def test_mul_with_zero(self):
        """Test multiplication with zero"""
        result = self.f1 * self.f5
        self.assertEqual(str(result), "0/1", "1/2 * 0 should be 0/1")
        
    def test_mul_with_one(self):
        """Test multiplication with one"""
        result = self.f2 * Fraction(1, 1)
        self.assertEqual(str(result), "3/4", "3/4 * 1 should be 3/4")
        
    def test_mul_whole_numbers(self):
        """Test multiplication of whole numbers as fractions"""
        result = Fraction(2) * Fraction(3)
        self.assertEqual(str(result), "6/1", "2 * 3 should be 6/1")
        
    def test_mul_needs_reduction(self):
        """Test multiplication that needs reduction"""
        result = self.f2 * self.f3
        self.assertEqual(str(result), "1/2", "3/4 * 2/3 should be 1/2")
        
    def test_mul_negative_numbers(self):
        """Test multiplication of negative numbers"""
        result = Fraction(-2, 3) * Fraction(-1, 4)
        self.assertEqual(str(result), "1/6", "(-2/3) * (-1/4) should be 1/6")


if __name__ == '__main__':
    unittest.main()