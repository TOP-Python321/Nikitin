volum_numbers = int(input(' '))

sum_numbers = 0

while volum_numbers > 0:
    number = int(input(' '))
    if number > 0: 
        sum_numbers += number
    volum_numbers -= 1

print(sum_numbers)


# Пример ввода:
     # 9
     # 15
     # 2
     # -9
     # 5
     # -15
     # 10

# Пример вывода:
    # 41
    