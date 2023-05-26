f1, f2 = 1, 1
number = int(input())
if number == 1:
    print(f1)
elif number > 1:
    print(f1, f2, end=' ')
    for i in range(2, number):  
        f1, f2 = f2, f1 + f2
        print(f2, end=' ')


# 1
# 1

# 16
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987


# ИТОГ: отлично — 4/4
