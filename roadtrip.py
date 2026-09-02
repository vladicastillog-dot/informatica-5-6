def main():

    answer = ""
    followup = ""

    while answer != "Yes!":
        answer = input("Are we there yet? ").title().strip()
        if answer =="Yes":
            followup= input("Really? ")
        if followup == "Yes":
            break


    print("We are here!")


if __name__== "__main__":
    main()
