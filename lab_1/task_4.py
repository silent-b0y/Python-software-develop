users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
visitings = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
all_visitings = len(users)
visitings["Общее количество"] = all_visitings
unique_users = set(users)
unique_visitings = len(unique_users)
visitings["Уникальные посещения"] = unique_visitings
print(visitings)
