# TODO Напишите функцию find_common_participants
def find_common_participants(string_1, string_2, sep=','):
    list_1 = string_1.split(sep)
    list_2 = string_2.split(sep)
    final_list = list(set(list_1).intersection(list_2))
    final_list.sort()
    return final_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, sep='|'))
