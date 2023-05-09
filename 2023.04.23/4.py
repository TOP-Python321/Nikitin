num_discharge = int(input(' '))
max_num = int('9' * num_discharge)
coinc_numbers = 0
volum_num = 0
for i in range(2, max_num + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            coinc_numbers += 1
    if coinc_numbers == 2:     
        volum_num += 1
    coinc_numbers = 0
print(volum_num)

# Пример ввода:
    # 3

# Пример вывода:
    # 168  

