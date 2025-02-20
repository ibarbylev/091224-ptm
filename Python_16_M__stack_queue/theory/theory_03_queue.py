from collections import deque

queue = deque()
queue.append(1)
print(queue)
queue.append(2)
print(queue)
first_element = queue.popleft()  # Извлечение первого элемента из очереди
print(first_element)  # 1
print(queue)

