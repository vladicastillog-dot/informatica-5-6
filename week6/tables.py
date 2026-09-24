def main ():
    table = input("enter a number 1-10: ")
    while table != "exit":
        number = int(table)
        for x in range(1,11):
            print(f"{x} times {number} is {x*number}")
        table = input("enter a number 1-10")









if __name__== "__main__":
    main()
