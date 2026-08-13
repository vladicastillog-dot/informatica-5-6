def main():
    # planet = input("Planet:")

    # #Separation
    # print("Hello", planet)

    # #Concatenation
    # print("Hello " + planet)

    # # Formatted Strings
    # print(f"Hello {planet}")

    # #Ending
    # print("Hello", end=" ")
    # print(planet)

    name = input("What is your name? ")
    color = input("Whats your favorite colour? ")
    andjetive =input("Tell me an adjetive: ")
    goal = input("Tell me a goal: ")

    print(f"Hello, {name}!", end="\n\n")

    print("This is your story:")

    print(f"At dawn the sky turned {color}, and the air felt {andjetive}")
    print(f" I decided today I will finally {goal}")

if __name__ == "__main__":
    main()
