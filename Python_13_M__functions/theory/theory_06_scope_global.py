count = 0


def main():
    global count
    count += 1
    print("inside the main function", count)


print("before function main", count)
main()
print("after function main", count)
