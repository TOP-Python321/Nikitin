text = input()
punctuation = '.,:;!?–—\'\"()*/'
# ИСПОЛЬЗОВАТЬ: можно не создавать список, если вы не собираетесь его использовать в таком качестве (а здесь вы этого не делаете) — метод join() ожидает итерируемый объект и прекрасно удовлетворится самим генераторным выражением
text_clean = ''.join(char for char in text if char not in punctuation)
print(text_clean)


# Было темно в гостиной. Лаптев, не садясь и держа шляпу в руках, стал извиняться за беспокойство; он спросил, что делать, чтобы сестра спала по ночам, и отчего она так страшно худеет, и его смущала мысль, что, кажется, эти самые вопросы он уже задавал доктору сегодня во время его утреннего визита.
# Было темно в гостиной Лаптев не садясь и держа шляпу в руках стал извиняться за беспокойство он спросил что делать чтобы сестра спала по ночам и отчего она так страшно худеет и его смущала мысль что кажется эти самые вопросы он уже задавал доктору сегодня во время его утреннего визита


# ИТОГ: отлично — 3/3