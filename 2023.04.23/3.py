number = int(input())
sum_numberb = 0

# ИСПРАВИТЬ: цикл ниже выполняет лишние итерации — подумайте, при каких значениях divider остаток от деления никогда не сможет быть равным нулю

# ИСПОЛЬЗОВАТЬ: всегда лучше называть вещи своими именами: например, делитель — делителем =)
# КОММЕНТАРИЙ: а имена переменных i, j, k традиционно используются почти только для индексов
for divider in range(1, number+1):
    if number % divider == 0:
        sum_numberb += divider
print(sum_numberb)    


# 100
# 217


# ИТОГ: хорошо, но нужно лучше — 2/4