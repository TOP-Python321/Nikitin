fruits = []
while True:
    fruit = input()
    if not fruit:
        break
    fruits.append(fruit)
if len(fruits) >= 2:
    fruits = fruits[:-2] + [' и '.join(fruits[-2:])]
print(*fruits, sep = ', ')

# Пример ввода 1:
    # яблоко
# Пример вывода 1:
    # яблоко
# Пример ввода 2:
    # яблоко
    # груша
# Пример вывода 2:
    # яблоко и груша
# Пример ввода 3:
    # яблоко
    # груша
    # апельсин
# Пример вывода 3:
    # яблоко, груша и апельсин
# Пример ввода 4:
    # яблоко
    # груша
    # апельсин
    # лимон
# Пример вывода 4:
    # яблоко, груша, апельсин и лимон