def main ():
    print("Tacos el Moreno")
    rating = float(input("Rate the restaurant 1-5"))

    if rating > 5:
        print("Incorrect value ")
    elif rating > 4.5:
        print("Perfection")
    elif rating > 4:
        print("Excellent")
    elif rating > 3:
        print("Good")
    elif rating > 2:
        print("fair")
    else:
        print("poor")



if __name__== "__main__":
    main()
