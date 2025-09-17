
#unit testing

#Step 2: Write a Unit Test

# import unittest 
# from math_utils import sub_numbers

# class TestMathUtils(unittest.TestCase):
#     def test_sub_numbers(self):   #one test method
#         # Test Case 1: Positive numbers
#         self.assertEqual(sub_numbers(10,20 ), 10)

#         # Test Case 2: Zero + number
#         self.assertEqual(sub_numbers(5, 20), 50)

#         # Test Case 3: Negative + positive
#         self.assertEqual(sub_numbers(30, 10), 20)

# if __name__ == "__main__": 
#     unittest.main()  

import unittest
from math_utils import sub_numbers

class TestMathUtils(unittest.TestCase):
    def test_sub_numbers_positive(self):
        # Test Case 1: Positive numbers
        self.assertEqual(sub_numbers(30, 10), 20)  # 30-10 = 20 ✅

    def test_sub_numbers_zero(self):
        # Test Case 2: Zero - number
        self.assertEqual(sub_numbers(0, 20), -20)  # 0-20 = -20 ✅

    def test_sub_numbers_negative(self):
        # Test Case 3: Negative - positive
        self.assertEqual(sub_numbers(-5, 10), -15)  # -5-10 = -15 ✅

if __name__ == "__main__":
    unittest.main()

