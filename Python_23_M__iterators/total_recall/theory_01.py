"""Что выведет на экран этот код?"""


import sys


try:
    sys.exit(1)
except Exception as e:
    print(f"Исключение SystemExit: {e}")

