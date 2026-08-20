def main():

    transistors = 17800000000
    year = int(input("How many years into the future ? "))
    transistors *= 2 **(year/2)
    print(transistors)


if __name__== "__main__":
    main()
