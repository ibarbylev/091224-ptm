import os

os.makedirs('new_dir', exist_ok=True)
current_dir = os.getcwd()
new_path = os.path.join(current_dir, 'new_dir')
print(new_path)

os.chdir(new_path)
print(os.getcwd())

separator = os.path.sep  # / for Linux or \ for Windows
print('separator =', separator)

# Дальше код будет работать только для Linux и macOS
# для Windows слэш надо заменить на separator
if os.name == 'posix':

    new_path_lst = os.getcwd().split('/')
    print(new_path_lst)

    new_path = '/'.join(new_path_lst[:-1])
    print(new_path)

    os.chdir(new_path)
    print(os.getcwd())
    print(os.path.abspath('.'))
    print(os.path.abspath('..'))
    print(os.path.abspath('../../..'))


# os.path.exists()
print(os.path.exists(
        os.path.join(current_dir, 'new_dir')
    )
)

# os.path.isdir()
print(os.path.isdir('new_dir'))

# os.path.isfile()
print(os.path.isfile('theory_01_sys.py'))
