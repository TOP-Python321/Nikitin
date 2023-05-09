text = input('')      
count = 0          
if text[i] == ' ':
    count += 1
price = (len(text) - count) * 30
print(price // 100, 'руб.', price % 100, 'коп.')

# Пример ввода:
    # грузите апельсины бочках братья карамазовы

# Пример вывода:
    # 11 руб. 40 коп.
        


