num_one = int(input())
num_two = int(input())
if num_one % num_two == 0:
    print(f'{num_one} делится на {num_two} нацело')
    print(f'частное: {num_one // num_two}')
else:
    print(f'{num_one} не делится на {num_two}')
    print(f'неполное частное: {num_one // num_two}')
    print(f'остаток: {num_one % num_two}')
    
    
# Пример ввода 1:    
# 8
# 2
# Пример вывода 1:
# 8 делится на 2 нацело
# частное: 4
# Пример ввода 2:
# 8
# 3
# Пример вывода 1:

# 8 не делится на 3
# неполное частное: 2
# остаток: 2
