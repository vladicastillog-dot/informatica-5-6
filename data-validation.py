def main ():
    not_val = True

    while not_val:
        try:
            int(input("Enter a number between 1-10: "))
            not_val = False
        except ValueError:
            print("You Must enter a number 1-10")

if __name__== "__main__":
    main()
