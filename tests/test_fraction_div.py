import unittest
from fraction import Fraction

class TestFractionDiv(unittest.TestCase):
    """Tests for the __truediv__ method of Fraction class."""
    
    def setUp(self):
        """Set up common fractions for testing"""
        self.f1 = Fraction(1, 2)
        self.f2 = Fraction(1, 4)
        self.f3 = Fraction(3, 5)
        self.f4 = Fraction(-2, 3)
        self.f5 = Fraction(0, 1)
        self.f6 = Fraction(7)
        
    def test_div_simple_fractions(self):
        """Test division of simple fractions"""
        res = self.f1 / self.f2
        self.assertEqual(str(res), "2/1", "1/2 / 1/4 should be 2/1")
        
    def test_div_with_negative(self):
        """Test division with a negative fraction"""
        res = self.f3 / self.f4
        self.assertEqual(str(res), "-9/10", "3/5 / (-2/3) should be -9/10")
        
    def test_div_by_zero(self):
        """Test exception raised division by zero should raise ZeroDivisionError"""
        with self.assertRaises(ZeroDivisionError, msg="Division by zero should raise ZeroDivisionError"):
            self.f1 / self.f5
            
    def test_zero_div(self):
        """Test zero divided by a fraction"""
        result = self.f5 / self.f1
        self.assertEqual(str(result), "0/1", "0 / 1/2 should be 0/1")
        
    def test_div_by_whole_number(self):
        """Test division by a whole number"""
        result = self.f1 / self.f6
        self.assertEqual(str(result), "1/14", "1/2 / 7 should be 1/14")
        
    def test_div_complex_needs_reduction(self):
        """Test complex division that needs reduction"""
        f1 = Fraction(2, 3)
        f2 = Fraction(4, 9)
        result = f1 / f2
        self.assertEqual(str(result), "3/2", "2/3 / 4/9 should be 3/2")
        
    def test_div_by_negative(self):
        """Test division by a negative number"""
        result = Fraction(3, 4) / Fraction(-3, 2)
        self.assertEqual(str(result), "-1/2", "3/4 / (-3/2) should be -1/2")
        
    def test_div_fraction_by_itself(self):
        """Test division of a fraction by itself"""
        result = self.f3 / self.f3
        self.assertEqual(str(result), "1/1", "3/5 / 3/5 should be 1/1")


if __name__ == '__main__':
    unittest.main()
