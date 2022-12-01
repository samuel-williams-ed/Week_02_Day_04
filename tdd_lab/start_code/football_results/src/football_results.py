list_of_scores = [{    
    "home_score": 0,
    "away_score": 1},
    {    
    "home_score": 0,
    "away_score": 1}
    ,{    
    "home_score": 0,
    "away_score": 1}
    ,{    
    "home_score": 0,
    "away_score": 1}
    ]

def get_result(final_score):
    home_score = final_score["home_score"]
    away_score = final_score["away_score"]
    if home_score > away_score:
        return "Home win"
    elif home_score < away_score:
        return "Away win"
    else:
        return "Draw"

def get_results(final_scores):
    final_score_tests = []
    for result in final_scores:
        result_string = get_result(result)
        final_score_tests.append(result_string)
    return final_score_tests
        