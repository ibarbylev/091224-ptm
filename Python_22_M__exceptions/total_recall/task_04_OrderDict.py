from collections import OrderedDict

ordered_dict = OrderedDict({'apple': 5, 'banana': 2, 'orange': 8})
print(ordered_dict)         # OrderedDict({'apple': 5, 'banana': 2, 'orange': 8})
ordered_dict.pop('apple')
print(ordered_dict)         # OrderedDict({'banana': 2, 'orange': 8})
ordered_dict["apple"] = 5
print(ordered_dict)         # OrderedDict({'banana': 2, 'orange': 8, 'apple': 5})
