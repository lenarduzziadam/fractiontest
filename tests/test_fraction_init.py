import unittest
from fraction import Fraction


class TestFractionInit(unittest.TestCase):
    #Tests for the __init__ method of Fraction class.
    
    def test_init_with_two_integers(self):
        #Test initialization with two integers
        f = Fraction(2, 4)
        self.assertEqual(str(f), "1/2", "Fraction(2, 4) should be reduced to 1/2")
        
    def test_init_with_one_integer(self):
        #Test initialization with one integer
        f = Fraction(5)
        self.assertEqual(str(f), "5/1", "Fraction(5) should create 5/1")
        
    def test_init_with_negative_numbers(self):
        #Test initialization with negative numbers
        f1 = Fraction(-3, 6)
        self.assertEqual(str(f1), "-1/2", "Fraction(-3, 6) should be reduced to -1/2")
        
        f2 = Fraction(3, -6)
        self.assertEqual(str(f2), "-1/2", "Fraction(3, -6) should be reduced to -1/2")
        
        f3 = Fraction(-3, -6)
        self.assertEqual(str(f3), "1/2", "Fraction(-3, -6) should be reduced to 1/2")
        
    def test_init_with_zero_numerator(self):
        #Test initialization with zero numerator
        f = Fraction(0, 5)
        self.assertEqual(str(f), "0/1", "Fraction(0, 5) should be reduced to 0/1")
        
    def test_init_with_zero_denominator(self):
        #Test initialization with zero denominator
        with self.assertRaises(ZeroDivisionError, msg="Should raise ZeroDivisionError when denominator is 0"):
            Fraction(5, 0)
            
    def test_init_with_float(self):
        #Test initialization with a float should raise TypeError
        with self.assertRaises(TypeError, msg="Should raise TypeError when numerator is a float"):
            Fraction(2.4)
            
        with self.assertRaises(TypeError, msg="Should raise TypeError when denominator is a float"):
            Fraction(1, 2.5)


if __name__ == '__main__':
    unittest.main()