letters = 'AbltOJFHgtlbgndfWLFNT'

for i in range(len(letters)-1, -1, -1):
    print(i, len(letters))
    if letters[i].isupper():
        letters = letters.replace(letters[i], '')  # 6


print(letters)