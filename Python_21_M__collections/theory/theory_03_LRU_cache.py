from collections import OrderedDict


def lru_cache(capacity, cache, key, value):
    if key in cache:
        # Если ключ уже существует, обновляем значение и перемещаем элемент в конец словаря
        cache.pop(key)
    elif len(cache) >= capacity:
        # Если кэш переполнен, удаляем самый старый элемент (last=False)
        # if .popitem(last=True),  LIFO == stack
        # if .popitem(last=False), FIFO == queue
        cache.popitem(last=False)
    cache[key] = value


capacity = 3
cache = OrderedDict()


lru_cache(capacity, cache, "key1", "value1")
lru_cache(capacity, cache, "key2", "value2")
lru_cache(capacity, cache, "key3", "value3")

print(cache)  # Выводит OrderedDict([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])

lru_cache(capacity, cache, "key2", "new_value2")  # Обновляем значение "key2"
print(cache)  # Выводит OrderedDict([('key1', 'value1'), ('key3', 'value3'), ('key2', 'new_value2')])

lru_cache(capacity, cache, "key4", "value4")  # Кэш переполнен, удаляем "key1"
print(cache)  # Выводит OrderedDict([('key3', 'value3'), ('key2', 'new_value2'), ('key4', 'value4')])
