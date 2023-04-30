num = int(input())

# КОММЕНТАРИЙ: цифра — digit, число — number, num
num1 = num // 100
num2 = num % 100 // 10
num3 = num % 10

number_sum = num1 + num2 + num3
print('Сумма цифр =', number_sum)

mult = num1 * num2 * num3
print('Произведение цифр =', mult)


# 654
# Сумма цифр = 15
# Произведение цифр = 120


# ИТОГ: отлично — 4/4
