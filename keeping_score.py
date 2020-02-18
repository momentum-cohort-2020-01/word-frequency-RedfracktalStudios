test_name_list = ["Marsha", "Purusha", "Legend"]


def make_scorecard(names):
    score_dict = {}
    for name in names:
        print(name)
        score_dict[name] = 0
    print(score_dict)
    return(score_dict)


def update_score(score_dict):
    for name, score in score_dict.items():
        print(name)
        score_dict[name += 1]
        print(f'{name}:{score}')


def play_game():
    update score(make_scorecared(test_name_list))


play_game
