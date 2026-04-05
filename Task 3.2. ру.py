# TODO Напишите функцию find_common_participants
def find_common_participants(first,second,dev = ','):
    fixed_first = first.split(dev)  # Множество участников первой группы без разделителей
    fixed_second = second.split(dev)  # Множество участников второй группы без разделителей
    common_parts=[]  # Список общих участников
    for i in fixed_first:
        if i in fixed_second:   # Проверяем находится ли участник первой группы во второй
            common_parts+=[i]
    return common_parts       


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_parts = find_common_participants(participants_first_group,participants_second_group,'|')
print(common_parts)
# TODO Провеьте работу функции с разделителем отличным от запятой
