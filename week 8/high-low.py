def main ():

    def highest(a,b):
        if a > b:
            print(f"the highest number is {a}")
        elif b > a:
            print(f"the highest numbert is {b}")
        elif b == a:
            print("both numbers are equal")
        else:
            print("no valid number")

    num1 = int(input("Enter a number: "))
    num2 = int(input("enter a number: "))

    highest(num1,num2)

    def lowest(a,b,c):
            if a < b and a < c:
                print(f"the loiwest number is {a}")
            elif b < a and b < c:
                print(f"the lowest numbert is {b}")
            elif c < a and c < b:
                print(f"the lowest number is {c}")
            elif c == a and b:
                print("the three are equal")
            elif b == a:
                print("both numbers are equal")
            else:
                print("no valid number")

    num1 = int(input("Enter a number: "))
    num2 = int(input("enter a number: "))
    num3 = int(input("enter a number: "))

    lowest(num1,num2,num3)




if __name__== "__main__":
    main()

