import random

def main():
    coin = ["heads","tails"]
    attempts = 3
    while attempts >0:
        flip = random.choice(coin)
        guess = input("heads or tails?: ").strip().lowe()

        print("the coin landed on", flip)

    if guess == flip:
        print("winner")
        break
    else:
        print("loser")
        attempts -= 1
        print("attempts left:", attempts)


if __name__== "__main__":
    main()
