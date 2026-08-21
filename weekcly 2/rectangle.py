def main():
    l = 5
    w = int(input("how many Width do you want?: "))
    print("O" * w)
    print("O" * w)
    print("O" * w)
    print("O" * w)
    print("O" * w)

    p = (2 * l) + (2 * w)
    print ("Perimeter:", p)
    a = (w * l)
    print("Area:", a)
    d = (l**2 + w**2)**(1/2)
    print("Diagonal:", d)
     

if __name__== "__main__":
        main()
