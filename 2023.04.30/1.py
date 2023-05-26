adres = input()
if '@' in adres and '.' in adres:
    print('да')
else:
    print('нет')

# Пример ввода 1:
    # andreynikitin@bk.ru
# Пример вывода 1:
    # да
# Пример ввода 2:
    # andreynikitin@bkru
# Пример вывода 2:
    # нет
