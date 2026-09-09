import random


def main():

    print("Learning Math problems")

    attempts = 0

    while attempts > 3:

        num1 = random.randit(1,99)
        num2 = random.randit(1,99)

        correct = num1 + num2
        print(f"What is {num1}+{num2}?")
        user = int(input("Your answer: "))

    if user == correct:
        print("Hurray!!")
        attempts += 1
        print(f"attempts: {'🌟' * attempts}")
    else:
        print("Incorrect answer")
        print(f"The answer was {correct}")
        attempts = 0

    print()

    print("Congratulations! You got 3 correct answers in a row ! 🌟")



if __name__== "__main__":
    main()
