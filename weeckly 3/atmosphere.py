def main ():
    atm = input("Decent atmosphere Layer: ")


    if atm == "Exosphere":
        print("Your altitude level will be between 700–10,000 km")
    elif atm == "Thermosphere":
        print("Your altitude level will be between 85–700 km" )
    elif atm == "Mesosphere":
        print("Your altitude level will be between 50–85 km")
    elif atm == "Stratosphere":
        print("Your altitude level will be between 12–50 km")
    elif atm == "Troposphere":
        print("Your altitude level will be between 0–12 km")
    else:
        print("ATMOSPHERE NOT FOUND IT")


    ex = float(input("Enter Exact Altitude: "))

    if ex >=700:
        print ("total decent time:", 16.0 + 230.0 + 175.0 + 506.7 + 600.0 )
    elif ex >=85:
        print("total decent time:", 230.0 + 175.0 + 506.7 + 600.0)
    elif ex >=50:
        print("total decent time:", 175.0 + 506.7 + 600.0)
    elif ex >=12:
        print("total decent time:", 506.7 + 600.0)
    elif ex >=0:
        print("total decent time:", 600.0)
    else:
        print("no found it")





if __name__== "__main__":
    main()
