import os
from pprint import pprint

# pprint(os.listdir('..'))
# pprint(os.listdir('.'))


for root, dirs, files in os.walk('..'):
    print(f' ====================== root : {root} =========================== ')
    print('dirs:')
    pprint(dirs)
    print('files:')
    pprint(files)