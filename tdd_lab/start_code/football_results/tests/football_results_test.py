import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    # if __name__ == "__main__":
    #     unittest.main()

    def setUp(self):
        self.test_list_of_scores = [{    
        "home_score": 2,
        "away_score": 2},
        {    
        "home_score": 4,
        "away_score": 3}
        ,{    
        "home_score": 0,
        "away_score": 1}
        ]
        
        self.dictionary_draw = {    
        "home_score": 2,
        "away_score": 2}
        self.dictionary_home_win = {    
        "home_score": 4,
        "away_score": 3}
        self.dictionary_away_win = {    
        "home_score": 0,
        "away_score": 1}

    def test_get_result(self):
        self.assertEqual("Draw", get_result(self.dictionary_draw))
        self.assertEqual("Away win", get_result(self.dictionary_away_win))
        self.assertEqual("Home win", get_result(self.dictionary_home_win))
    
    def test_get_results(self):
        self.assertEqual(["Draw", "Home win", "Away win"], get_results(self.test_list_of_scores))
