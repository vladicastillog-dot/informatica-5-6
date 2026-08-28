def main ():

    print("calculator")
    num1 = int(input("Number1: "))
    num2 = int(input("Number2: "))
    ope = input("operation: ")

    if ope == "+":
        print(num1 + num2)
    elif ope == "*":
        print(num1 * num2)
    elif ope == "/":
        print(num1 / num2)
    elif ope == "-":
        print(num1 - num2)
    else:
        print()






if __name__== "__main__":
    main()
