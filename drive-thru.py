
def welcome():
    print("Welcome to Moreno Wings")
    print("Here is the menu: ")
    menu = ["Cheeseburger", "Fries","Soda","Ice Cream","Cookie"]

    for _ in menu:
        print(f"{menu.index(_)+1}.{_}")

def get_item(play):
        if play == "Cheeseburger" or play == "1":
            print("Here is your 🍔")
        elif play == "fries" or play == '2':
            print("Here is your 🍟")

        elif play == "soda" or play == '3':
            print("Here is your 🥤")

        elif play == "ice cream" or play == '4':
            print("Here is your 🍦")

        elif play == "cookie" or play == '5':
            print("Here is your 🍪")

        else:
            print("not a valid option")




def main ():
    welcome()
    user_selection = input("What item do you want? ").lower().strip()
    get_item(user_selection)

if __name__== "__main__":
    main()
