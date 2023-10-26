users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
visitings = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
visitings["Общее количество"] = len(users)
visitings["Уникальные посещения"] = len(set(users))
print(visitings)
