cell_one = input()
cell_two = input()
sum_one = ord(cell_one[0]) +  int(cell_one[1])
sum_two = ord(cell_two[0]) +  int(cell_two[1])
sum_cells =sum_one + sum_two

if ('a' <= cell_one[0] <= 'h' 
    and 'a' <= cell_two[0] <= 'h' 
    and 1 <= int(cell_one[1]) <= 8 
    and 1 <= int(cell_two[1]) <= 8):
    if sum_cells % 2 == 0:
        print('Да')
    else:
        print('Нет')    
else:
    print('Не верно укзан диапозон клеток')
# Пример первого ввода: 
# a1
# e7

# Да

# Пример второго ввода:
# a3
# b3

# Нет