num = input()

num1 = int(num) // 100 
num2 =  int(num) % 100 // 10
num3 =int(num) % 10

sum = num1  + num2 + num3
print('Сумма цифр = ', sum)
mult= num1 * num2 * num3
print('Произведение цифр = ', mult)