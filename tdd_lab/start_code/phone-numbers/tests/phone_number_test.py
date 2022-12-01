import unittest
from src.phone_number import * 

class TestPhoneNumber(unittest.TestCase):
    
    def test_number_has_formatted(self):
        formatted_string = phone_number_formatter(1234567890)
        self.assertEqual("(123) 456-7890", formatted_string)

    