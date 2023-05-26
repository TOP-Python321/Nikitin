scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

enter_word = input("Введите слово: ").upper()

scores_word = 0

for i in enter_word:
    for k, v in scores_letters.items():
        if i in v:
            scores_word += k
print(scores_word)

# Пример ввода:
    # щелкунчик

# Пример вывода:
    # 29
    