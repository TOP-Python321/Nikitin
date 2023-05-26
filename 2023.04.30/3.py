first_list = input('Enter: ').split()
second_list = input('Enter: ').split()
first_list = ([j for j in first_list])
second_list = ([j for j in second_list])

for i in range(len(first_list)):
    if second_list == first_list[i:i + len(second_list)]:
        answer = "Да"
        break
    else:
        answer = "Нет"
        
print(answer)

# Пример ввода 1:
    # Enter: 1 2 3 
    # Enter: 1 2

# Пример вывода 1:
    # да

# Пример ввода 2:
    # Enter: 1 2 3 4
    # Enter: 2 4

# Пример вывода 2:
    # нет


