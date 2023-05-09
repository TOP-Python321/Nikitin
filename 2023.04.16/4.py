cell_one = input()
cell_two = input()

# sum_one = ord(cell_one[0]) + int(cell_one[1])
# sum_two = ord(cell_two[0]) + int(cell_two[1])
# sum_cells = sum_one + sum_two

# КОММЕНТАРИЙ: странный у вас порядок работы программы: сначала выполняются вычисления с полученными данными и только потом, спохватившись, программа проводит проверку на корректность введённых данных — это явно неудачное архитектурное решение
# if ('a' <= cell_one[0] <= 'h'
        # and 'a' <= cell_two[0] <= 'h'
        # ИСПРАВИТЬ: повторное вычисление int(cell_one[1]) — неоптимально
        # and 1 <= int(cell_one[1]) <= 8
        # and 1 <= int(cell_two[1]) <= 8):
    # if sum_cells % 2 == 0:
        # print('Да')
    # else:
        # print('Нет')
# else:
    # print('Не верно указан диапазон клеток')

sum_cells = (ord(cell_one[0]) + int(cell_one[1])) + (ord(cell_two[0]) + int(cell_two[1]))
if sum_cells % 2 == 0:
    print('Да')
else:
    print('Нет')

# КОММЕНТАРИЙ: что касается учебных задач, то обычно мы подразумеваем, что условный пользователь будет вводить требуемые данные всегда корректно — поэтому проверки на корректность вводимых данных можно не выполнять, пока в задании явным образом не сказано обратное


# a1
# e7
# Да

# a3
# b3
# Нет


# ИТОГ: переписать — 3/5
