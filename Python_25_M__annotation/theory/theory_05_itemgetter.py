from operator import itemgetter

data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 20}
]
print(sorted(data, key=itemgetter('age')))

print(sorted(data, key=lambda x: x.get('age')))


