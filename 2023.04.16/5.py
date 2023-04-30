cell_one = input()
cell_two = input()

if ('a' <= cell_one[0] <= 'h' 
        and 'a' <= cell_two[0] <= 'h'
        and 1 <= int(cell_one[1]) <= 8
        and 1 <= int(cell_two[1]) <= 8):
    if cell_one[0] == cell_two[0] or int(cell_one[1]) == int(cell_two[1]):
        print('да')
    else:
        print('нет')
else:
    print('Не верно введены координаты')


# a4
# h4
# да

# a4
# h8
# нет


# ИТОГ: отлично — 3/3
