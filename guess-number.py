import random

def main():

    player = input("What is your name payer?" )
    print(f"Well, {player}, I am thinking of a number between 1 and 40")

    attempts = 0


    number = random.randint(1,40)
    while attempts < 7:
        guess = int(input("Is a number between 1-40"))

        if number > guess:
            print("Number to low")
        elif number < guess:
            print("Number to high")
        elif number == guess:
            print("Congratulations YOU GUESS MY NUMBER YOU WON")
            print(f"Number of attemps: {attempts}")
            break
        else:
            print("No valid number")

        attempts += 1



if __name__== "__main__":
    main()

