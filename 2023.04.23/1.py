list_num = []
while True:
    enter_num = int(input(' '))
    if enter_num % 7 == 0:
        list_num.append(enter_num)
    else:
        print(*list_num[::-1])
# Пример ввода:
     # 49
     # 49
     # 56
     # 63
     # 70
     # 77
     # 84
     # 91
     # 98
     # 105
     # 112
     # 119
     # 120

# Пример вывода:
    # 119 112 105 98 91 84 77 70 63 56 49 49

  
    
    





