list_num = []
while True:
    enter_num = int(input(' '))
    if enter_num % 7 == 0:
        # КОММЕНТАРИЙ: в более сложных циклах тело цикла будет более длинным и сложным для восприятия, поэтому лучшей практикой будет вывести действия, выполняемые по завершении цикла, за пределы тела цикла
        list_num.append(enter_num)
        # ДОБАВИТЬ: должен быть выход из цикла, сейчас работу этого кода можно прервать только принудительно
    else:
        print(*list_num[::-1])


# ИСПОЛЬЗОВАТЬ здесь и далее везде: не надо добавлять строки Пример ввода и Пример вывода — смотрите, как я правлю и далее делайте по аналогии

#  49
#  49
#  56
#  63
#  70
#  77
#  84
#  91
#  98
#  105
#  112
#  119
#  120
# 119 112 105 98 91 84 77 70 63 56 49 49


# ИТОГ: доработать — 2/3