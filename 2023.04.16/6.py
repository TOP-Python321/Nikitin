cell_one = input()
cell_two = input()    

if ('a' <= cell_one[0] <= 'h' 
    and 'a' <= cell_two[0] <= 'h' 
    and 1 <= int(cell_one[1]) <= 8 
    and 1 <= int(cell_two[1]) <= 8):
    if (-1 <= ord(cell_one[0]) - ord(cell_two [0]) <= 1 
        and -1 <= int(cell_one[1]) - int(cell_two [1]) <= 1):
        print('Да')
    else:
        print('Нет')
else:
    print('Не корректные координаты')
# Пример первого ввода: 
# d4
# c3

# Да

# Пример второго ввода:
# d4
# c8

# Нет