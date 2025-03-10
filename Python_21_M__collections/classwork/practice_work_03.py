"""В аквариуме три рыбки, и их названия, виды и резервуары указываются в этих трёх кортежах.
Нужно организовать инвентарный список по резервуарам и получить список словарей рыб,
присутствующих в каждом резервуаре, в формате
{'name': name, 'species': species}
Используйте defaultdict для группировки рыб по резервуарам.
"""
from collections import defaultdict
from pprint import pprint

fish_inventory = [
    ("Sammy", "shark", "tank-a"),
    ("Jamie", "cuttlefish", "tank-b"),
    ("Mary", "squid", "tank-a"),
]

fish_in_tanks = defaultdict(list)
for fish_line in fish_inventory:
    name, species, tank = fish_line
    fish = {'name': name, 'species': species}
    fish_in_tanks[tank].append(fish)

pprint(dict(fish_in_tanks))

# {'tank-a': [{'name': 'Sammy', 'species': 'shark'},
#             {'name': 'Mary', 'species': 'squid'}],
#  'tank-b': [{'name': 'Jamie', 'species': 'cuttlefish'}]}
