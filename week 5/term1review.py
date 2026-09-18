from datetime import datetime

def main ():

    day = datetime.now().weekday()
    days =["Monday", "Tuesday", "Wednesday", "Thursaday", "friday", "Saturday" , "Sunday"]
    print(days[day])


    #print("What day is it today?")
    #day= int(input())

    if day <= 4:
        print("Its a weekday")
        remaining = 5 - day
        print(remaining, "days until the weekend")
    elif day == 4:
        print("its Friday")
        print("Just a day left until the weekend")
    else:
        print("its the weekend!")

        months = ["January","February","March","April","May","June","July,"Agust","September","October","November","December"]

    print("These are the summer months:")
    print("Whan months is it? (1-12)")
    month = datetime.now().month
    print("it is",months[month-1])

    seasons = ["Winter","Spring","Summer","Atumn"]
    print("What month is it?(1-12)")

    if month <= 2 or month == 12:
        season = 0
    elif month<=5
        season = 1
    elif month <= 8:
        season = 2
    else:
        season = 3

    print("It is ",seasons[season])




if __name__== "__main__":
    main()
