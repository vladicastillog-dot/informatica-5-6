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

    name = input("What is your name? ").strip().title()
    color = input("Whats your favorite colour? ").strip().lower()
    andjetive =input("Tell me an adjetive: ").strip().lower()
    goal = input("Tell me a goal: ").strip().lower()

    print(f"Hello, {name}!")

    print("This is your story:")

    print(f"At dawn the sky turned {color}, and the air felt {andjetive}, I decided today I will finally {goal}")

    print(f"At dawn the sky turned {color}, and the air felt {andjetive}, I decided today I will finally {goal}".upper())






if __name__ == "__main__":
    main()
