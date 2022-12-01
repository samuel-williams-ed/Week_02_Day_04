import unittest
from src.word_reverser import word_reverse

class TestWordReverse(unittest.TestCase):
    # def setUp(self):
        # test_line_1 = "Hello this is a test fantastic"
        # test_line_2 = "The cat was cute and he was called Azzazel"
        # test_line_3 = "Very cool hat"


    # Have unit tests for the following sentences 

    # "Hello this is a test, fantastic"
    # "The cat was cute and he was called Azzazel"
    # "Very cool hat"

    def test_line_1_is_reversed(self):
        reverser_string_1 = word_reverse("Hello this is a test fantastic")
        self.assertEqual("Hello this is a test citsatnaf", reverser_string_1)

    def test_line_2_is_reverser(self):
        reverser_string_2 = word_reverse("The cat was cute and he was called Azzazel")
        self.assertEqual("The cat was cute and he was dellac lezazzA", reverser_string_2)
    
    def test_line_3_is_reverser(self):
        reverser_string_3 = word_reverse("Very cool hat")
        self.assertEqual("Very cool hat", reverser_string_3)

    
