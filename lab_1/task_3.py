list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
num_of_one_team = int(len(list_players) / 2)
first_team = list_players[:num_of_one_team]
second_team = list_players[num_of_one_team:]
print(first_team)
print(second_team)
