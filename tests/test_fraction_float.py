import unittest
from fraction import Fraction


class TestFractionFloat(unittest.TestCase):
    """Tests for the __float__ method of Fraction class."""
    
    def test_float_half(self):
        """Test float value of 1/2"""
        f = Fraction(1, 2)
        self.assertEqual(float(f), 0.5, "Float of Fraction(1, 2) should be 0.5")
        
    def test_float_three_quarters(self):
        """Test float value of 3/4"""
        f = Fraction(3, 4)
        self.assertEqual(float(f), 0.75, "Float of Fraction(3, 4) should be 0.75")
        
    def test_float_negative_fraction(self):
        """Test float value of a negative fraction"""
        f = Fraction(-5, 8)
        self.assertEqual(float(f), -0.625, "Float of Fraction(-5, 8) should be -0.625")
        
    def test_float_zero(self):
        """Test float value of 0/1"""
        f = Fraction(0, 10)
        self.assertEqual(float(f), 0.0, "Float of Fraction(0, 10) should be 0.0")
        
    def test_float_whole_number(self):
        """Test float value of a whole number"""
        f = Fraction(7)
        self.assertEqual(float(f), 7.0, "Float of Fraction(7) should be 7.0")
        
    def test_float_reduced_fraction(self):
        """Test float value of a fraction that gets reduced"""
        f = Fraction(25, 100)
        self.assertEqual(float(f), 0.25, "Float of Fraction(25, 100) should be 0.25")
        
    def test_float_large_numbers(self):
        """Test float value with large numbers"""
        f = Fraction(1000000, 1000)
        self.assertEqual(float(f), 1000.0, "Float of Fraction(1000000, 1000) should be 1000.0")


if __name__ == '__main__':
    unittest.main()
