import itertools

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
combinations = itertools.combinations(letters, 2)
print(*combinations)
# ('a', 'b'), ('a', 'c'), ('b', 'c')

permutations = itertools.permutations(numbers)
print(*permutations)
# (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)

product = itertools.product(letters, numbers)
print(*product)
# ('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)
