import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):

    def setUp(self):
        self.list_of_scores = [100, 0, 90, 30]

    def test_high_score(self):
        self.assertEqual(100,personal_best(self.list_of_scores))

    def test_last_score_added(self):
        self.assertEqual(30, latest(self.list_of_scores))

    def test_personal_top_three(self):
        self.assertEqual([100,90,30], personal_top_three(self.list_of_scores))


    # Tests

    # Test latest score (the last thing in the list)

    # Test personal best (the highest score in the list)

    # Test top three from list of scores

    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    
