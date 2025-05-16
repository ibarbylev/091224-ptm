count = 0  # global


def main():
    count_main = 1  # local
    print("count inside the main function", count)
    print("count_main inside the main function", count_main)


main()
print("count outside the main function", count)
print("count_main outside the main function", count_main)
