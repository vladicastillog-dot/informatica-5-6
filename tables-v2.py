def main ():
    numbers = True
    while numbers:
        try:
            times_table = int(input("Welcome to the times table quiz Enter a times table that you would like to be tested on: "))
            numbers = False
        except ValueError:
              print("Invalid")
    max_value=int(input("Enter a maximum value for your times table: "))

    print(f"Here is the {times_table}times table")
    variable1 = 3

    for x in range(1, max_value + 1):
                    answer = x * int(times_table)
                    user = int(input(f"{x} times {times_table} is "))
                    if user == answer:
                            print("correct")
                    else:
                        print("incorrect")
                        variable1 -= 1
                    if variable1 == 0:
                           print("You faild")
                           break




if __name__== "__main__":
    main()
