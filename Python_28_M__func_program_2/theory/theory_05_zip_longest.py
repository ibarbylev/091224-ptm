from itertools import zip_longest

letters = ['a', 'b', 'c']
numbers = [1, 2]

usual_zip = zip(letters, numbers)
print(*usual_zip)

longest_zip = zip_longest(letters, numbers)
print(*longest_zip)

longest_zip_2 = zip_longest(letters, numbers, fillvalue='Some Value')
print(*longest_zip_2)
