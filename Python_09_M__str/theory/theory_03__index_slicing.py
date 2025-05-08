# Элемент строки можно получить по индексу (начиная с 0)

text = 'texts'
print(text[0])
print(text[1])
print(text[-1])


# Можно также получить (нарезать) символы в нужном порядке
print(text[0:2])    # te
print(text[:2])     # te
print(text[::2])    # txs
print(text[::-1])   # stxet

# копирование строки
text_2 = text[:]
print(text_2)

text_2 = text[::]
print(text_2)