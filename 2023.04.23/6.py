num_ticket = input()
num_list = [int(i) for i in num_ticket]
if sum(num_list[:3]) == sum(num_list[3:]):
    print('да')
else:
    print('нет')

# Пример ввода 1:
    # 912651

# Пример вывода 1:
    # да

# Пример ввода 2:
    # 632813

# Пример вывода 2:
    # нет
    

